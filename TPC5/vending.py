import json, sys, re, os
from io import TextIOWrapper
from tabulate import tabulate
from itertools import islice

class Produtos:
    precos = {
        '1c'  : 0.01,
        '2c'  : 0.02,
        '5c'  : 0.05,
        '10c' : 0.10,
        '20c' : 0.20,
        '50c' : 0.50,
        '1e'  : 1.00,
        '2e'  : 2.00
    }

    def load_json_data(self, data):
        self.produtos_json = data
        self.produtos = []
        if len(self.produtos_json) == 0:
            self.headers = ["cod", "nome", "quant", "preco"]
            return
        
        self.headers = list(self.produtos_json[0].keys())
        for produto_raw in self.produtos_json:
            if list(produto_raw.keys()) != self.headers:
                raise Exception(f"Different fields in entry (expected: {self.headers()}, actual: {produto_raw.keys()})")
            self.produtos.append(produto_raw.values())

    def save(self):
        with open(self.nomeF, "w") as json_file:
            json.dump(self.produtos_json, json_file, indent=4)
        
    def load_json_file(self,nomeF):
        with open(nomeF, "r") as json_file:
            self.load_json_data(json.load(json_file))

    def __init__(self, nomeF):
        self.nomeF = nomeF
        if isinstance(nomeF, str):
            self.load_json_file(nomeF)
        else:
            self.load_json_data(nomeF)

    def __str__(self):
        return tabulate(self.produtos, headers=self.headers)

class Menu:
    @staticmethod
    def print(s):
        print(f"maq: {s}")

    @staticmethod
    def listar(p, _, s):
        Menu.print("\n" + str(p))
        return s

    @staticmethod
    def moeda(p, c, s):
        for m in re.findall(r"\b\d{1,2}[ce](?=[,.\s])", c):
            s = s + p.precos[m]
        return Menu.saldo(p, c, s)
    
    @staticmethod
    def troco(valor):
        moedas = []
        precos_sorted = sorted(Produtos.precos.items(), key=lambda item: item[1], reverse=True)
        for moeda, moeda_value in precos_sorted:
            while valor >= moeda_value:
                moedas.append(moeda)
                valor = round(valor - moeda_value, 2)
        return moedas
    
    @staticmethod
    def trocoStr(valor):
        trocos_str = []
        troco = Menu.troco(valor)
        precos_sorted = sorted(Produtos.precos.items(), key=lambda item: item[1], reverse=True)
        for moeda, _ in precos_sorted:
            if troco.count(moeda) > 0:
                trocos_str.append(f"{troco.count(moeda)}x {moeda}")
        
        if len(trocos_str) == 0:
            return "Nao tem troco"
        
        trocos_string = ", ".join(trocos_str[:-1])
        if len(trocos_str) > 1:
            trocos_string += " e " + trocos_str[-1]
        else:
            # If there's only one type of coin, just use the first element
            trocos_string = trocos_str[0]
    
        return trocos_string
    
    @staticmethod
    def selecionar(p, c, s):
        sel = re.findall(r"selecionar (.+)",c)[0]
        produto = next((d for d in p.produtos_json if d['cod'] == sel), None)
        if produto == None:
            raise Exception("Produto nao existe")
        
        if produto["quant"] <= 0:
            raise Exception("Produto nao disponivel")
        
        if produto["preco"] > s:
            Menu.print("Saldo insuficiente para satisfazer o seu pedido")
            Menu.print(f"{Menu.saldoStr(s)}; Pedido = {Menu.montanteStr(s)}")
            return s
        
        produto["quant"] -= 1

        # troco
        Menu.print(f"Pode retirar o produto dispensado \"{produto["nome"]}\"")
        return s - produto["preco"]

    @staticmethod
    def montanteStr(s):
        val = ""
        if int(s) != 0:
            val = f"{int(s)}e"
        if s % 1 != 0:
            val = val + f"{int(s % 1 * 100):02d}c"
        if val == "":
            val = "0e"
        return val

    @staticmethod
    def saldoStr(s):
        return f"Saldo = {Menu.montanteStr(s)}"

    @staticmethod
    def saldo(_, __, s):
        Menu.print(Menu.saldoStr(s))
        return s

    @staticmethod
    def sair(p, c, s):
        Menu.print(f"Pode retirar o troco: {Menu.trocoStr(s)}.")
        Menu.print(f"Ate a proxima")
        exit(0)
    
    @staticmethod
    def help(_, __, s):
        print("Comando invalido!")
        print("Comandos: ")
        for function, _ in islice(Menu.functions.items(), len(Menu.functions) - 1):
            print(f"\t{function}")
        return s

    functions = {
        r"listar" : listar,
        r"moeda( (\d{1,2})[c|e][,|.])+$": moeda,
        r"selecionar (.+)$": selecionar,
        r"saldo": saldo,
        r"sair": sair,
        r".*" : help
    }

    @staticmethod
    def parse():
        i = input(">> ")
        for function, method in Menu.functions.items():
            if re.search(function, i):
                return i, method
        raise Exception("Method not found")


def main(argv):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    saldo = 0
    while True:
        p = Produtos(os.path.join(script_dir,"produtos.json"))
        try:
            comando, method = Menu.parse()
            saldo = method(p, comando, saldo)
        except Exception as e:
            Menu.print(f"{str(e)}")
            Menu.saldo(None, None, saldo)
        p.save()

if __name__ == "__main__":
    main(sys.argv)
