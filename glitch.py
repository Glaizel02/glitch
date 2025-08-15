import random
import time
import asyncio
import aiohttp
import re
import os
import json
import string
import uuid
import requests
import urllib.parse
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.table import Table
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Optional, Tuple, Union
import rich.box

class LocalDBManager:
    def __init__(self):
        self.db_file = "resources.json"
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump([], f)
    
    def _save_resources(self, resources: List) -> None:
        with open(self.db_file, 'w') as f:
            json.dump(resources, f, indent=2)
    
    def get_resources(self) -> List:
        with open(self.db_file, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    
    def add_resource(self, resource: Dict) -> None:
        resources = self.get_resources()
        resources.append(resource)
        self._save_resources(resources)
    
    def remove_resource(self, index: int) -> bool:
        resources = self.get_resources()
        if 0 <= index < len(resources):
            del resources[index]
            self._save_resources(resources)
            return True
        return False

class FacebookTokenGetter:
    def __init__(self):
        self.useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1"
        self.endpoints = {
            "b_graph": "https://b-graph.facebook.com",
            "key": "https://b-api.facebook.com",
            "business": "https://business.facebook.com",
            "auth": "https://b-api.facebook.com/method/auth.login"
        }
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.useragent,
            'Accept-Language': 'en_US'
        })
        self.request_timeout = 30

    def fetch_cookies(self, email: str, password: str) -> Dict:
        """Fetch Facebook cookies using email and password"""
        try:
            params = {
                'adid': str(uuid.uuid4()),
                'email': email,
                'password': password,
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'locale': 'en_US',
                'client_country_code': 'US',
                'credentials_type': 'device_based_login_password',
                'generate_session_cookies': '1',
                'generate_analytics_claim': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'irisSeqID': '1',
                'try_num': '1',
                'enroll_misauth': 'false',
                'meta_inf_fbmeta': 'NO_FILE',
                'source': 'login',
                'machine_id': ''.join(random.choices(string.ascii_letters + string.digits, k=22)),
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            
            full_url = self.endpoints['auth'] + "?" + urllib.parse.urlencode(params)
            response = self.session.get(full_url, timeout=self.request_timeout)
            response.raise_for_status()
            data = response.json()
            
            if 'session_cookies' in data:
                cookies = "; ".join(
                    f"{cookie['name']}={cookie['value']}"
                    for cookie in data['session_cookies']
                )
                return {
                    "cookies": cookies,
                    "status": "success",
                    "message": "Cookies obtained successfully"
                }
            else:
                error_msg = data.get('error_msg', data.get('error', {}).get('message', 'Unknown error'))
                return {
                    "status": "error",
                    "message": f"Failed to get cookies: {error_msg}"
                }
                
        except requests.exceptions.Timeout:
            return {
                "status": "error",
                "message": "Login request timed out"
            }
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "message": f"Network error during login: {str(e)}"
            }
        except json.JSONDecodeError:
            return {
                "status": "error",
                "message": "Invalid response from login server"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Unexpected error: {str(e)}"
            }

    def get_eaaau_token(self, email: str, password: str) -> Dict:
        try:
            headers = {
                'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-friendly-name': 'Authenticate',
                'x-fb-connection-type': 'Unknown',
                'accept-encoding': 'gzip, deflate',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            data = {
                'adid': ''.join(random.choices(string.hexdigits, k=16)),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': email,
                'password': password,
                'generate_analytics_claims': '0',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '0',
                'fb_api_req_friendly_name': 'authenticate',
            }
            
            response = self.session.post(
                f"{self.endpoints['b_graph']}/auth/login",
                headers=headers,
                data=data
            ).json()
            
            if 'session_key' in response:
                cookies = "; ".join(
                    f"{cookie['name']}={cookie['value']}" 
                    for cookie in response.get('session_cookies', [])
                )
                return {
                    "token": response["access_token"].strip(),
                    "cookies": cookies,
                    "status": "success"
                }
            else:
                error = response.get('error', {})
                return {
                    "status": "error",
                    "message": error.get('message', 'Unknown error')
                }
                
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    def get_eaad6v7_token(self, eaaau_token: str) -> Dict:
        try:
            url = f"{self.endpoints['key']}/method/auth.getSessionforApp?format=json&access_token={eaaau_token.strip()}&new_app_id=275254692598279"
            response = self.session.get(url).json()
            
            if 'access_token' in response:
                return {
                    "token": response["access_token"].strip(),
                    "status": "success"
                }
            else:
                return {
                    "status": "error",
                    "message": response.get('error', {}).get('message', 'Failed to get EAAD6V7 token')
                }
                
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    def get_eaag_token(self, cookies: str) -> Dict:
        try:
            headers = {
                'authority': 'business.facebook.com',
                'cookie': cookies,
                'referer': 'https://www.facebook.com/',
                'user-agent': self.useragent
            }
            
            response = self.session.get(
                'https://business.facebook.com/content_management',
                headers=headers,
                timeout=self.request_timeout
            )
            
            if 'EAAG' in response.text:
                token = response.text.split('EAAG')[1].split('","')[0]
                return {
                    "token": f"EAAG{token}".strip(),
                    "status": "success"
                }
            return {
                "status": "error",
                "message": "EAAG token not found"
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    def get_all_tokens(self, email: str, password: str) -> Dict:
        """Get all tokens (cookies, EAAAAU, EAAD6V7, EAAG) in one call"""
        result = {
            "status": "success",
            "cookies": None,
            "eaaau": None,
            "eaad6v7": None,
            "eaag": None,
            "errors": []
        }
        
        # First get cookies and EAAAAU token
        eaaau_result = self.get_eaaau_token(email, password)
        if eaaau_result.get("status") != "success":
            result["status"] = "error"
            result["errors"].append(f"EAAAAU: {eaaau_result.get('message', 'Unknown error')}")
            return result
        
        result["cookies"] = eaaau_result["cookies"]
        result["eaaau"] = eaaau_result["token"]
        
        # Get EAAD6V7 token
        eaad6v7_result = self.get_eaad6v7_token(eaaau_result["token"])
        if eaad6v7_result.get("status") == "success":
            result["eaad6v7"] = eaad6v7_result["token"]
        else:
            result["errors"].append(f"EAAD6V7: {eaad6v7_result.get('message', 'Unknown error')}")
        
        # Get EAAG token from cookies
        eaag_result = self.get_eaag_token(eaaau_result["cookies"])
        if eaag_result.get("status") == "success":
            result["eaag"] = eaag_result["token"]
        else:
            result["errors"].append(f"EAAG: {eaag_result.get('message', 'Unknown error')}")
        
        return result

class FacebookAutoShare:
    def __init__(self):
        self.version = '1.0.1'
        self.dev = 'CYZSH'
        self.console = Console()
        self.api_version = 'v22.0'
        self.user_agents = self._generate_user_agents()
        self.user_agent = random.choice(self.user_agents)
        self.session = None
        self.executor = ThreadPoolExecutor(max_workers=100)
        self.connector = aiohttp.TCPConnector(limit=0, force_close=True)
        self.concurrent = 17
        self.start_time = None
        self.error_log = []
        self.db = LocalDBManager()
        self.interval = 0
        self.REQUEST_TIMEOUT = 30
        self.current_menu = "main"
        self.token_getter = FacebookTokenGetter()

    def _generate_user_agents(self):
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
        ]

    @staticmethod
    def get_headers(cookie: str = None) -> Dict:
        headers = {
            "User-Agent": random.choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
            ]),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        }
        if cookie:
            headers["Cookie"] = cookie
        return headers

    def loading(self, duration: float = 2, message: str = "Processing") -> None:
        symbols = ['◉', '◎', '◌', '◍']
        end_time = time.time() + duration
        while time.time() < end_time:
            for symbol in symbols:
                print(f"\033[93m{symbol} {message}...\033[0m", end='\r')
                time.sleep(0.1)
        print(" " * (len(message) + 10), end='\r')

    def print_panel(self, title, content, color):
        self.console.print(Panel(
            content,
            title=title,
            width=None,
            padding=(1, 3),
            border_style=color,
            title_align="left",
            style=f"bold {color}",
            box=rich.box.ROUNDED
        ))

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_banner(self):
        banner = r"""
               [magenta]  ██████╗ ██╗      ██╗ ████████╗  ██████╗ ██╗  ██╗
               [medium_purple]██╔════╝  ██║      ██║ ╚══██╔══╝ ██╔════╝ ██║  ██║
               [orchid]██║  ███╗ ██║      ██║    ██║    ██║      ███████║
               [deep_pink4]██║   ██║ ██║      ██║    ██║    ██║      ██╔══██║
               [bright_magenta]╚██████╔╝ ███████╗ ██║    ██║    ╚██████╗ ██║  ██║
               [magenta] ╚═════╝  ╚══════╝ ╚═╝    ╚═╝     ╚═════╝ ╚═╝  ╚═╝
        """
        menu_modes = {
            'main': 'Main Menu',
            'share': 'Spam Share',
            'resources': 'Resource Management',
            'token_gen': 'Token Generator'
        }
        current_mode = menu_modes.get(self.current_menu, 'Main Menu')
        
        info = f"""
[›] 𝐓𝐎𝐎𝐋: 𝐅𝐁 𝐒𝐩𝐚𝐦 𝐒𝐡𝐚𝐫𝐞
[›] 𝐕𝐞𝐫𝐬𝐢𝐨𝐧: 𝟏.𝟏
[›] 𝐃𝐞𝐯: 𝐆𝐋𝐈𝐓𝐂𝐇𝐁𝐘𝐀𝐍𝐍𝐈𝐄
[›] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐜𝐭𝐢𝐯𝐞
[›] 𝐏𝐚𝐧𝐞𝐥: {current_mode}
        """
        self.print_panel('', banner, "bright_cyan")
        self.print_panel('INFO', info, "bright_blue")

    def show_main_menu(self):
        self.current_menu = "main"
        self.clear_screen()
        self.show_banner()
        self.print_panel(
            "Main Menu",
             "[𝟏] 𝐈𝐍𝐈𝐓𝐈𝐀𝐋𝐈𝐙𝐄 𝐒𝐏𝐀𝐌𝐒𝐇𝐀𝐑𝐄\n"
             "[𝟐] 𝐌𝐀𝐍𝐀𝐆𝐄 𝐑𝐄𝐒𝐎𝐔𝐑𝐂𝐄𝐒\n"
             "[𝟑] 𝐓𝐎𝐊𝐄𝐍 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑\n"
             "[𝟒] 𝐄𝐗𝐈𝐓",
            "bright_green"
        )

    def show_share_menu(self):
        self.current_menu = "share"
        self.clear_screen()
        self.show_banner()
        self.print_panel(
            "Spam Share",
           "[𝟏] 𝐒𝐇𝐀𝐑𝐄 𝐀𝐒 𝐔𝐒𝐄𝐑\n"
           "[𝟐] 𝐒𝐇𝐀𝐑𝐄 𝐀𝐒 𝐏𝐀𝐆𝐄\n"
           "[𝟑] 𝐂𝐎𝐌𝐁𝐈𝐍𝐄𝐃 𝐒𝐇𝐀𝐑𝐈𝐍𝐆\n"
           "[𝟎] 𝐁𝐀𝐂𝐊 𝐓𝐎 𝐌𝐀𝐈𝐍",
            "bright_yellow"
        )

    async def show_resource_management(self):
        self.current_menu = "resources"
        self.clear_screen()
        self.show_banner()
        
        resources = self.db.get_resources()
        
        table = Table(
            title=f"[bold bright_cyan]Resources[/] (Testing {len(resources)} entries...)",
            show_header=True,
            header_style="bold bright_blue",
            width=59,
            border_style="bright_green"
        )
        
        table.add_column("#", style="dim", width=4)
        table.add_column("Type", width=8)
        table.add_column("Content", width=12)
        table.add_column("Status", width=12)
        table.add_column("Details", width=16)
    
        tested_resources = []
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=25),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            transient=True
        ) as progress:
            task = progress.add_task("Validating...", total=len(resources))
            
            for idx, resource in enumerate(resources):
                status = ""
                details = ""
                
                if isinstance(resource, dict):
                    if 'cookie' in resource:
                        token = self.get_token_from_cookie(resource['cookie'])
                        if token:
                            test_result = await self.verify_token(token)
                            status = "[green]✓ LIVE[/]" if test_result['valid'] else "[red]DEAD[/]"
                            details = f"{len(test_result.get('pages', []))} pages" if test_result['valid'] else "Invalid"
                        else:
                            status = "[red]INVALID[/]"
                            details = "Bad cookie"
                        
                        tested_resources.append({
                            'type': "Cookie",
                            'content': resource['cookie'],
                            'status': status,
                            'details': details
                        })
                        
                    elif 'token' in resource:
                        test_result = await self.verify_token(resource['token'])
                        if test_result['valid']:
                            status = "[green]✓ LIVE[/]"
                            details = f"{len(test_result.get('pages', []))} pages"
                        else:
                            status = "[red]DEAD[/]"
                            details = test_result.get('error', 'Invalid')[:12]
                        
                        tested_resources.append({
                            'type': "Token",
                            'content': resource['token'],
                            'status': status,
                            'details': details
                        })
                
                progress.update(task, advance=1)
                await asyncio.sleep(0.1)
    
        for idx, res in enumerate(tested_resources):
            content_preview = (res['content'][:7] + '...') if len(res['content']) > 19 else res['content']
            table.add_row(
                str(idx),
                res['type'],
                content_preview,
                res['status'],
                res['details']
            )
    
        self.console.print(table)
        self.print_panel(
            "Controls",
            "[1] Add  [2] Remove  [3] Test All  [0] Back",
            "bright_magenta"
        )

    async def show_token_generator(self):
        self.current_menu = "token_gen"
        self.clear_screen()
        self.show_banner()
        
        self.print_panel(
            "Token Generator",
           "[𝟏] 𝐆𝐄𝐓 𝐓𝐎𝐊𝐄𝐍𝐒+𝐂𝐎𝐎𝐊𝐈𝐄𝐒\n"
           "[𝟐] 𝐆𝐄𝐓 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 𝐎𝐍𝐋𝐘\n"
           "[𝟑] 𝐆𝐄𝐓 𝐄𝐀𝐀𝐆 𝐓𝐎𝐊𝐄𝐍 𝐅𝐑𝐎�	M 𝐂𝐎𝐎𝐊𝐈𝐄𝐒\n"
           "[𝟎] 𝐁𝐀𝐂𝐊 𝐓𝐎 𝐌𝐀𝐈𝐍",
            "bright_cyan"
        )
        
        choice = input("\n[›] Select: ")
        
        if choice == "0":
            self.current_menu = "main"
        elif choice == "1":
            await self.get_all_tokens()
        elif choice == "2":
            await self.get_cookies_only()
        elif choice == "3":
            await self.get_eaag_from_cookies()
        else:
            self.print_panel("Error", "Invalid choice", "red")
            time.sleep(1)

    async def get_all_tokens(self):
        self.clear_screen()
        self.show_banner()
        
        email = input("[›] 𝐄𝐌𝐀𝐈𝐋/𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: ")
        password = input("[›] 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃: ")
        
        self.loading(3, "Authenticating")
        
        result = self.token_getter.get_all_tokens(email, password)
        
        self.clear_screen()
        self.show_banner()
        
        if result["status"] == "error":
            self.print_panel("Error", result["errors"][0], "red")
            input("\n[Press Enter to continue]")
            await self.show_token_generator()
        
        table = Table(title="Generated Tokens", show_header=True, header_style="bold bright_blue", border_style="bright_cyan")
        table.add_column("Token Type", style="bright_green")
        table.add_column("Value", style="white")
        
        table.add_row("Cookies", result["cookies"] or "[red]Failed to get[/red]")
        table.add_row("EAAAAU Token", result["eaaau"] or "[red]Failed to get[/red]")
        
        if result["eaad6v7"]:
            table.add_row("EAAD6V7 Token", result["eaad6v7"])
        else:
            table.add_row("EAAD6V7 Token", "[red]Failed to get[/red]")
            
        if result["eaag"]:
            table.add_row("EAAG Token", result["eaag"])
        else:
            table.add_row("EAAG Token", "[red]Failed to get[/red]")
        
        self.console.print(table)
        
        if result["errors"]:
            self.print_panel("Partial Errors", "\n".join(result["errors"]), "yellow")
        
        save = input("\n[›] Save to resources? (y/n): ").lower()
        if save == 'y':
            if result["cookies"]:
                self.db.add_resource({"cookie": result["cookies"]})
            if result["eaaau"]:
                self.db.add_resource({"token": result["eaaau"]})
            if result["eaad6v7"]:
                self.db.add_resource({"token": result["eaad6v7"]})
            if result["eaag"]:
                self.db.add_resource({"token": result["eaag"]})
            self.print_panel("Success", "Tokens saved to resources!", "green")
        
        input("\n[Press Enter to continue]")
        await self.show_token_generator()

    async def get_cookies_only(self):
        self.clear_screen()
        self.show_banner()
        
        email = input("[›] Email/Username: ")
        password = input("[›] Password: ")
        
        self.loading(3, "Fetching Cookies")
        
        result = self.token_getter.fetch_cookies(email, password)
        
        self.clear_screen()
        self.show_banner()
        
        if result["status"] == "error":
            self.print_panel("Error", result["message"], "red")
        else:
            self.print_panel("Success", "Cookies obtained successfully!", "green")
            self.print_panel("Cookies", result["cookies"], "bright_blue")
            
            save = input("\n[›] Save to resources? (y/n): ").lower()
            if save == 'y':
                self.db.add_resource({"cookie": result["cookies"]})
                self.print_panel("Success", "Cookies saved to resources!", "green")
        
        input("\n[Press Enter to continue]")
        await self.show_token_generator()

    async def get_eaag_from_cookies(self):
        self.clear_screen()
        self.show_banner()
        
        cookies = input("[›] Enter cookies: ")
        
        self.loading(3, "Extracting EAAG Token")
        
        result = self.token_getter.get_eaag_token(cookies)
        
        self.clear_screen()
        self.show_banner()
        
        if result["status"] == "error":
            self.print_panel("Error", result["message"], "red")
        else:
            self.print_panel("Success", "EAAG Token retrieved successfully!", "green")
            self.print_panel("EAAG Token", result["token"], "bright_blue")
            
            save = input("\n[›] Save to resources? (y/n): ").lower()
            if save == 'y':
                self.db.add_resource({"token": result["token"]})
                self.print_panel("Success", "Token saved to resources!", "green")
        
        input("\n[Press Enter to continue]")
        await self.show_token_generator()

    async def create_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession(
                connector=self.connector,
                headers={'User-Agent': self.user_agent},
                timeout=aiohttp.ClientTimeout(total=self.REQUEST_TIMEOUT)
            )

    async def close_session(self):
        if self.session and not self.session.closed:
            await self.session.close()
        self.executor.shutdown(wait=True)

    def get_token_from_cookie(self, cookie: str) -> Optional[str]:
        try:
            response = requests.get(
                "https://business.facebook.com/content_management",
                headers=self.get_headers(cookie),
                timeout=self.REQUEST_TIMEOUT
            )
            response.raise_for_status()
            token = response.text.split("EAAG")[1].split('","')[0]
            return f"EAAG{token}"
        except Exception as e:
            self.error_log.append(f"Cookie Error: {str(e)}")
            return None

    def load_tokens(self) -> List[Dict]:
        resources = self.db.get_resources()
        valid_tokens = []
        
        for item in resources:
            if isinstance(item, dict):
                if item.get('token'):
                    valid_tokens.append({'token': item['token'], 'type': 'token'})
                elif item.get('cookie'):
                    token = self.get_token_from_cookie(item['cookie'])
                    if token:
                        valid_tokens.append({'token': token, 'type': 'cookie'})
        return valid_tokens

    async def verify_token(self, token: str) -> Dict:
        try:
            await self.create_session()
            async with self.session.get(
                f"https://graph.facebook.com/{self.api_version}/me/accounts",
                params={'access_token': token},
                timeout=10
            ) as resp:
                data = await resp.json()
                if resp.status == 200:
                    pages = [{
                        'name': page['name'],
                        'access_token': page['access_token'],
                        'id': page['id']
                    } for page in data.get('data', [])]
                    return {'valid': True, 'pages': pages}
                return {'valid': False, 'error': data.get('error', {}).get('message', 'Unknown error')}
        except Exception as e:
            return {'valid': False, 'error': str(e)}

    async def get_post_id(self, post_link: str) -> Optional[str]:
        """Extract post ID from URL"""
        self.loading(2, "Finding post ID")
        try:
            await self.create_session()
            async with self.session.post(
                "https://id.traodoisub.com/api.php",
                data={"link": post_link},
                timeout=10
            ) as resp:
                if (await resp.json()).get('id'):
                    return (await resp.json())['id']

            patterns = [
                r'facebook\.com\/.+\/(?:posts|photos|activity)\/(\d+)',
                r'story_fbid=(\d+)&id=(\d+)',
                r'facebook\.com\/(\d+_\d+)'
            ]
            for pattern in patterns:
                match = re.search(pattern, post_link)
                if match:
                    return f"{match.group(1)}_{match.group(2)}" if len(match.groups()) > 1 else match.group(1)
            return None
        except Exception as e:
            self.print_panel("", f"Failed to get post ID: {str(e)}", "red")
            self.error_log.append(f"Post ID Error: {str(e)}")
            return None

    async def perform_share(self, token: str, target_id: str, is_page: bool = False) -> bool:
        try:
            params = {
                "link": f"https://m.facebook.com/{target_id}",
                "published": "0",
                "access_token": token
            }
            endpoint = f"{target_id}/feed" if is_page else "me/feed"
            
            async with self.session.post(
                f"https://graph.facebook.com/{self.api_version}/{endpoint}",
                params=params,
                timeout=5
            ) as resp:
                data = await resp.json()
                if resp.status != 200:
                    self.error_log.append(f"Share Error: {data.get('error', {}).get('message', 'Unknown error')}")
                    return False
                return data.get('id') is not None
        except Exception as e:
            self.error_log.append(f"Share Exception: {str(e)}")
            return False

    async def burst_share(self, share_type: int, post_id: str, total_shares: int) -> Tuple[int, int]:
        tokens = self.load_tokens()
        pages = []
        
        if share_type in [2, 3]:
            for token_data in tokens.copy():
                result = await self.verify_token(token_data['token'])
                if result['valid'] and result.get('pages'):
                    pages.extend(result['pages'])
                    if share_type == 2:  # Pages only mode
                        tokens.remove(token_data)

        success = failed = 0
        self.start_time = time.time()
        
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=25),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            transient=True
        ) as progress:
            task = progress.add_task("Sharing...", total=total_shares)
            
            while success + failed < total_shares:
                try:
                    if share_type == 1 and tokens:  # User only
                        token = random.choice(tokens)['token']
                        result = await self.perform_share(token, post_id)
                    elif share_type == 2 and pages:  # Page only
                        page = random.choice(pages)
                        result = await self.perform_share(page['access_token'], page['id'], True)
                    elif share_type == 3:  # Combined
                        if tokens and (not pages or random.choice([True, False])):
                            token = random.choice(tokens)['token']
                            result = await self.perform_share(token, post_id)
                        elif pages:
                            page = random.choice(pages)
                            result = await self.perform_share(page['access_token'], page['id'], True)
                        else:
                            break
                    else:
                        break
                    
                    if result:
                        success += 1
                    else:
                        failed += 1
                    
                    progress.update(task, advance=1)
                    
                    if self.interval > 0:
                        await asyncio.sleep(self.interval)
                except Exception as e:
                    failed += 1
                    self.error_log.append(f"Task Error: {str(e)}")
        
        return success, failed

    async def run_share_process(self, share_type: int, post_link: str, total_shares: int):
        self.clear_screen()
        self.show_banner()
        
        post_id = await self.get_post_id(post_link)
        if not post_id:
            self.print_panel("Error", "Failed to get post ID", "red")
            return
        
        self.print_panel("Info", f"Post ID: {post_id}", "green")
        
        tokens = self.load_tokens()
        if not tokens:
            self.print_panel("Error", "No valid tokens/cookies found", "red")
            return
        
        self.print_panel("Status", f"Starting {total_shares} shares...", "bright_blue")
        success, failed = await self.burst_share(share_type, post_id, total_shares)
        elapsed = time.time() - self.start_time
        
        self.print_panel("Results",
            f"Success: {success}\n"
            f"Failed: {failed}\n"
            f"Time: {elapsed:.2f}s\n"
            f"Speed: {success/max(1, elapsed):.1f}/s",
            "green" if success >= total_shares * 0.7 else "yellow"
        )

    async def run(self):
        while True:
            if self.current_menu == "main":
                self.show_main_menu()
                choice = input("\n[›] Select: ")
                
                if choice == "1":
                    self.show_share_menu()
                elif choice == "2":
                    await self.manage_resources()
                elif choice == "3":
                    await self.show_token_generator()
                elif choice == "4":
                    break
                
            elif self.current_menu == "share":
                self.show_share_menu()
                choice = input("\n[›] Select: ")
                
                if choice == "0":
                    self.current_menu = "main"
                elif choice in ["1", "2", "3"]:
                    post_link = input("[›] Post URL: ")
                    amount = int(input("[›] Share count: ") or 5)
                    self.interval = float(input("[›] Delay (seconds): ") or 3)
                    
                    await self.run_share_process(int(choice), post_link, amount)
                    input("\n[Press Enter to continue]")
                else:
                    self.print_panel("Error", "Invalid choice", "red")
                    time.sleep(1)

            elif self.current_menu == "resources":
                await self.manage_resources()

    async def manage_resources(self):
        while True:
            await self.show_resource_management()
            choice = input("\n[›] Select: ")
            
            if choice == "0":
                self.current_menu = "main"
                break
            elif choice == "1":
                resource = input("[›] Enter cookie/token: ").strip()
                if not resource:
                    self.print_panel("Error", "Cannot be empty", "red")
                else:
                    resource_type = 'cookie' if ('c_user=' in resource or 'xs=' in resource) else 'token'
                    self.db.add_resource({resource_type: resource})
                    self.print_panel("Success", "Resource added!", "green")
                time.sleep(1)
            elif choice == "2":
                try:
                    index = int(input("[›] Index to remove: "))
                    if self.db.remove_resource(index):
                        self.print_panel("Success", "Resource removed!", "green")
                    else:
                        self.print_panel("Error", "Invalid index", "red")
                    time.sleep(1)
                except ValueError:
                    self.print_panel("Error", "Enter a number", "red")
                    time.sleep(1)
            elif choice == "3":
                await self.show_resource_management()
                time.sleep(1)
            else:
                self.print_panel("Error", "Invalid choice", "red")
                time.sleep(1)

async def main():
    tool = FacebookAutoShare()
    try:
        await tool.run()
    finally:
        await tool.close_session()

if __name__ == "__main__":
    asyncio.run(main())
