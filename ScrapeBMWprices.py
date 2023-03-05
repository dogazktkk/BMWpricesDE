from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import warnings
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)


def ScrapeBMWprices():
    options = Options()
    options.headless = False
    driver = uc.Chrome(use_subprocess=True, options=options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.bmw.de/de/home.html")

    # Scrolls the page down, else the tags are not seen by selenium (required)
    driver.execute_script("window.scrollBy(0, 1000);")

    # Clicks to "i" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[2]/button').click()
    time.sleep(0.5)

    i_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            i_serie_list.append(car_tag.text)

    # Clicks to "X" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[3]/button').click()
    time.sleep(0.5)

    x_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            x_serie_list.append(car_tag.text)

    # Clicks to "M" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[4]/button').click()
    time.sleep(0.5)

    m_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            m_serie_list.append(car_tag.text)

    # Clicks to "8er" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[5]/button').click()
    time.sleep(0.5)

    eight_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            eight_serie_list.append(car_tag.text)

    # Clicks to "7er" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[6]/button').click()
    time.sleep(0.5)

    seven_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            seven_serie_list.append(car_tag.text)

    # Clicks to "6er" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[7]/button').click()
    time.sleep(0.5)

    six_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            six_serie_list.append(car_tag.text)

    # Clicks to "5er" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[8]/button').click()
    time.sleep(0.5)

    five_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            five_serie_list.append(car_tag.text)

    # Clicks to "4er" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[9]/button').click()
    time.sleep(0.5)

    four_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            four_serie_list.append(car_tag.text)

    # Clicks to "3er" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[10]/button').click()
    time.sleep(0.5)

    three_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            three_serie_list.append(car_tag.text)

    # Clicks to "2er" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[11]/button').click()
    time.sleep(0.5)

    two_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            two_serie_list.append(car_tag.text)

    # Clicks to "1er" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[12]/button').click()
    time.sleep(0.5)

    one_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            one_serie_list.append(car_tag.text)

    # Clicks to "Z4" serie
    driver.find_element("xpath", '/html/body/div[1]/main/div[1]/div[7]/div[1]/div[2]/nav/div/ul/li[13]/button').click()
    time.sleep(0.5)

    z4_serie_list = []
    car_tags = driver.find_elements("class name", 'ds2-model-card--entry')
    for car_tag in car_tags:
        if car_tag.text != "":
            z4_serie_list.append(car_tag.text)

    return i_serie_list, x_serie_list, m_serie_list, eight_serie_list, seven_serie_list, six_serie_list, \
           five_serie_list, four_serie_list, three_serie_list, two_serie_list, one_serie_list, z4_serie_list