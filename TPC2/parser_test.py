import unittest
from parser_markdown import *

class TestParser(unittest.TestCase):

    def test_rule_header_1(self):
        p = parser()
        k = p.rule_header("# abc\n# bca \n# asd\n")
        self.assertEqual(k, "<h1>abc</h1>\n<h1>bca </h1>\n<h1>asd</h1>\n")
    
    def test_rule_header_2(self):
        p = parser()
        k = p.rule_header("abc ## asd\n")
        self.assertEqual(k, "abc ## asd\n")
    
    def test_rule_header_3(self):
        p = parser()
        k = p.rule_header("abc \n## asd\n")
        self.assertEqual(k, "abc \n<h2>asd</h2>\n")

    def test_rule_bold_1(self):
        p = parser()
        k = p.rule_bold("dasd sa** aqui** asdas")
        self.assertEqual(k, "dasd sa<b> aqui</b> asdas")

    def test_rule_italico_1(self):
        p = parser()
        k = p.rule_italico("dasd sa* aqui* asdas")
        self.assertEqual(k, "dasd sa<i> aqui</i> asdas")

    def test_rule_lista(self):
        p = parser()
        k = p.rule_lista("1. elemento1\n2. elemento2\nasdsfa\n1. element11")
        self.assertEqual(k, '<ol>\n<li> elemento1</li>\n<li> elemento2</li>\n</ol>\nasdsfa\n<ol>\n<li> element11</li>\n</ol>')

    def test_rule_link(self):
        p = parser()
        k = p.rule_link("[página da UC](http://www.uc.pt)")
        self.assertEqual(k, '<a href="http://www.uc.pt">página da UC</a>')

    def test_rule_image(self):
        p = parser()
        k = p.rule_image("![imagem dum coelho](http://www.coellho.com)")
        self.assertEqual(k, '<img src="http://www.coellho.com" alt="imagem dum coelho"/>')

if __name__ == '__main__':
    unittest.main()