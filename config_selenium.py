from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_name = "test"
password = "test"

driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
driver.get("http://testphp.vulnweb.com/login.php")

# element = driver.find_element_by_id('uname')
# element.send_keys(user_name)
# element = driver.find_element_by_id('password')
# element.send_keys(password)
# element.send_keys(Keys.RETURN)

# element.close
#  Le principal problème ici est que le site : http://testphp.vulnweb.com/login.php ne dispose pas d'id sur ces éléments interactifs. On ne peut donc pas les cibler pour réaliser des test spécifiques sur eux.