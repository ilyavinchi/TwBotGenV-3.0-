import pickle
from os import remove, system, listdir
from os.path import exists, abspath
from time import sleep, gmtime, strftime, time, timezone, altzone
from random import choice, randint
from json import dump, load, dumps, loads
from math import ceil

import clipboard
from uuid import uuid1
from requests import get
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from names import get_full_name
from telebot import TeleBot
from threading import Thread

# driver.delete_all_cookies()
# names.get_full_name(gender='female')

def jload(jload_path):
	if exists(jload_path):
		while True:
			try:
				with open(jload_path, "r") as f:
					return load(f) 
			except Exception as e:
				print(e)
				sleep(0.1)
				continue
	else:
		return
def jdump(jdump_path, what_dump):
	if exists(jdump_path.replace(jdump_path.split("/")[-1], "")):
		while True:
			try:
				with open(jdump_path, "w") as f:
					dump(what_dump, f)
				return True
			except:
				sleep(0.1)
				continue
	else:
		return
def pload(pload_path):
	if exists(pload_path):
		while True:
			try:
				with open(pload_path, "rb") as f:
					return pickle.load(f) 
			except:
				time.sleep(1)
				continue
	else:
		return
def pdump(pdump_path, what_dump):
	if exists(pdump_path.replace(pdump_path.split("/")[-1], "")):
		while True:
			try:
				with open(pdump_path, "wb") as f:
					pickle.dump(what_dump, f)     
				return True
			except:
				time.sleep(1)
				continue
	else:
			return

def changearrayval(changefile_path, change_key, change_val):
	if exists(changefile_path):
		while True:
			try:
				filearray = jload(changefile_path)
				filearray[change_key] = change_val
				jdump(changefile_path, filearray)
				break
			except:
				time.sleep(0.1)
				continue
	else:
		raise Exception('Файл не существует')
def removearrayval(changefile_path, remove_val):
	if exists(changefile_path):
		while True:
			try:
				filearray = jload(changefile_path)
				if type(filearray) is list:
					filearray.remove(remove_val)
				elif type(filearray) is dict:
					filearray.pop(remove_val)
				else:
					print('Неизвестный тип файла')
					return
				jdump(changefile_path, filearray)
				break
			except:
				sleep(0.1)
				continue
	else:
		raise Exception('Файл не существует')
def removefiles(*files_pathes):
	for x in files_pathes:
		remove(x)

ALPHABET = list('abcdefghijklmnopqrstuvwxyz')
OFFER_LINK = "http://wait3seconds.ga/"

MAX_FOLLOWING_THREADS = 0
POSTS_PER_DAY = 8
PAUSE_BETWEEN_POSTS = ceil(24 / POSTS_PER_DAY) * 3600

jdump("Loops/posting.json", ["Deloris Matthews", "Donna Wall"])
a = {}
a["Deloris Matthews"] = {"Timer": True, "Fmode": 0, "EndCount": 0}
a["Donna Wall"] = {"Timer": True, "Fmode": 0, "EndCount": 0}
jdump("Loops/following.json", a)

def diedthread():
	pass
COUNT_OF_FOLLOW_THREADS = 5
follow_threads = [Thread(target=diedthread) for c in range(COUNT_OF_FOLLOW_THREADS)]
PARSE_AT_A_TIME = 5
SEND_PARSING_TEXT = "(nude OR sex OR tits)"
PAUSE_BETWEEN_FOLLOWINGS = [60, 90]
MAX_FOLLOWING_PER_DAY = 300
follow_threads_active = False
bot = TeleBot('1107563794:AAHwpuyWE1JWF2ZLTfGp7pMnMmWX_ys8omw')
# bot.send_message(457184560, "Введи рекапчу\n" + "Login: " + enter[0] + "\nPassword: " + enter[1])

def cookie_creator():
	driver = driver_start_empty("https://twitter.com/login", False)
	input()
	pdump("Cookies/test.pkl", driver.get_cookies())
	driver.quit()
def test_account(t_name):
	driver = driver_start(t_name, False)
	print("READY")
	input()
	driver.quit()
def wait(dr, el_info, tries, wait_type):
	if wait_type == 1:
		for x in range(tries*10):
			try:
				elem = dr.find_element(By.XPATH, el_info)
				return elem
			except:
				sleep(0.1)
	elif wait_type == 2:
		for x in range(tries*10):
			try:
				elem = dr.find_elements(By.XPATH, el_info)
				return elem
			except:
				sleep(0.1)
	return False
