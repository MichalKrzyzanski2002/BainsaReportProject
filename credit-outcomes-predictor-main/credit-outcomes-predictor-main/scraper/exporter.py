import os
import actions
from person import Person
from selenium import webdriver
#driver = webdriver.Chrome("./chromedriver")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
import json
import dill

    
def export_to_file (file_name,person):
    with open(file_name, 'wb') as file:
        dill.dump(person, file)
    print(f'Object successfully saved to "{file_name}"')

email =""
password = ""
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
cyril_account = Person("link", driver=driver) ## replace link with social media
print(cyril_account.company_urls)
print(cyril_account.companies)

export_to_file("cyril.dill",cyril_account)

