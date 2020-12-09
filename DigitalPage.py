from selenium import webdriver
import smtplib
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\vtiwari02data\chromedriver.exe")

driver.implicitly_wait(2)
driver.maximize_window()

driver.get("http://ilrtvit688:25050/retail/retail-login/")

#driver.find_element_by_id('search-input').click()
driver.find_element_by_name('username').send_keys('posuser11')
driver.find_element_by_name('password').send_keys('Unix11!')
driver.implicitly_wait(4)
driver.find_element_by_xpath("/html/body/section/div/div[1]/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/form/div[2]/button").click()
driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div[2]/button").click()

driver.find_element_by_name('owningIndividual.firstName').send_keys('VFIT')
driver.find_element_by_name('owningIndividual.lastName').send_keys('VFIT')
driver.find_element_by_name('owningIndividual.nation').send_keys('Italia').click()

#select = Select(driver.find_element_by_name('owningIndividual.nation'))

# select by visible text

select.select_by_visible_text('Italia')

# select by value

select.select_by_value('Italia')


#driver.find_element_by_name('owningIndividual.nation').select_by_visible_text("Italia")
#menu.select_by_index(1)
#menu.select_by_visible_text("Italia")

#driver.find_element_by_class_name('class="ds-form__input ds-date react-datepicker-ignore-onclickoutside').send_keys('02/12/1995')
#driver.find_element_by_name('owningIndividual.fiscalCode').send_keys('VFTVFT95T42F205Y')
#driver.find_element_by_xpath('/html/body/section/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div[2]/fieldset/div[3]/div/div/button[2]').click()


sender = 'vtiwari@amdocs.com'
receivers = ['vtiwari@amdocs.com']

message = """From: From Person <vtiwari@amdocs.com>
To: To Person <vtiwari@adocs.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
print("maillllllll")

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")

#print("search box clicked")
#driver.findElement(By.name("SAMLResponse")).TAB();
#driver.findElement(By.name("SAMLResponse")).click();
#driver.findElement(By.name("SAMLResponse")).send_keys(Keys.TAB)
#driver.findElement(By.name("SAMLResponse")).sendKeys("abcdefghlkjl");





