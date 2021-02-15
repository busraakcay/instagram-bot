from instaInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username,password):
        self.browser = webdriver.Chrome(executable_path="C:/Users/Busra/OneDrive/Masaüstü/Dosyalar/PythonT/chromedriver")
        self.username = username
        self.password = password
        self.followerList = []
        self.followingList = []
        self.unfollowersList = []
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        
        uInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        pInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        uInput.send_keys(self.username)
        pInput.send_keys(self.password)
        pInput.send_keys(Keys.ENTER)
        time.sleep(4)

    def getFollowers(self):
        url = "https://www.instagram.com/" + self.username
        self.browser.get(url)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(4)

        dialog = self.browser.find_element_by_xpath("/html/body/div[5]/div/div")
        followerCount = len(dialog.find_elements_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li"))
        print(f"first count: {followerCount}")
        self.action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            time.sleep(1)
            self.action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(5)
            dialog.click()
            time.sleep(1)
            self.action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(5)

            newCount = len(dialog.find_elements_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"updated count: {newCount}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li")


        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            self.followerList.append(link)

        with open("followers.txt", "w",encoding="UTF-8") as file:
            for item in self.followerList:
                file.write(item + "\n")

    def getFollowing(self):
        url = "https://www.instagram.com/" + self.username
        self.browser.get(url)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(4)

        dialog = self.browser.find_element_by_xpath('/html/body/div[5]/div/div')
        followingCount = len(dialog.find_elements_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li"))
        print(f"first count: {followingCount}")
        self.action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            time.sleep(1)
            self.action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(5)
            dialog.click()
            time.sleep(1)
            self.action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(5)

            newCount = len(dialog.find_elements_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li"))

            if followingCount != newCount:
                followingCount = newCount
                print(f"updated count: {newCount}")
                time.sleep(1)
            else:
                break

        followings = dialog.find_elements_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li")

        for user in followings:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            self.followingList.append(link)

        with open("followings.txt", "w",encoding="UTF-8") as file:
            for item in self.followingList:
                file.write(item + "\n")

    def unfollowers(self):
        if len(self.followingList) != 0 and len(self.followerList) != 0:
            for following in self.followingList:
                if following not in self.followerList:
                    self.unfollowersList.append(following)

        with open("unfollow.txt", "w",encoding="UTF-8") as file:
            for item in self.unfollowersList:
                file.write(item + "\n")
                  
insta = Instagram(username, password)
insta.signIn()
insta.getFollowers()
insta.getFollowing()
insta.unfollowers()