def driver_start_empty(start_url, headless_mode = True):
	options = Options()
	headless = headless_mode
	if headless:
		options.add_argument('--headless')
		options.add_argument('--disable-gpu')
	options.add_argument("--disable-notifications")
	options.add_argument("--disable-extensions")
	driver = Chrome("chromedriver.exe", options = options)
	driver.set_window_size(1366, 768) if headless == True else driver.maximize_window() 
	driver.get(start_url)
	return driver
def driver_start(bot_name, headless_mode = True):
	options = Options()
	headless = headless_mode
	if headless:
		options.add_argument('--headless')
		options.add_argument('--disable-gpu')
	options.add_argument("--disable-notifications")
	options.add_argument("--disable-extensions")
	driver = Chrome("chromedriver.exe", options = options)
	driver.set_window_size(1366, 768) if headless == True else driver.maximize_window() 
	driver.get("https://twitter.com/login")
	for cookie in pickle.load(open("Cookies/" + bot_name + ".pkl", "rb")):
		if 'expiry' in cookie:
			del cookie['expiry']
			driver.add_cookie(cookie)
	driver.refresh()
	return driver

def balance():
	b = get('http://api.sms-reg.com/getBalance.php?apikey=8t0kjwxk118uih3peiw3c8rbb7e61g62')
	b = b.text
	json_b = loads(b)
	if int(json_b["balance"].split(".")[0]) > 4:
		return True
	else:
		return

def url_to_imgs():
	while True:
		letter_choice = choice(ALPHABET)
		driver = driver_start_empty("https://www.kindgirls.com/girls/?i=" + letter_choice, True)
		while True:
			sleep(1)
			models = wait(driver, '//div[@class="model_list"]', 10, 2)
			if len(models) > 0:
				random_model = randint(0, len(models)-1)
			else:
				continue
			models[random_model].click()
			alboms = wait(driver, '//div[@class="gal_list"]', 10, 2)
			if len(alboms) > 8:
				clipboard.copy(driver.current_url)
				return driver.current_url
			else:
				driver.get("https://www.kindgirls.com/girls/?i=" + letter_choice)
				continue
def url_shortener(bot_name):
	driver = driver_start_empty("https://is.gd/create.php")
	link_to_shorter = OFFER_LINK
	wait(driver, '//input[@class="urlbox"]', 10, 1).send_keys(link_to_shorter)
	wait(driver, "//div[@id='shorturllabel']/label", 10, 1).click()

	bot_name = bot_name.split(" ")[0] + bot_name.split(" ")[1]
	link_save = bot_name + '_' + str(uuid1()).replace("-", "")[:6]
	driver.find_element(By.XPATH , "//input[@class='shorturlbox']").send_keys(link_save)
	driver.find_element(By.XPATH, "//input[@id='logstats']").send_keys(Keys.SPACE)
	driver.find_element(By.XPATH , "//input[@class='submitbutton']").submit()
	link_save = wait(driver, '//input[@id="short_url"]', 10, 1).get_attribute("value")
	return link_save
def url_shortener_main(bot_name):
	driver = driver_start_empty("https://is.gd/create.php")
	link_to_shorter = OFFER_LINK
	wait(driver, '//input[@class="urlbox"]', 10, 1).send_keys(link_to_shorter)
	wait(driver, "//div[@id='shorturllabel']/label", 10, 1).click()

	bot_name = bot_name.split(" ")[0] + bot_name.split(" ")[1]
	link_save = bot_name
	driver.find_element(By.XPATH , "//input[@class='shorturlbox']").send_keys(link_save)
	driver.find_element(By.XPATH, "//input[@id='logstats']").send_keys(Keys.SPACE)
	driver.find_element(By.XPATH , "//input[@class='submitbutton']").submit()
	link_save = wait(driver, '//input[@id="short_url"]', 10, 1).get_attribute("value")
	return link_save
