import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Globals_Functions():

    #Funcion de inicio (siempre debe ir)
    def __init__(self,driver):
        self.driver=driver

    #Funcion que retorna el tiempo
    def time(self,tie):
        t = time.sleep(tie)
        return t

    #Funcion navegar
    def navegar(self, url,tiempo):
        self.driver.get(url)
        #self.driver.maximize_window()
        print("Página abierta: "+str(url))
        t = time.sleep(tiempo)
        return t

    #Funcion mixta por xpath o id
    def texto_Mixto(self,tipo,selector,texto,tiempo):
        if(tipo=="xpath"):
            try:
                #Esperamos el elemento segun el tiempo indicado (En este caso 5 seg)
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                #Localizamos ese elemeto
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                #Pasamos el elemento
                val = self.driver.find_element(By.XPATH, selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector,texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif(tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t


    #Funcion click mixta por xpath o id
    def click_Mixto(self, tipo, selector,tiempo):
        if (tipo == "xpath"):
            try:
                #Esperamos el elemento segun el tiempo indicado (En este caso 5 seg)
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                #Localizamos el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                #Pasamos el elemento
                val = self.driver.find_element(By.XPATH, selector)
                val.click()
                print("dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                val.click()
                print("dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t


    def salida(self):
        print("Se termina la prueba exitosamente")