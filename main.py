from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

def start():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wb=webdriver.Chrome(r'./chromedriver.exe',options=options)
    #wd.implicitly_wait(10)
    wb.get(r'http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com')
    username=wb.find_element(By.ID,'phone')
    passwd=wb.find_element(By.ID,'pwd')
    #登录
    username.send_keys(input("请输入您的用户名"))  
    passwd.send_keys(input("请输入您的密码"))    
    wb.find_element(By.TAG_NAME,'button').click()
    #看课表
    print("登录中(5s).......\n")
    time.sleep(5)
    #wb.find_element(By.TAG_NAME,'iframe')
    url=wb.find_element(By.TAG_NAME,'iframe').get_attribute('src')
    wb.get(url)
    #///////
    #找到课程列表输出
    print("请稍后，正在获取课表(5S)......\n")
    time.sleep(5)
    course=wb.find_elements(By.TAG_NAME,'span')

    j=1
    for i  in range(1,len(course)-2):
        print(str(j)+'.'+course[i].text)
        j=j+1
    #找课程对应的url
    courseurllib=[]
    courseurl=wb.find_elements(By.CLASS_NAME,'color1')
    for k in courseurl:
        courseurllib.append(k.get_attribute('href'))

    #选择url进入课程，开始刷tm
    flag=int(input("请按照序号输入想要刷的课程序号"))
    gourl=courseurllib[flag-1]

    wb.get(gourl)
    wb.find_element(By.XPATH,'//a[@title="章节"]').click()
    time.sleep(2)
    wb.switch_to.frame('frame_content-zj')
    course_list=wb.find_elements(By.XPATH,'//span[@class="catalog_sbar"]')

    courlistmax=len(course_list)-1
    randomnum=random.randint(0,courlistmax)
    course_list[randomnum].click()
    loopnum = int(input("请输入要刷的次数:"))
    looptime = int(input("请输入间隔的时间(建议大于30s):"))
    print("正在刷，最小化浏览器窗口，去干点别的吧！\n")
    for q in range(0,loopnum):
        course_list[randomnum].click()
        time.sleep(looptime)
    '''
    wb.switch_to.default_content()
    #自动定位到学习界面的窗口
    for handle in wb.window_handles:
        wb.switch_to.window(handle)
        if '学生学习页面' in wb.title:
            break
    #开始刷自动找页面，自动刷
   
    time.sleep(3)
    autoselect=wb.find_elements(By.XPATH,'//span[@class="posCatalog_name"]')
    jx=autoselect
    loopnum=int(input("请输入要刷的次数:"))
    looptime=int(input("请输入间隔的时间(建议大于30s):"))

    for q in range(0,loopnum):
        courlistmax = len(autoselect) - 1
        randomnum = random.randint(1, courlistmax)
        autoselect[randomnum].click()
        autoselect=jx
        time.sleep(looptime)
    '''
    print("刷完啦！！！！\n")
    wb.quit()





if __name__=="__main__":
    print("------------------------------------------------------------------\n")
    print("         XXT FUCK !!!           用于某xxt  刷次数                   \n")
    print("                                                                  \n")
    print("            运行程序根据提示输入账号密码，输入完最小化浏览器               \n")
    print("                        等待完成就好                                \n")
    print("                                                                  \n")
    print("                                                                  \n")
    print("                     Power by   Qinghua                           \n")
    print("------------------------------------------------------------------\n")
    start()