def autoposting(autoposting_bot_name):
	try:
		account_settings = jload("Settings/" + autoposting_bot_name + ".json")
		driver = driver_start(autoposting_bot_name, False)
		driver.get(account_settings["IMG URL"])
		alboms = wait(driver, '//div[@class="gal_list"]', 10, 2)
		alboms[account_settings["ALBOM ID"]].click()
		photos = wait(driver, '//div[@class="gal_list"]', 10, 2)
		photos[account_settings["PHOTO ID"]].click()
		URL = wait(driver, '//img', 10, 1).get_attribute("src")
		account_settings["PHOTO ID"] += 1
		if account_settings["PHOTO ID"] == len(photos):
			if (account_settings["ALBOM ID"] + 1) > len(alboms) - 1:
				account_settings["PHOTO ID"] = 0
				account_settings["ALBOM ID"] = 0
			else:
				account_settings["PHOTO ID"] = 0
				account_settings["ALBOM ID"] += 1
		jdump("Settings/" + autoposting_bot_name + ".json", account_settings)

		driver.get("https://twitter.com/home")	

		picture_req = get(URL)
		if picture_req.status_code == 200:
			with open("3.jpg", 'wb') as f:
				f.write(picture_req.content)

		system("nconvert -out jpeg -o %_.jpg -q 95 -rmeta -rexifthumb -noise uniform 0.1 3.jpg")
		wait(driver, '//input[@type="file"]', 10, 1).send_keys(abspath("3_.jpg"))

		with open("texts.txt", 'r', encoding="utf-8") as f:
			all_texts = f.read().split("\n\n")
		contents_from_file = all_texts[randint(0, len(all_texts) - 1)] + url_shortener(autoposting_bot_name)
		clipboard.copy(contents_from_file)
		wait(driver, '//div[@role="textbox"]', 10, 1).send_keys(Keys.CONTROL, 'v')

		wait(driver, '//div[@data-testid="tweetButtonInline"]', 10, 1).click()
		sleep(5)
		changearrayval('Statistic/' + autoposting_bot_name + " stat.json", "Posts", "Next post: " + strftime("%X", gmtime(time() - timezone + PAUSE_BETWEEN_POSTS)))
		remove("3.jpg")
		remove("3_.jpg")
		driver.quit()
		return True
	except Exception as e:
		return
def delete_last_post(delete_last_post_name):
	driver = driver_start(delete_last_post_name, False)
	wait(driver, '//header[@role="banner"]//nav[@role="navigation"]/a[7]', 10, 1).click()
	wait(driver, '//div[@data-testid="primaryColumn"]//div[@data-testid="caret"]', 10, 1).click()
	wait(driver, '//div[@role="menu"]/div/div/div/div[1]', 10, 1).click()
	wait(driver, '//div[@data-testid="confirmationSheetConfirm"]', 10, 1).click()
	sleep(10)
	driver.quit()

def parsing(dr):
	driver = dr
	wait(driver, '//a[@data-testid="AppTabBar_Explore_Link"]/div', 10, 1).click()
	el = wait(driver, "//input[@data-testid='SearchBox_Search_Input']", 10, 1)
	el.click()
	el.send_keys(SEND_PARSING_TEXT)
	el.send_keys(Keys.ENTER)
	wait(driver, '//nav/div[@role="tablist"]/div[2]/a/div', 10, 1).click()
	driver.refresh()
	driver.refresh()
	for x in range(60):
		try:
			logins = wait(driver, '//div[@data-testid="tweet"]/div/div/div/div/div/div/a/div/div[2]', 10, 2)
			ready_logins = []
			for i in range(PARSE_AT_A_TIME):
				user_name = logins[i].text.replace("@", "")
				if user_name:
					ready_logins.append(user_name)
			return ready_logins
		except:
			sleep(1)
			continue
