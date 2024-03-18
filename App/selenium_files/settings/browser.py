from selenium import webdriver
import time
import pickle
import random
class Browser:
    
    # def __init__(self, path_driver:str):
    #     self.path_driver = path_driver
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        
    def change_url(self,url):
        if self.driver.current_url!=url:
            try:
                self.driver.get(url)
            except:
                return False
        return True
    def save_cookies(self,username):
        # try:
            pickle.dump(self.driver.get_cookies(),open(f'{username}.pkl','wb'))
        #     return True
        # except:
        #     return False
    def load_cookies(self,username):
        # print("load cookies")
        cookies = pickle.load(open(f'{username}.pkl','rb'))
        # print("this is true")
        # for item in cookies.split(';'):
        #     name,value = item.split('=', 1)
        #     name=name.replace(' ', '').replace('\r', '').replace('\n', '')
        #     value = value.replace(' ', '').replace('\r', '').replace('\n', '')
        #     cookie_dict={
        #             'name':name,
        #             'value':value,
        #             "domain": "",  # Google Chrome
        #             "expires": "",
        #             'path': '/',
        #             'httpOnly': False,
        #             'HostOnly': False,
        #             'Secure': False
        #         }
        # self.driver_.add_cookie(cookie_dict)
        
        lst=[]
        for cookie in cookies:
            lst.append(cookie)

            self.driver.add_cookie(cookie)
        # f= open("c2.txt","w")
        # for item in lst:
        #     f.write(str(item))
        # f.close()
        self.driver.refresh()
        time.sleep(5)
    def rem_cookies(self):
        self.driver.delete_all_cookies()
    def close(self):
        self.driver.close()
        self.driver.quit()
def write_in_element(text,element):
    for _char in text:
        element.send_keys(_char)
        # t= random.random()
        t= 0.04
        time.sleep(t)
        
        