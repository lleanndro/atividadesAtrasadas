from selenium_utils.utils import *
from selenium_utils.test_base import *
import pytest

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_DIR = Path(__file__).resolve().parent

#setup: sudo -H pip3 install -r requirements.txt&sudo -H apt-get install -y chromium-browser
#run: python -m pytest -q --num_exercicio="0.2" test.py

@pytest.mark.usefixtures("open_chrome")
class TestExampleOne:
    tests = [
            {
             "a":-6, "b":4, "c":4,
             "delta":112,
             "x1":-0.549,
             "x2":1.215,
             "raizes":2,
             "parabola":"baixo",
             "vertice":(0.3333,4.6667)
            },
            {
                "a":-6, "b":4, "c":-2,
                "delta": -32,
                "x1": None,
                "x2": None,
                "raizes": 0,
                "parabola": None,
                "vertice": (None, None)
            },
            {
                "a":6, "b":0, "c":0,
                "delta": 0,
                "x1": 0,
                "x2": 0,
                "raizes": 1,
                "parabola": "cima",
                "vertice": (0, 0)
            },
        ]

    def get_button(self):
        button = self.chrome.find_elements(By.CSS_SELECTOR, "#coeficientes-da-equacao button")
        assert 1 == len(button), "Não foi encontrado a tag button"

        return button
    def get_inputs(self):
        arr_inputs = self.chrome.find_elements(By.CSS_SELECTOR, "#coeficientes-da-equacao input[type='number']")
        assert 3 == len(arr_inputs), "Deve-se haver 3 inputs numéricos dentro do section de id coeficientes-da-equacao"
        return arr_inputs
     
    def test_exercicio1(self):
        arquivo = "index.html"
        url = f"file://{BASE_DIR}/{arquivo}"
        open_new_page(url, self.chrome)

        #há 3 inputs em #coeficientes-da-equacao?
        self.get_inputs()

        #criou um botao?
        self.get_button()
    
    def fill_inputs_test(self):
        button = self.get_button()


        coef_a, coef_b, coef_c = self.get_inputs()

        for input_and_exp_result in TestExampleOne.tests: 
            coef_a.clear()
            coef_b.clear()
            coef_c.clear()

            coef_a.send_keys(input_and_exp_result["a"])
            coef_b.send_keys(input_and_exp_result["b"])
            coef_c.send_keys(input_and_exp_result["c"])

            button.click()

            yield input_and_exp_result

    def test_exercicio3(self):

        for input_and_exp_result in self.fill_inputs_test():
            #checa resultado
            input_delta = self.chrome.find_elements(By.ID, "#resultado-delta")
            val_delta = input_delta.get_attribute('value')
            expected_delta = input_and_exp_result["delta"]
            assert int(val_delta) == expected_delta, f"Delta incorreto. Esperado:{expected_delta} calculado: {val_delta}"
    
    def test_exercicio4(self):

        for input_and_exp_result in self.fill_inputs_test():
            #checa resultado
            input_x1 = self.chrome.find_elements(By.ID, "#resultado-x1")
            input_x2 = self.chrome.find_elements(By.ID, "#resultado-x2")
            
            val_x1 = input_x1.get_attribute('value')
            val_x2 = input_x2.get_attribute('value')
            
            expected_x1 = input_and_exp_result["x1"]
            expected_x2 = input_and_exp_result["x2"]
            if expected_x1 is not None and expected_x2 is not None:
                assert round(int(val_x1)*100) == round(expected_x1*100), f"X1 incorreto. Esperado:{expected_x1} calculado: {val_x1}"
                assert round(int(val_x2)*100) == round(expected_x2*100), f"X2 incorreto. Esperado:{expected_x2} calculado: {val_x2}"
            else:
                assert expected_x1 is None, "x1 deve ser vazio"
                assert expected_x2 is None, "x2 deve ser vazio"
    
    def test_desafio1(self):
        button = self.get_button()


        coef_a, coef_b, coef_c = self.get_inputs()
        
        coef_a.clear()
        coef_a.send_keys("0")
        button.click()

        WebDriverWait(self.chrome, 10).until(EC.alert_is_present())
        self.chrome.switch_to.alert.accept()

    def test_desafio2(self):
        for input_and_exp_result in self.fill_inputs_test():
            #checa resultado
            input_qtd_raizes = self.chrome.find_elements(By.ID, "#qtd_raizes")
            input_concavidade_parabola = self.chrome.find_elements(By.ID, "#concavidade_parabola")
            input_pos_parabola = self.chrome.find_elements(By.ID, "#posicao_parabola")
            
            val_qtd_raizes = int(input_qtd_raizes.get_attribute('value'))
            val_concavidade_parabola = input_concavidade_parabola.get_attribute('value')
            val_pos_parabola = input_pos_parabola.get_attribute('value')

            assert int(val_qtd_raizes) == val_qtd_raizes, f"Raizes incorreto. Esperado:{val_qtd_raizes} calculado: {val_qtd_raizes}"

            if(val_qtd_raizes>0):
            expected_x1 = input_and_exp_result["x1"]
            expected_x2 = input_and_exp_result["x2"]
            if expected_x1 is not None and expected_x2 is not None:
                assert round(int(val_x1)*100) == round(expected_x1*100), f"Delta incorreto. Esperado:{expected_x1} calculado: {val_x1}"
                assert round(int(val_x2)*100) == round(expected_x2*100), f"Delta incorreto. Esperado:{expected_x2} calculado: {val_x2}"
            else:
                assert expected_x1 is None, "x1 deve ser vazio"
                assert expected_x2 is None, "x2 deve ser vazio"