def autofollowing(autofollowing_bot_name, follow_mode = 0, last_count = 0):
	try:
		driver = driver_start(autofollowing_bot_name, True)
		count_of_followings = last_count
		count_of_unfollowings = last_count
		following_base = []
		following_save_base = jload("Sub_bases/" + autofollowing_bot_name + " base.json")
		mode = follow_mode
		if len(following_save_base) < 4500 and mode == 0:
			while count_of_followings < MAX_FOLLOWING_PER_DAY:
				if len(following_base) == 0:
					changearrayval("Statistic/" + autofollowing_bot_name + " stat.json", "Followings", "PARSING")
					following_base = parsing(driver)

				driver.get("https://twitter.com/" + following_base[0])
				if wait(driver, "//div[@data-testid='placementTracking']", 10, 1) and wait(driver, "//div[@data-testid='placementTracking']", 10, 1).text == "Follow":
					wait(driver, "//div[@data-testid='placementTracking']", 10, 1).click()
					if wait(driver, '//div[@role="alert"]', 3, 1):
						raise Exception('Аккаунт забанен')
					else:
						following_save_base = jload("Sub_bases/" + autofollowing_bot_name + " base.json")
						following_save_base.append(following_base[0])
						jdump("Sub_bases/" + autofollowing_bot_name + " base.json", following_save_base)
						count_of_followings += 1
						following_base.pop(0)
						changearrayval("Statistic/" + autofollowing_bot_name + " stat.json", "Followings", str(count_of_followings) + "/" + str(MAX_FOLLOWING_PER_DAY))
						if count_of_followings == MAX_FOLLOWING_PER_DAY:
							changearrayval("Statistic/" + autofollowing_bot_name + " stat.json", "Followings", "End Following Successful")
							return True, 0
						else:
							sleep(randint(PAUSE_BETWEEN_FOLLOWINGS[0], PAUSE_BETWEEN_FOLLOWINGS[1]))
				else:
					following_base.pop(0)
		else:
			mode = 1
			changearrayval("Statistic/" + autofollowing_bot_name + " stat.json", "Followings", "UNFOLLOWING")
			while count_of_unfollowings < 300:
				following_save_base = jload("Sub_bases/" + autofollowing_bot_name + " base.json")
				driver.get("https://twitter.com/" + following_save_base[0])
				if wait(driver, '//div[@data-testid="primaryColumn"]/div/div/div/div/div/div/div/div/div/div/div[2]', 10, 1):
					following_save_base.append(following_save_base.pop(0))
					jdump("Sub_bases/" + autofollowing_bot_name + " base.json", following_save_base)
				else:
					if wait(driver, "//div[@data-testid='placementTracking']", 10, 1):
						wait(driver, "//div[@data-testid='placementTracking']", 10, 1).click()
						if wait(driver, '//div[@role="alert"]', 3, 1):
							raise Exception('Аккаунт забанен')
						else:
							following_save_base.pop(0)
							jdump("Sub_bases/" + autofollowing_bot_name + " base.json", following_save_base)
							count_of_unfollowings += 1
					else:
						following_save_base.pop(0)
			mode = 0
			return True, 0
	except Exception as e:
		print(e)
		driver.quit()
		changearrayval("Statistic/" + autofollowing_bot_name + " stat.json", "Followings", "ERROR")
		if mode == 0:
			return False, mode, count_of_followings
		elif mode == 1:
				return False, mode, count_of_unfollowings

def phone_gen():
	phone_numb_search = get('http://api.sms-reg.com/getNum.php?country=ru&service=twitter&apikey=8t0kjwxk118uih3peiw3c8rbb7e61g62')
	phone_numb_search = phone_numb_search.text
	json_phone_numb_search = loads(phone_numb_search)
	phone_search_tzid = json_phone_numb_search['tzid']
	for x in range(900):
		phone_numb_info = get('http://api.sms-reg.com/getState.php?tzid=' + phone_search_tzid + '&apikey=8t0kjwxk118uih3peiw3c8rbb7e61g62')
		phone_numb_info = phone_numb_info.text
		json_phone_numb_info = loads(phone_numb_info)
		if json_phone_numb_info['response'] == 'WARNING_NO_NUMS':
			return
		elif json_phone_numb_info['response'] == 'TZ_INPOOL':
			sleep(1)
		elif json_phone_numb_info['response'] == 'TZ_NUM_PREPARE':
			return "+" + json_phone_numb_info['number'], phone_search_tzid

	return
def sms_get(p_tzid):
	sms_ready = get('http://api.sms-reg.com/setReady.php?tzid=' + p_tzid + '&apikey=8t0kjwxk118uih3peiw3c8rbb7e61g62')
	for x in range(650):
		sms_info = get('http://api.sms-reg.com/getState.php?tzid=' + p_tzid + '&apikey=8t0kjwxk118uih3peiw3c8rbb7e61g62')
		sms_info = sms_info.text
		json_sms_info = loads(sms_info)
		if json_sms_info['response'] == 'TZ_NUM_ANSWER':
			return json_sms_info['msg']
		elif json_sms_info['response'] == "TZ_OVER_EMPTY" or json_sms_info['response'] == "TZ_DELETED":
			return 
		else:
			sleep(1)

	return 
