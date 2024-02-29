import sys
import re

def main(imp):
    soma = 0
    somadorON = True 
    with open(imp[1], 'r') as f:
        for line in f:
            palavras = re.findall(r'[Oo][Ff]{2}|[Oo][Nn]|=|\d+', line)
            for pal in palavras:
                if re.fullmatch(r'[Oo][Nn]', pal):
                    somadorON = True
                elif re.fullmatch(r'[Oo][Ff]{2}', pal):
                    somadorON = False
                elif somadorON and re.fullmatch(r'\d+', pal):
                    soma += int(pal)
                elif re.fullmatch(r'=', pal):
                    print("A soma final é: ", soma)

if __name__ == '__main__':
    main(sys.argv)
