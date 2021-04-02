from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from time import sleep
from random import choice

def remove_tag(data):
	flag = True
	new_data = ''
	if '</div></div>' in data:
		data = data.replace('</div></div>', '\n')
	for i in data:
		if i == '<':
			flag = False
		if i == '>':
			flag = True
		if flag:
			new_data += i
	symbol = '< > = ,'
	for i in symbol.split(' '):
		if i in new_data:
			new_data = new_data.replace(i, '')
	return new_data

USER = 'dinhdong224@gmail.com'
PASS = 'nopass220$'
SCROLL_PAUSE_TIME = [10.5, 10, 11, 13, 15]
LOGIN_URL = 'https://www.facebook.com/login'
# DH_URL = 'https://www.facebook.com/duy.huynh.501'
# POST_URL = 'https://www.facebook.com/duy.huynh.501/posts/2698101366918044'
CLASS_NAME = '''oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw'''
with open('link_summary', 'r+') as f:
	body = f.read()
list_link = body.split ('\n')

# OPEN CHROME AND LOGIN
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block - CONFIG THE NOTIFICATION SETTINGS
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})
# LOGIN FB AND REDIRECT TO THE NEW SITE
web = Chrome(chrome_options=option)
web.get(LOGIN_URL)
mail = web.find_element_by_name("email")
mail.clear()
sleep(1)
mail.send_keys(USER)
sleep(2)
pwd = web.find_element_by_name("pass")
pwd.clear()
sleep(1)
pwd.send_keys(PASS)
sleep(2)
pwd.send_keys(Keys.RETURN)
sleep(4)

for POST_URL in list_link[93:]:

	web.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
	sleep(1)
	web.get(POST_URL)
	sleep(10)
	page_source = web.page_source
	
	# open new tab
	page_b = BeautifulSoup(page_source)
	time = page_b.findAll("b", {"class":"b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4"})
	content = page_b.findAll("span", {"class" : "d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m"})
	time = remove_tag(str(time[0]))
	content = remove_tag(str(content[0]))
	with open("post_test", "a+") as f:
		f.write (f'Post {list_link.index(POST_URL)}\n')
		f.write (f'Time: {time}\n')
		f.write (f'Content:\n{content}\n')

	# close the old tab
	web.find_element_by_tag_name('body').send_keys(Keys.COMMAND + '1')
	web.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
web.close()