def newaccount():
	try:
		# Получение телефона
		print("TRY GET PHONE")
		phone, tzid = phone_gen()
		# phone, tzid = "+380687900282", "000000"
		if phone:
			print(phone)
			driver = driver_start_empty("https://twitter.com/i/flow/signup", False)
			name = get_full_name(gender='female')
			wait(driver, "//input[@type='text']", 60, 1).send_keys(name)
			wait(driver, "//input[@type='tel']", 60, 1).send_keys(phone)

			if wait(driver, "//div[@role='group']/div/div/div[1]/div/select/option[@value='" + str(randint(1,12))+"']", 2, 1):
				wait(driver, "//div[@role='group']/div/div/div[1]/div/select/option[@value='" + str(randint(1,12))+"']", 10, 1).click()
				wait(driver, "//div[@role='group']/div/div/div[2]/div/select/option[@value='" + str(randint(1,28))+"']", 10, 1).click()
				wait(driver, "//div[@role='group']/div/div/div[3]/div/select/option[@value='" + str(randint(1996,2001))+"']", 10, 1).click()

			while not wait(driver, "//div[@data-testid='confirmationSheetConfirm']", 1, 1):
				wait(driver, '//div[@aria-labelledby="modal-header"]/*//div[@role="button"]/div/span/span', 1, 1).click()
			wait(driver, "//div[@data-testid='confirmationSheetConfirm']", 1, 1).click()
			print("TRY GET CODE")
			code = sms_get(tzid)
			if not code:
				raise Exception("Код не пришел")
			wait(driver, "//input[@name='verfication_code']", 10, 1).send_keys(code)
			wait(driver, "//div/div/div/div[@role='button']/div/span/span", 10, 1).click()
			password = str(uuid1()).replace("-", "")[:8]
			print(password)
			wait(driver, "//input[@name='password']", 10, 1).send_keys(password)
			while wait(driver, "//div/div/div/div[@role='button']/div/span/span", 1, 1):
				wait(driver, "//div/div/div/div[@role='button']/div/span/span", 1, 1).click()
			driver.get("https://twitter.com/home")
			pdump("Cookies/"+name+".pkl", driver.get_cookies())
			driver.get("https://twitter.com/settings/screen_name")
			split_name = name.split(" ")
			try_combinations = [split_name[0] + split_name[1], split_name[1] + split_name[0], split_name[1] +"_"+ split_name[0], split_name[0] +"_"+ split_name[1], split_name[1] + split_name[0] + "_", split_name[0] + split_name[1] + "_", split_name[0] + "_" + split_name[1] + "_", split_name[1] + "_" + split_name[0] + "_"]
			login = None
			for x in range(8):
				if driver.current_url == "https://twitter.com/settings/screen_name":
					while wait(driver, "//input", 10, 1).get_attribute("value") != "":
						wait(driver, "//input", 10, 1).send_keys(Keys.BACK_SPACE)
					wait(driver, "//input", 10, 1).send_keys(try_combinations[x])
					wait(driver, '//div[@data-testid="settingsDetailSave"]', 10, 1).click()
					login = try_combinations[x]
					sleep(2)
				else:
					break

			try:
				login = wait(driver, "//div[@role='tablist']/div/h2", 10, 1).text
			except Exception as e:
				pass
			
			print(login)
			driver.get("https://twitter.com/settings/language")
			if wait(driver, "//option[@value='en']", 10, 1):
				wait(driver, "//option[@value='en']", 10, 1).click()
				wait(driver, "//div/div/div/span/span", 10, 1).click()
			driver.get("https://twitter.com/settings/country")
			if wait(driver, "//option[@value='us']", 10, 1):
				wait(driver, "//option[@value='us']", 10, 1).click()
				wait(driver, "//div[@aria-haspopup='false'][1]", 10, 1).click()

			imgs_url = url_to_imgs()
			driver.get(imgs_url)
			wait(driver, '//div[@class="gal_list"]', 10, 2)[0].click()
			wait(driver, '//div[@class="gal_list"]', 10, 2)[0].click()
			picture_req = get(wait(driver, '//img', 10, 1).get_attribute("src"))
			if picture_req.status_code == 200:
				with open("2.jpg", 'wb') as f:
					f.write(picture_req.content)
			system("nconvert -out jpeg -o %_.jpg -q 95 -rmeta -rexifthumb -noise uniform 0.1 *.jpg")

			driver.get("https://twitter.com/settings/profile")
			wait(driver, "//div[1]/div[1]/div/div/div/input[@type='file']", 10, 1).send_keys(abspath("1_.jpg"))
			wait(driver, "//div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/span/span", 10, 1).click()
			wait(driver, "//div[1]/div[2]/div/div/div/input[@type='file']", 10, 1).send_keys(abspath("2_.jpg"))
			wait(driver, "//div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/span/span", 10, 1).click()
			offer_url = url_shortener_main(name)
			wait(driver, "//textarea[@name='description']", 10, 1).send_keys("Register and find me here - " + offer_url)
			wait(driver, "//input[@name='url']", 10, 1).send_keys(offer_url)
			wait(driver, "//div[1]/div/div/div/div/div/div/div/div/div/div/div/div/span/span", 10, 1).click()
			sleep(5)
			remove("1_.jpg")
			remove("2_.jpg")
			remove("2.jpg")
			driver.get("https://twitter.com/home")
			get('http://api.sms-reg.com/setOperationOk.php?tzid=' + tzid + '&apikey=8t0kjwxk118uih3peiw3c8rbb7e61g62')
			account_settings = {}
			account_settings["Bot name"] = name
			account_settings["Login"] = login
			account_settings["Password"] = password
			account_settings["TZID"] = tzid
			account_settings["IMG URL"] = imgs_url
			account_settings["ALBOM ID"] = 0
			account_settings["PHOTO ID"] = 1
			jdump("Settings/"+name+".json", account_settings)
			stat = {}
			stat["Followings"] = "OFF"
			stat["Posts"] = "OFF"
			jdump("Statistic/"+name+" stat.json", stat)
			jdump("Sub_bases/"+name+" base.json", [])
			balance_info = get('http://api.sms-reg.com/getBalance.php?apikey=8t0kjwxk118uih3peiw3c8rbb7e61g62')
			balance_info = balance_info.text
			json_balance_info = loads(balance_info)
			bot.send_message(457184560, "Ваш балланс: " + json_balance_info['balance'])			
			driver.quit()
			return name
	except Exception as e:
		print(e)
		return False

