# Importē visas nepieciešamās bibliotēkas. Ja bibliotēkas nestrādā, tad ir jāizpild kods "pip install selenium".
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Nodefinē mainīgo driver, lai programma spētu kontrolēt pārlūkprogrammu Google Chrome.
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options = option)



# Tiek definēta web adrese, kur tiek meklēta informācija par filmas reģionu
url = "https://www.google.com/"

# Atver mājaslapu, uz kuru aizved adrese.
driver.get(url)
time.sleep(0.5)

# Noraida Google sīkfailus
decline_cookies = driver.find_element(By.ID, "W0wltc")
decline_cookies.click()
time.sleep(0.1)


