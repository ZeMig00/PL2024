import unittest
from sql_lexer import SQLLexer, tokens

class Test_SQLLexer(unittest.TestCase):

    def setUp(self):
        self.lexer = SQLLexer()

    def verify_tokens(self, list_tokens, list_expected_tokens):
        for i,t in enumerate(list_tokens):
            self.assertEqual(t.type, list_expected_tokens[i])

    def test_SELECT_1(self):
        self.lexer.input("Select id, nome, salario From empregados Where salario >= 820".lower())
        self.verify_tokens(list(self.lexer), ["SELECT", "VAR", "COMMA", "VAR", "COMMA", "VAR", "FROM", "VAR", "WHERE", "VAR", "GTEQ", "NUMBER"])

    def test_SELECT_2(self):
        self.lexer.input("Select id, nome, salario From empregados Where salario >= 53 + 8".lower())
        self.verify_tokens(list(self.lexer), ["SELECT", "VAR", "COMMA", "VAR", "COMMA", "VAR", "FROM", "VAR", "WHERE", "VAR", "GTEQ", "NUMBER", "PLUS", "NUMBER"])

    def test_SELECT_3(self):
        self.lexer.input("Select * From empregados;".lower())
        self.verify_tokens(list(self.lexer), ["SELECT", "TIMES", "FROM", "VAR", "PV"])

    def test_SELECT_4(self):
        self.lexer.input("Select * From empregados where salario < (23 * 5 / (12+3));".lower())
        self.verify_tokens(list(self.lexer), ["SELECT", "TIMES", "FROM", "VAR", "WHERE", "VAR", "LT", "LPAREN", "NUMBER", "TIMES", "NUMBER", "DIVIDE", "LPAREN", "NUMBER", "PLUS", "NUMBER","RPAREN","RPAREN", "PV"])

if __name__ == "__main__":
    unittest.main()