endereco = "Rua das Flores 72, apartamento 1002, laranjeiras, Rio de Janeiro, RJ, 23440120"

#Importando Expressão Regular - REGEX
import re

#REGEX - 5 dígitos + hifen(opcional) +3 digitos
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #Match

if busca:
    cep = busca.group()
    print(cep)