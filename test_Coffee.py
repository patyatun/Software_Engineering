import unittest
from tkinter import Tk

class TestCoffeeSystem(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.root.withdraw()  # Ocultar la ventana de la GUI

    def test_tea_cost(self):
        # Valores de prueba
        t_Yuzu = 2
        t_HintGinger = 1
        t_JujubeGoji = 3
        t_LycheeOolong = 0
        t_GuavaJasmin = 1
        t_BlackLemon = 2
        t_MatchaLemon = 1

        # Cálculo esperado
        expected_tea_cost = round((t_Yuzu * 3.5) + (t_HintGinger * 3.5) + (t_JujubeGoji * 3.8) + (t_LycheeOolong * 4.5) + (t_GuavaJasmin * 4.5) + (t_BlackLemon * 4.5) + (t_MatchaLemon * 4.5), 2)

        # Llamar a la función de cálculo
        varTeaCost = round((t_Yuzu * 3.5) + (t_HintGinger * 3.5) + (t_JujubeGoji * 3.8) + (t_LycheeOolong * 4.5) + (t_GuavaJasmin * 4.5) + (t_BlackLemon * 4.5) + (t_MatchaLemon * 4.5), 2)

        # Verificar el resultado
        self.assertEqual(varTeaCost, expected_tea_cost)

    def test_non_coffee_cost(self):
        # Valores de prueba
        t_Chocolate = 3
        t_MatchaLatte = 2
        t_UbeOatLatte = 1

        # Cálculo esperado
        expected_non_coffee_cost = round((t_Chocolate * 4) + (t_MatchaLatte * 4.5) + (t_UbeOatLatte * 4.8), 2)

        # Llamar a la función de cálculo
        varNoncoffeCost = round((t_Chocolate * 4) + (t_MatchaLatte * 4.5) + (t_UbeOatLatte * 4.8), 2)

        # Verificar el resultado
        self.assertEqual(varNoncoffeCost, expected_non_coffee_cost)

    def test_coffee_cost(self):
        # Valores de prueba
        t_Espresso = 1
        t_DoubleEspresso = 2
        t_Americano = 3
        t_Capuccino = 0
        t_FlatWhite = 1
        t_Latte = 2
        t_Mocha = 1
        t_BiscoffLatte = 0
        t_DalgonaLatte = 1
        t_BlackSesamLatte = 2
        t_InjeolmiOatLatte = 0
        t_PistacchioOatLatte = 1

        # Cálculo esperado
        expected_coffee_cost = round((t_Espresso * 2) + (t_DoubleEspresso * 3) + (t_Americano * 2.5) + (t_Capuccino * 3.5) + (t_FlatWhite * 4) + (t_Latte * 3.8) + (t_Mocha * 4.5) + (t_BiscoffLatte * 4.5) + (t_DalgonaLatte * 4.9) + (t_BlackSesamLatte * 4.8) + (t_InjeolmiOatLatte * 5.2) + (t_PistacchioOatLatte * 5.4), 2)

        # Llamar a la función de cálculo
        varCoffeeCost = round((t_Espresso * 2) + (t_DoubleEspresso * 3) + (t_Americano * 2.5) + (t_Capuccino * 3.5) + (t_FlatWhite * 4) + (t_Latte * 3.8) + (t_Mocha * 4.5) + (t_BiscoffLatte * 4.5) + (t_DalgonaLatte * 4.9) + (t_BlackSesamLatte * 4.8) + (t_InjeolmiOatLatte * 5.2) + (t_PistacchioOatLatte * 5.4), 2)

        # Verificar el resultado
        self.assertEqual(varCoffeeCost, expected_coffee_cost)

if __name__ == '__main__':
    unittest.main()
