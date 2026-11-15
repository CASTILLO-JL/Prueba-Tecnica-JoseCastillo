#import pytest
from ..Globals.Globals_Functions import Globals_Functions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#En este archivo mandamos a llamar a nuestras funciones globales
#Este es el ejemplo completo de como realizar una prueba automatizada a la pagina https://www.saucedemo.com/.
#Este archivo es dependiente, o sea, sera llamado desde otro lugar para su ejecucion.
#Puntualmente sera llamado desde Test_Base_Page

class Base_Page():
    #Funcion de inicio
    def __init__(self, driver):
        self.driver = driver


    def correctEntry(self, username, clave, message, tg= 2):
        #Para ejecutar en navegador chrome
        driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        driver.maximize_window()
        #Llamamos nuestras funciones globales
        fg = Globals_Functions(driver)
        fg.navegar('https://www.saucedemo.com/', tg)
        #INICIANDO SESION
        fg.texto_Mixto('id','user-name', username, tg)
        fg.texto_Mixto('id','password', clave, tg)
        fg.click_Mixto('id', 'login-button', tg)
        successful = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="app_logo"]'))
        )
        # Pasamos el elemento
        successful = driver.find_element(By.XPATH, '//div[@class="app_logo"]')
        successful = successful.text
        if (successful == message):
            print('Prueba de inicio de sesion con datos correctos es EXITOSO')
        else:
            print('Prueba fallida')
        #AGREGANDO PRODUCTOS
        fg.click_Mixto('id', 'add-to-cart-sauce-labs-backpack', tg)
        fg.click_Mixto('id', 'add-to-cart-sauce-labs-bike-light', tg)
        #INGRESANDO AL CARRITO
        cart_icon = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon = cart_icon.click()
        #DANDO CLICK EN CHECKOUT
        fg.click_Mixto('id', 'checkout', tg)
        #LLENANDO FORMULARIO FINAL
        fg.texto_Mixto('id', 'first-name', 'JoseLuis', tg)
        fg.texto_Mixto('id', 'last-name', 'Castillo', tg)
        fg.texto_Mixto('id', 'postal-code', '11101', tg)
        fg.click_Mixto('id', 'continue', tg)
        #FINALIZANDO COMPRA
        fg.click_Mixto('id', 'finish', tg)
        finish = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        finish = driver.find_element(By.CLASS_NAME, "complete-header")
        finish = finish.text
        print(finish)
        if (finish == 'Thank you for your order!'):
            print('La compra se proceso correctamente')
        else:
            print('proceso fallido')






