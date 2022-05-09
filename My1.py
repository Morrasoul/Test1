from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(
    executable_path="C:\\Users\\morra\PycharmProjects\\Test\\venv\\chromedriver\\chromedriver.exe")

driver.get('http://google.com/ncr')
searchbox = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('selenide')

time.sleep(1)

searchbutton = driver.find_element(By.XPATH,
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
searchbutton.click()
# Если я правильно понял, то тут еще можно было воспользоваться send.keys(Keys.RETURN)(имитация нажатия Enter)

time.sleep(2)

sitename = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a')
sitename_title = sitename.get_attribute('href')

if sitename_title == "https://selenide.org/":
    print("Первый результат – ссылка на сайт selenide.org.")
else:
    print("Что-то пошло не так")

searchimages = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
searchimages.click()

name = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]')
name_title = name.get_attribute('href')
if name_title == "https://ru.selenide.org/":
    print("Первое изображение неким образом связано с сайтом selenide.org")
else:
    print("Первое изображение не связано с сайтом selenide.org")

results = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[3]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
results.click()

time.sleep(1)

sitename2 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a')
sitename2_title = sitename2.get_attribute('href')

if sitename2_title == "https://selenide.org/":
    print("Первый результат такой же, как и в шаге 3")
else:
    print("Первый результат не ведет на сайт selenide.org")
da = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a')
da_title = da.get_attribute('href')
a = input("Показать ссылку на первый результат? Введите Да или Нет: ")
b = "Да"
c = "да"
if a == b or a == c:
    print(da_title)
else:
        print('Ну ладно :(')

driver.close()
driver.quit()