def access(access_name):
	if balance():
		print("Access START")
		driver = driver_start(access_name, False)
		sleep(5)
		settings = jload("Settings/" + access_name + ".json")
		tzid = settings["TZID"]
		bot.send_message(457184560, "Введи рекапчу\n" + "Login: " + settings["Login"] + "\nPassword: " + settings["Password"] + "\n URL: https://twitter.com/")
		for x in range(900):
			if wait(driver, "//input[@id='code']", 1, 2):
				break
			else:
				driver.refresh()
				sleep(5)
				continue

			bot.send_message(457184560, "Время ввышло")
			driver.quit()
			return True
		for n in range(300):
			if n % 60 == 0:
				driver.get("https://twitter.com/account/access?did_not_receive=true")
				wait(driver, '//input[@type="submit"]', 10, 1).click()
				sleep(2)
			enter_info = get('http://api.sms-reg.com/getNumRepeat.php?tzid=' + tzid + '&apikey=8t0kjwxk118uih3peiw3c8rbb7e61g62')
			enter_info = enter_info.text
			json_enter_info = loads(enter_info)
			print(int(json_enter_info['response']))
			if int(json_enter_info['response']) == 0:
				driver.quit()
				return
			elif int(json_enter_info['response']) == 1:
				code = sms_get(json_enter_info['tzid'])
				if code:
					wait(driver, "//input[@id='code']", 10, 1).send_keys(code)
					get('http://api.sms-reg.com/setOperationOk.php?tzid=' + json_enter_info['tzid'] + '&apikey=8t0kjwxk118uih3peiw3c8rbb7e61g62')
					wait(driver, "//input[@type='submit']", 10, 1).click()
					sleep(5)
					driver.get("https://twitter.com/home")
					wait(driver, "//input[@type='submit']", 10, 1).click()
					sleep(5)
					driver.quit()
					return True
				else:
					return
			elif int(json_enter_info['response']) == 2:
				driver.quit()
				return
			elif int(json_enter_info['response']) == 3:
				sleep(1)
		driver.quit()
		return
	else:
		return True
