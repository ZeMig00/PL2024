import unittest
from vending import *
from io import StringIO

class Test_Produtos(unittest.TestCase):
    def setUp(self):
        self.json_data = [
            {
                "cod": "A1",
                "nome": "agua 0.5l",
                "quant": 8,
                "preco": 0.7
            },
            {
                "cod": "A2",
                "nome": "bolo",
                "quant": 5,
                "preco": 0.5
            }
        ]
    def test_PARSING_1(self):
        p = Produtos(self.json_data)
        self.assertEqual(str(p.produtos), "[dict_values(['A1', 'agua 0.5l', 8, 0.7]), dict_values(['A2', 'bolo', 5, 0.5])]")
    
    def test_TROCO_1(self):
        self.assertEqual(Menu.troco(2.5), ["2e", "50c"])
        self.assertEqual(Menu.trocoStr(2.5), "1x 2e e 1x 50c")
        self.assertEqual(Menu.trocoStr(0), "Nao tem troco")
        self.assertEqual(Menu.trocoStr(6), "3x 2e")
        self.assertEqual(Menu.trocoStr(3.5), "1x 2e, 1x 1e e 1x 50c")
        self.assertEqual(Menu.trocoStr(3.4), "1x 2e, 1x 1e e 2x 20c")
        
if __name__ == "__main__":
    unittest.main()