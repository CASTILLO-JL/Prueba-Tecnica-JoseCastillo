#import pytest
from .Base_Page import Base_Page
from selenium import webdriver

#En este archivo hacemos uso de nuestras funciones de Base_Page
#En este ejemplo utilizamos pytest dentro de un entorno virtual y la pruba la ejecutamos con un comando por medio de la CLI.
#Abrir la consola, ubicarse dentro de la carpeta Moduls y ejecutar el comando py.test Test_Base_Page.py -s -v
def test_Base_Page():
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    #Hacemos uso de nuestras funciones de base_page
    bp = Base_Page(driver)
    bp.correctEntry('standard_user', 'secret_sauce', 'Swag Labs')







