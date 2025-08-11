import time
import sys
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Auto-install matching ChromeDriver for your Chromium
chromedriver_autoinstaller.install()

# Unicode handling
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# Chrome options for Termux headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Start Chrome
driver = webdriver.Chrome(options=chrome_options)

# Data storage
names, video_links, dates, views = [], [], [], []

# Facebook video page URLs to scrape
urls = [
    'https://www.facebook.com/pg/RenaultIndia/videos/?ref=page_internal',
    'https://www.facebook.com/pg/HyundaiIndia/videos/?ref=page_internal',
    'https://www.facebook.com/pg/datsunindia/videos/?ref=page_internal'
    # Add more here...
]

# Login to Facebook
driver.get('https://www.facebook.com')
try:
    username = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "pass")
    username.send_keys("*******")  # Your Facebook email
    password.send_keys("*******")  # Your Facebook password
    login_attempt = driver.find_element(By.XPATH, "//*[@type='submit']")
    login_attempt.submit()
    time.sleep(5)
except:
    print("Login failed or not needed.")

# Loop through URLs
for url in urls:
    count = 0
    print("Scraping:", url)
    try:
        driver.get(url)
    except:
        print("Error fetching:", url)
        continue
    time.sleep(5)

    SCROLL_PAUSE_TIME = 3
    last_height = driver.execute_script("return document.body.scrollHeight")

    tmp, tmp1, tmp2, tmp3 = [], [], [], []

    while count <= 100:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    page_html = BeautifulSoup(driver.page_source, "html.parser")
    mv_containers = page_html.find_all("div", class_="_u3y")

    for container in mv_containers:
        # Video name
        try:
            name = container.find('div', class_='_3v4h _48gm _50f3 _50f7').text
            tmp.append(name)
        except:
            tmp.append("No Data")

        # Video link
        try:
            video_link = container.find('a', href=True)['href']
            tmp1.append("https://www.facebook.com" + str(video_link))
        except:
            tmp1.append("No Data")

        # Views
        try:
            view = container.find('span', class_='fcg').text.split(' ')[0]
            if view.endswith('K'):
                view = float(view[:-1]) * 1000
            elif view.endswith('M'):
                view = float(view[:-1]) * 1000000
            else:
                view = float(view)
            tmp2.append(view)
        except:
            tmp2.append("No Data")

        # Upload date
        try:
            date = container.find('div', class_='fsm fwn fcg').text
            tmp3.append(date.split('·')[1])
        except:
            tmp3.append("No Data")

        count += 1

    names += tmp
    video_links += tmp1
    views += tmp2
    dates += tmp3

driver.quit()

# Save to CSV
with open('facebook_videos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Video Name', 'Views', 'Video Link', 'Upload Date'])
    for name, view, link, date in zip(names, views, video_links, dates):
        writer.writerow([name, view, link, date])

print("✅ Data saved to facebook_videos.csv")
'https://www.facebook.com/pg/SkodaIndia/videos/?ref=page_internal',
'https://www.facebook.com/pg/MSArenaOfficial/videos/?ref=page_internal'



driver.get('https://www.facebook.com')

try:
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    #Your emmail id and password for the facebook account goes here.
    username.send_keys("*******")
    password.send_keys("*******")
    #Clicks on the Submit button after typing in the login credentials.
    login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
    login_attempt.submit()
    time.sleep(5)
except:
    pass

#For loop to loop through the list urls.
for url in urls:
    count = 0
    print("url" + url)
    try :
        driver.get(url)
    except:
        print("error fetching the url")
        continue
    time.sleep(5)

    page = driver.page_source

    soup_expatistan = BeautifulSoup(page, "html.parser")

    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    tmp = []
    tmp1=[]
    tmp2=[]
    tmp3=[]
    while count <=100 :

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        print("new_height" + str(new_height))
        if new_height == last_height:
            break
        last_height = new_height

        # print(str(driver))
        # link_loop = browser.page_source

    page_html = BeautifulSoup(driver.page_source, "html.parser")
    #print("page_html = {0}".format(page_html))
    mv_containers = page_html.find_all("div", class_="_u3y")
    #print("containers - {0}".format(mv_containers))

    for container in mv_containers:
        try:
            name = container.find('div', class_ = '_3v4h _48gm _50f3 _50f7')
            name = name.text
            #print(name)
            tmp.append(name)

        except:
            tmp.append("No Data")
            #print("No Names")

        try:
            video_link = container.find('a', href=True)
            video_link = video_link['href']
            video_link = "https://www.facebook.com"+str(video_link)
            #print(video_link)
            tmp1.append(video_link)

            #inputTag = soup.findAll(attrs={"name" : "stainfo"})
            #output = inputTag['value']
        except:
            tmp1.append("No Data")
            #print("No video_links")

        try:
            view = container.find('span', class_ = 'fcg')
            view = view.text.split(' ')[0]
            if (view[-1:] == 'K'):
                view = view[:-1]
                view = float(view)*1000
            elif (view[-1:] == 'M'):
                view = view[:-1]
                view = float(view)*1000000
            else:
                view = float(view)

            tmp2.append(view)

        except:
            tmp2.append("No Data")

        try:
            date = container.find('div', class_ = 'fsm fwn fcg')
            date = date.text
            #date = datetime.strptime('Jun 1 2005', '%b %d %Y')
            #date_month = datetime.month
            #print("date_month = "+date_month)
            tmp3.append(date.split('·')[1])
            #tmp3.append(date)

        except:
            tmp3.append("No Data")


        count = count + 1
    names += tmp
    video_links += tmp1
    views += tmp2
    dates += tmp3



driver.quit()


data_store = pd.DataFrame({ 'Video Name': names,
                            'Views': views,
                            'Video_Links': video_links,
                            'Upload Date': dates
                              })

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('facebook_videos.xlsx', engine='xlsxwriter')

# # Convert the dataframe to an XlsxWriter Excel object.
data_store.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
