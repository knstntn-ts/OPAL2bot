from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
import time
import numpy as np

CHROME_DRIVER_PATH = "PATH TO DRIVER"
URL = "https://www2.pvlighthouse.com.au/calculators/opal%202/opal%202.aspx"

spectrum_file = 'C:/Users/Silvaco/Desktop/AM1_5G.csv'


class Opal2Bot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def load_page(self):
        self.driver.get(URL)
        time.sleep(5)

    def add_film(self):
        # add_film_btn = self.driver.find_element(By.ID, 'TabContainer1_TabPanelCalculator_AddFilm')
        add_film_btn = self.driver.find_element(By.XPATH,
                                                '/html/body/div/div[1]/form/div[3]/div[3]/div/div[1]/div[1]/div[5]/div[1]/table/tbody/tr[2]/td[6]/span/span[1]/input')
        add_film_btn.click()
        time.sleep(5)

    def load_data(self):
        load_data_btn = self.driver.find_element(By.ID, 'btnTab_5')
        load_data_btn.click()
        time.sleep(5)
        collapse_reflection = self.driver.find_element(By.ID, 'TabContainer1_TabPanelCustomData_btnCustomReflection')
        collapse_reflection.click()
        time.sleep(5)
        expend_spectrum = self.driver.find_element(By.ID, 'TabContainer1_TabPanelCustomData_btnCustomSpectrum')
        expend_spectrum.click()
        time.sleep(5)
        choose_btn = self.driver.find_element(By.ID, 'TabContainer1_TabPanelCustomData_SpectrumFileUpload')
        choose_btn.send_keys(spectrum_file)
        time.sleep(5)
        upload_button = self.driver.find_element(By.ID,
                                                 'TabContainer1_TabPanelCustomData_SpectrumFileUploadButton').click()

        time.sleep(5)

    def choose_film(self, film_number, film):
        select = Select(
            self.driver.find_element(By.ID, f'TabContainer1_TabPanelCalculator_ddlFilmMaterial{film_number}'))
        select.select_by_visible_text(film)
        time.sleep(5)

    def change_spec(self, film=2):
        select = Select(self.driver.find_element(By.ID, f'TabContainer1_TabPanelCalculator_ddlFilmSpecifics2'))
        select.select_by_visible_text('Undoped [Rao19]')
        time.sleep(5)

    def change_substrate(self):
        select = Select(self.driver.find_element(By.ID, f'TabContainer1_TabPanelCalculator_SubstrateMaterial'))
        # select by visible text
        select.select_by_visible_text('Perovskite')
        time.sleep(5)
        select = Select(self.driver.find_element(By.ID, f'TabContainer1_TabPanelCalculator_SubstrateSpecifics'))
        select.select_by_visible_text('CH3NH3PbI3 - nanocrystalline [Lop15]')

        time.sleep(5)

    def enter_thk(self, film_number, thk):
        film_thk = self.driver.find_element(By.ID, f'TabContainer1_TabPanelCalculator_t{film_number}')
        print(film_thk)
        film_thk.clear()
        film_thk.send_keys(thk)
        film_thk.send_keys(Keys.ENTER)
        time.sleep(5)

    def get_jph(self):
        jph_field = self.driver.find_element(By.ID, 'TabContainer1_TabPanelCalculator_JGOutput')
        jph_val = jph_field.text
        return float(jph_val)


ito_thk_list = np.linspace(1, 200, 200)
to_add = 3
films = ['ITO', 'SnO2']
jph_all = []
bot = Opal2Bot(CHROME_DRIVER_PATH)
bot.load_page()
bot.load_data()

print(jph_all)

