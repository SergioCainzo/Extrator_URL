import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()


    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("URL Inválida")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("URL Inválida")


    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base


    def get_url_parametro(self):
        indice_interrogacao = self.url.find("?")
        url_parametro = self.url[indice_interrogacao + 1:]
        return url_parametro


    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) +1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
        return valor

    #Tamanho do Objeto
    def __len__(self):
        return len(self.url)

    #Print do Objeto
    def __str__(self):
        return f'URL: {self.url}\nParametros: {self.get_url_parametro()}\nURL BASE: {self.get_url_base()}'

    #Verificação de objetos iguais (URL)
    def __eq__(self, other):
        return self.url ==other.url

#extrator_url = ExtratorURL(None)
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')

print(f'Qual o valor da Quantidade: {valor_quantidade}')
print('')
print(f'Qual o tamanho da nossa URL: {len(extrator_url)} Caracteres')
print('')
print(extrator_url)
print('')
print(f'As URLs são iguais? {extrator_url == extrator_url2}')
print('')
#print(id(extrator_url))
#print(id(extrator_url2))

### DESAFIO ###
# Conversão de dólar para real
VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * VALOR_DOLAR
    print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")