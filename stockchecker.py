from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "xxx"
# Your Auth Token from twilio.com/console
auth_token  = "xxx"

client = Client(account_sid, auth_token)


# Loading webdrivers
options = Options()
# Path to your chrome profile
options.add_argument("user-data-dir=C:\\Users\\Boxca\\AppData\\Local\\Google\\Chrome\\profiletwo")
driver = webdriver.Chrome(r"C:\Users\Boxca\Downloads\Drivers\chromedriver_win32 (1)\chromedriver.exe",
options=options)


# Opening Website
driver.get('https://www.bestbuy.com/site/searchpage.jsp?st=rtx+3080&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys&irclickid=WUDxXJRLkxyOWeM0TbWK8Xs3UkiXpZRxI2oJxw0&irgwc=1&ref=198&loc=Future%20PLC.&acampID=0&mpid=221109&irclickid=UO-xLp2b7xyLR8M0EkzjZTwgUkEwzVwZ3TbFSU0&irgwc=1&ref=198&loc=Narrativ&acampID=0&mpid=376373')


while True:
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for post in soup.find_all('li', 'sku-item'):
        link = post.find('a', href=True)
        title = post.find('h4', 'sku-header')
        if "Add to Cart" in post.text:

            # print(post.text)
            print(title.text)
            print("https://www.bestbuy.com" + link['href'])
            message = client.messages.create(
                to="+16236808348",
                from_="+12566678863",
                body=f"We found a card in stock!\n\n{title.text}.\n\nhttps://www.bestbuy.com{link['href']}")
            print(message.sid)
            message = client.messages.create(
                to="+16023189499",
                from_="+12566678863",
                body=f"We found a card in stock!\n\n{title.text}.\n\nhttps://www.bestbuy.com{link['href']}")
            print(message.sid)
    time.sleep(60)
    driver.refresh()