def ban_test(ban_name):
	driver = driver_start(ban_name, False)
	sleep(10)
	if driver.current_url == "https://twitter.com/account/access":
		access_res = access(ban_name)
		if not access_res:
			try:
				removearrayval("Loops/posting.json", ban_name)
				removearrayval("Loops/following.json", ban_name)
				settings = jload("Settings/" + ban_name + ".json")
				s_m = "Account banned"
				for x in settings:
					s_m = s_m + '\n' + str(x) + ": " + str(settings[x])
				bot.send_message(457184560, s_m)
				removefiles("Cookies/" + ban_name + ".pkl", "Settings/" + ban_name + ".json", "Statistic/" + ban_name + " stat.json", "Sub_bases/" + ban_name + " base.json")
			except:
				pass
			return
	else:
		driver.get("https://twitter.com/messages")
		if wait(driver, '//div[@role="alert"]', 10, 1):
			try:
				removearrayval("Loops/posting.json", ban_name)
				removearrayval("Loops/following.json", ban_name)
				settings = jload("Settings/" + ban_name + ".json")
				s_m = "Account banned"
				for x in settings:
					s_m = s_m + '\n' + str(x) + ": " + str(settings[x])
				bot.send_message(457184560, s_m)
				removefiles("Cookies/" + ban_name + ".pkl", "Settings/" + ban_name + ".json", "Statistic/" + ban_name + " stat.json", "Sub_bases/" + ban_name + " base.json")
			except:
				pass
			return

	driver.quit()
	return True

def autoposting_loop():
	while True:
		posting_names = jload("Loops/posting.json")
		for x in posting_names:
			print("START NEW AUTOPOSTING")
			if not autoposting(x):
				Thread(target=ban_test, args=(x,)).start()

		print("PAUSE_BETWEEN_POSTS:", PAUSE_BETWEEN_POSTS)
		sleep(PAUSE_BETWEEN_POSTS)

def diebalance():
	while not balance():
		sleep(3600)
def autofollowing_tester(autofollowing_tester_name):
	following_setting = jload("Loops/following.json")[autofollowing_tester_name]
	res = autofollowing(autofollowing_tester_name, following_setting["Fmode"], following_setting["EndCount"])
	if res[0]:
		following_setting["Timer"] = time() + 86400
		following_setting["Fmode"] = 0
		following_setting["EndCount"] = 0
		changearrayval('Loops/following.json', autofollowing_tester_name, following_setting)
	else:
		if ban_test(autofollowing_tester_name):
			following_setting["Timer"] = True
			following_setting["Fmode"] = res[1]
			following_setting["EndCount"] = res[2]
			changearrayval('Loops/following.json', autofollowing_tester_name, following_setting)
def autofollowing_loop():
	while True:
		print("START")
		for x in range(len(follow_threads)):
			if not follow_threads[x].is_alive():
				print("NEW START AUTOFOLLOWING")
				followings_list = jload("Loops/following.json")
				start_name = None
				for z in followings_list:
					if followings_list[z]["Timer"] and followings_list[z]["Timer"] < time():
						start_name = z
						followings_list[z]["Timer"] = False
						jdump("Loops/following.json", followings_list)
						break
				if start_name:
					follow_threads[x] = Thread(target=autofollowing_tester, args=(start_name,))
					follow_threads[x].start()
					sleep(30)
				else:
					if balance():
						while not start_name:
							start_name = newaccount()
						followings_list[start_name] = {"Timer": False, "Fmode": 0, "EndCount": 0}
						jdump("Loops/following.json", followings_list)
						follow_threads[x] = Thread(target=autofollowing_tester, arg=(start_name,))
						follow_threads[x].start()
						sleep(30)
					else:
						bot.send_message(457184560, "Пополните счет sms-reg")
						diebalance()
						follow_threads[x] = Thread(target=diebalance)
						follow_threads[x].start()
		print("PAUSE")
		sleep(30)

def statistic_bot():
	print("STAT START")
	@bot.message_handler(content_types=['text'])
	def send_text(message):
		if message.text.lower() == "stat":
			accounts_set_list = listdir("Statistic/")
			for x in accounts_set_list:
				accounts_set = jload("Statistic/" + x)
				print()
				bot.send_message(message.chat.id, "Bot name: " + x.replace(" stat.json", "") + "\nFollowings: " + str(accounts_set["Followings"]) + "\nPosts: " + str(accounts_set["Posts"]))
	bot.polling()

Thread(target=autoposting_loop).start()
Thread(target=autofollowing_loop).start()
Thread(target=statistic_bot).start()