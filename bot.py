from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        """
        Logs into Instagram using the provided username and password.
        """
        self.driver.get('https://instagram.com')
        time.sleep(6)
        user_input = self.driver.find_element("xpath",'//input[@name="username"]')
        user_input.clear()
        user_input.send_keys(username)
        pass_input = self.driver.find_element("xpath",'//input[@name="password"]')
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element("xpath",'//button[@type="submit"]').click()
        time.sleep(5)
        self.driver.get('https://www.instagram.com/amyazdan__/')
        time.sleep(2)

    def quit(self):
        """
        Quits the WebDriver instance.
        """
        self.driver.quit()

    def make_list(self, list_xpath):
        """
        Creates a list of followers or following users.

        Args:
            list_xpath (str): The XPath of the list element on the Instagram profile page.

        Returns:
            list: A list of followers or following users.
        """
        self.driver.get('https://www.instagram.com/USER_NAME/')
        time.sleep(4)
        self.driver.find_element("xpath", list_xpath).click()
        time.sleep(7)
        win = self.driver.find_element("xpath",'//div[@class="_aano"]')
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", win)
        while True:
            self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", win)
            time.sleep(3)
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", win)
            if new_height == last_height:
                break
            last_height = new_height
        follower_list_link = self.driver.find_elements("tag name", 'a')
        my_list = [i.get_attribute('title') for i in follower_list_link if '' != i.get_attribute('title')]
        print(follower_list_link)
        return my_list

    def unfollow_list(self):
        """
        Finds the users who unfollowed you by comparing the followers and following lists.

        Writes the unfollowed users to a text file named 'listeTangha.txt'.
        """
        f = open('listeTangha.txt', 'w')
        follow_list = InstaBot.make_list(self, '//a[@href="/USER_NAME/followers/"]')
        following_list = InstaBot.make_list(self, '//a[@href="/USER_NAME/following/"]')
        unfollow_list = []
        for i in following_list:
            is_followed = False
            for j in follow_list:
                if i == j:
                    is_followed = True
            if not is_followed:
                f.write(i + '\n')
                unfollow_list.append(i)
        f.flush()
        f.close()
        print(unfollow_list)

    def unfyab(self):
        """
        Prints the users who do not follow you back.
        """
        time.sleep(5)
        following_button = self.driver.find_element("xpath",'//a[@href="/USER_NAME/following/"]')
        following_button.click
