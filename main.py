##### IMPORT STATEMENTS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

##### CONSTATNS AND VARIABLES FOR HOLDING DATA
CHROME_DRIVER_PATH = "PATH TO DRIVER"
URL = "https://www2.pvlighthouse.com.au/calculators/opal%202/opal%202.aspx"
jph_all = []

#### Bot class
class OPAL2Bot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def load_page(self):
        self.driver.get(URL)
        time.sleep(5)

    ### Function for choosing the desired film
    def choose_film(self, film_number, film):
        select = Select(
            self.driver.find_element(By.ID, f'TabContainer1_TabPanelCalculator_ddlFilmMaterial{film_number}'))
        select.select_by_visible_text(film)
        time.sleep(5)

    ### Function for changing the substrate type and changing its source
    def change_substrate(self):
        select = Select(self.driver.find_element(By.ID, f'TabContainer1_TabPanelCalculator_SubstrateMaterial'))
        select.select_by_visible_text('Perovskite')
        time.sleep(5)
        select = Select(self.driver.find_element(By.ID, f'TabContainer1_TabPanelCalculator_SubstrateSpecifics'))
        select.select_by_visible_text('CH3NH3PbI3 - nanocrystalline [Lop15]')
        time.sleep(5)

    ### Function for entering thickness of the specific film
    def enter_thk(self, film_number, thk):
        film_thk = self.driver.find_element(By.ID, f'TabContainer1_TabPanelCalculator_t{film_number}')
        film_thk.clear()
        film_thk.send_keys(thk)
        film_thk.send_keys(Keys.ENTER)
        time.sleep(5)

    ### Function for getting the calculated value of Jph
    def get_jph(self):
        jph_field = self.driver.find_element(By.ID, 'TabContainer1_TabPanelCalculator_JGOutput')
        jph_val = jph_field.text
        return float(jph_val)


# Films of interested and their thicknesses
films = ['ITO', 'SnO2']
thicknesses = [10, 20]

# ---------------------- BOT SETUP --------------------#
bot = OPAL2Bot(CHROME_DRIVER_PATH)
bot.load_page()
bot.change_substrate()

# --- Go through the parameters and do the changes --- #
for i in range(len(films)):
    bot.choose_film(i + 1, films[i])
    bot.enter_thk(i + 1, thicknesses[i])

    jph = bot.get_jph()
    jph_all.append(jph)


# --- Saving data --- #
# If you wish to save data to csv file, uncomment these lines (and import numpy module)
# jph_out = np.array(jph_all)
# np.savetxt('FILEPATH', jph_out, delimiter=",")

# Print out collected data
print(jph_all)
