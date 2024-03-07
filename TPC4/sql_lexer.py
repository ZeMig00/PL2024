import sys
import ply.lex as lex


# List of token names.   This is always required
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'COMMA',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'VAR',
    'PV',
    'GT',
    'GTEQ',
    'LT',
    'LTEQ',
    'EQ',
    'EQEQ'
)

def SQLLexer():
    # Regular expression rules for simple tokens
    t_PLUS    = r'\+'
    t_COMMA    = r','
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_PV = r'\;'
    t_GT = r'\>'
    t_GTEQ = r'\>\='
    t_LT = r'\<'
    t_LTEQ = r'\<\='
    t_EQ = r'\='
    t_EQEQ = r'\=\='

    def t_SELECT(t):
        r'select'
        return t
    
    def t_FROM(t):
        r'from'
        return t
    
    def t_WHERE(t):
        r'where'
        return t
    
    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)    
        return t
    
    def t_VAR(t):
        r'[a-zA-Z]\w*'
        t.value = str(t.value)
        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer from my environment and return it    
    return lex.lex()


def main():
    lexer = SQLLexer()
    for line in sys.stdin:
        # case insensitive
        lexer.input(line.lower())
        for t in lexer:
            print(t)

if __name__ == "__main__":
    main()