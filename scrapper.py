import time as t
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/L879444/Downloads/chromedriver.exe')

#open the moddle main page
driver.get("https://moodle2.bgu.ac.il/moodle/local/mydashboard/")

#Find username and password voxes
id_box = driver.find_element_by_id('login_username')
pass_box = driver.find_element_by_id('login_password')

username = ''
password = ''
#Type into the boxes
id_box.send_keys(username)
pass_box.send_keys(password)

# Find login button
login_button = driver.find_element_by_xpath('//form[@id="login"]//div[3]')
# Click login
login_button.click()

#open the media gallery
driver.get("https://moodle2.bgu.ac.il/moodle/local/kalturamediagallery/index.php?courseid=37011")

#switch to frame wich contains the videos
driver.switch_to.frame("contentframe")

#scroll till the end of the videos
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    t.sleep(0.5)


class video:
    def __init__(self, groupNum, date, lecturer, source):
        self.groupNum = groupNum
        self.date = date
        self.lecturer = lecturer
        self.source = source

# creating list
listOfGroupNames = []

html_list = driver.find_element_by_id("gallery")
items = html_list.find_elements_by_tag_name("li")
for item in items:
    lecturerSeg = item.find_element_by_class_name("userLink")
    sourceSeg = item.find_element_by_class_name("item_link").get_attribute('href')

    text = item.text

    dateSeg = ""
    groupNumSeg = "-1"
    if "קב׳" in text:
        groupNumSeg = text.split("קב׳")[1]
        dateSeg = text.split("קב׳")[1].split("(")[1]
        dateSeg = dateSeg[:len(dateSeg)-1]
    # elif "קבוצה" in text:
    #     groupNumSeg = text.split("קבוצה")[1]
    #     dateSeg = text.split("קבוצה")
    #     # dateSeg = dateSeg[:len(dateSeg)-1]
    #
    #     listOfGroupNames.append( groupNumSeg[:3] )
    #     print(dateSeg)
    listOfGroupNames.append( video(str(groupNumSeg[:3]), str(dateSeg), str(lecturerSeg.get_attribute("innerHTML")), str(sourceSeg))  )
for obj in listOfGroupNames:
    print(obj.groupNum + ", " + obj.lecturer + ", " + obj.date + ", " + obj.source + "\n" )
