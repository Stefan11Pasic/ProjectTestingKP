import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from page import KpPage


def TestiranjePretrage():
    """
    Test koraci:
    1. Navigacija na https://novi.kupujemprodajem.com/ stranicu
    2. Uneti ‘laptop’ u polje za pretragu
    3. Sortirati da ide od jeftinijeg
    4. Proveriti cenu prvog i drugog proizvoda
    5. Uraditi proveru da je prvi prikazani proizvod bio jeftiniji od drugog

    :return:
    """
    driver = webdriver.Chrome()

    # 1. Navigacija na https://novi.kupujemprodajem.com/ stranicu
    driver.get('https://novi.kupujemprodajem.com/')

    # 2. Uneti ‘laptop’ u polje za pretragu
    input2 = driver.find_element(By.XPATH, KpPage.input)
    input2.send_keys('laptop')
    time.sleep(3)

    driver.find_element(By.XPATH, KpPage.pretraga_dugme).click()

    # 3. Sortirati da ide od jeftinijeg
    time.sleep(3)
    driver.find_element(By.XPATH, KpPage.sortiraj).click()
    time.sleep(5)
    driver.find_element(By.XPATH, KpPage.jeftiniji).click()

    # 4. Proveriti cenu prvog i drugog proizvoda
    time.sleep(3)
    cena1 = driver.find_element(By.XPATH, KpPage.cena1)
    cena2 = driver.find_element(By.XPATH, KpPage.cena2)

    # 5. Uraditi proveru da je prvi prikazani proizvod bio jeftiniji od drugog
    cena1 = cena1.text.split(' ')[0]
    cena2 = cena2.text.split(' ')[0]

    assert int(cena1) <= int(cena2)

def Testiranjemenjacnice():
    """
    Test koraci:
    1. Navigacija na https://novi.kupujemprodajem.com/ stranicu
    2. Klik u polje menjacnice
    3. Unosimo broj 0 na vec generisani broj 100
    4. Provera tacnosti menjacnice

    :return:
    """

    driver = webdriver.Chrome()
    # 1. Navigacija na https://novi.kupujemprodajem.com/ stranicu
    driver.get('https://novi.kupujemprodajem.com/')

    # 2. Klik u polje menjacnice
    input = driver.find_element(By.XPATH, KpPage.euro)

    # 3. Unosimo broj 0 na vec generisani broj 100
    input.send_keys('0')
    time.sleep(1)
    # 4. Provera tacnosti menjacnice

    course = driver.find_element(By.XPATH, KpPage.course).text

    din = float(course) * 1000
    eur = int(driver.find_element(By.CLASS_NAME, KpPage.eur).text.replace('.', ''))
    assert din == eur
    time.sleep(2)

def TestiranjeFilteraZaCenu():
    """"
    Test koraci:
     1. Navigacija na https://novi.kupujemprodajem.com/ stranicu
     2. Uneti ‘monitor’ u polje za pretragu
     3. Klik na filter za cenu
     4. Uneti 5000 za donju vrednost
     5. Uneti 10000 za gornju vrednost
     6. Izvrsiti pretragu
     7. Provera da je cena prvog prikazanog proizvoda u opsegu filtera

     :return:
     """
    driver=webdriver.Chrome()
    # 1. Navigacija na https://novi.kupujemprodajem.com/ stranicu
    driver.get('https://novi.kupujemprodajem.com/')

    # 2.Uneti ‘monitor’ u polje za pretragu
    monitor=driver.find_element(By.XPATH,KpPage.monitor)
    monitor.send_keys('monitor')
    # 3. Klik na filter za cenu
    driver.find_element(By.XPATH, KpPage.pretraga_dugme).click()
    time.sleep(3)
    driver.find_element(By.XPATH,KpPage.filterZaCenu).click()
    time.sleep(3)

    #4. Uneti 5000 za donju vrednost
    input3 = driver.find_element(By.XPATH, KpPage.cenaod)
    input3.send_keys("5000")

    # 5. Uneti 10000 za gornju vrednost
    input3 = driver.find_element(By.XPATH, KpPage.cenado)
    input3.send_keys("10000")
    time.sleep(3)

    # 6. Izvrsiti pretragu
    driver.find_element(By.XPATH, KpPage.primenifiltere).click()
    time.sleep(5)

    #7. Provera da je cena prvog prikazanog proizvoda u opsegu filtera
    cenaprvog = driver.find_element(By.XPATH, KpPage.cenaprvog)
    cenaprvog = cenaprvog.text.split(' ')[0]
    cena = float(cenaprvog) *1000
    if 5000 < cena < 1000:
        print("Cena je izmedju 5000 i 10000")
    else:
        print("Cena nije izmedju 5000 i 10000")
        time.sleep(5)


def TestiranjeUlogovanja():
    """"
    Test koraci:
    # 1. Navigacija na https://novi.kupujemprodajem.com/ stranicu
    # 2.Klik na dugme za ulogovanje
    # 3. Provera da je prikazana opcija za login preko facebook naloga
    :return:
    """


    driver = webdriver.Chrome()
    # 1. Navigacija na https://novi.kupujemprodajem.com/ stranicu
    driver.get('https://novi.kupujemprodajem.com/')

    # 2.Klik na dugme za ulogovanje
    driver.find_element(By.XPATH, KpPage.ulogujse).click()
    time.sleep(5)

    # 3. Provera da je prikazana opcija za login preko facebook naloga
    driver.find_element(By.XPATH, KpPage.facebook)
def TestiranjeUsluge():
    """
    # 1. Navigacija na https: //novi.kupujemprodajem.com/ stranicu
      2. Klik na usluge na sredini stranice
      3. Provera da li je otvorena zeljena stranica
    :return:
    """
    driver = webdriver.Chrome()
    # 1. Navigacija na https: //novi.kupujemprodajem.com/ stranicu
    driver.get('https://novi.kupujemprodajem.com/')

    #2. Klik na usluge na sredini stranice
    usluge = driver.find_element(By.XPATH, KpPage.usluge).click()
    time.sleep(3)
    assert driver.find_element(By.XPATH, KpPage.usluge)

    #3. Provera da li je otvorena zeljena stranica

def Testiranjepovratkanapocetnustranicu():
    """
        # 1. Navigacija na https: //novi.kupujemprodajem.com/ stranicu
          2. Klik na usluge na sredini stranice
          3. Provera da li je otvorena zeljena stranica
          4. Klik na kupujem prodajem naslov
          5.Provera da li je ucitana pocetna stranica
          :return:
        """
    driver = webdriver.Chrome()
    # 1. Navigacija na https: //novi.kupujemprodajem.com/ stranicu
    driver.get('https://novi.kupujemprodajem.com/')
    usluge = driver.find_element(By.XPATH, KpPage.usluge).click()
    time.sleep(3)
    assert driver.find_element(By.XPATH, KpPage.usluge)
    kupujemprodajem = driver.find_element(By.XPATH, KpPage.kupujemprodajem).click()
    time.sleep(3)
    assert driver.find_element(By.XPATH, KpPage.kupujemprodajem)
TestiranjePretrage()


















