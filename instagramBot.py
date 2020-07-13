
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

def instaLogin(username, pw):
    #driver = webdriver.Chrome()
    username = username
    driver.get("https://instagram.com")
    sleep(2)

    #Giriş yap
    driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(2)

    #Verification code girişi (manuel)
    code=input("Enter code >> ")
    driver.find_element_by_xpath("//input[@name=\"verificationCode\"]").send_keys(code)
    driver.find_element_by_xpath('//button[@type="button"]').click()
    sleep(4)

    #Not Now butonuna tıkla
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

def instaPorifle(profileName):
    driver.get("https://instagram.com/"+profileName+"")
    sleep(1)

def firstPic():
    sleep(1)
    pic = driver.find_element_by_class_name("_9AhH0")
    pic.click()   # clicks on the first picture
    sleep(1)

def likePic():
    sleep(2)

    #aa=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg/path").text()
    #print(aa)
    #button = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg").get_attribute("aria-label")
    #print(button)
    #ele = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg")
    #ele = driver.find_element_by_xpath("//button[normalize-space(@class)='wpO6b']/*[name()='svg']")


    likeAtr = driver.find_element_by_css_selector("span.fr66n > button > svg").get_attribute("aria-label")
    sleep(2)
    if likeAtr == "Like":
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
    sleep(1)


def nextPic(flag):
    if flag == 0:
        nex = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
        flag=1
    else:
        nex = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
    # finds the button which gives the next picture
    sleep(1)
    return nex
    #ccs=.FY9nT.\_8-yf5
    #ccs=fr66n

def continueLiking():
    flag = 0
    while(True):

        if flag == 0:
            next_el = nextPic(0)
            flag=1
        else:
            next_el = nextPic(1)

        # if next button is there then
        if next_el != False:
            print(next_el)
            # click the next button
            next_el.click()
            sleep(1)

            # like the picture
            likePic()
            sleep(1)
        else:
            print("not found")
            break
#/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg/path
#/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg/path

#/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg

#3Beğenmekten Vazgeç
#Beğen



instaLogin('onur_cete','xxx')
instaPorifle("deniz_bagci")
firstPic()
likePic()
continueLiking()
