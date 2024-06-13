# Formatação de Strings

nome = 'Guilherme Dias'
altura = 1.85
peso = 110
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, pesa', 
      peso, 'Kilos e seu IMC é de', imc)

# F-strings = formatação ou Format
linha_1 = f'{nome} tem altura de {altura:.2f} pesa {peso} Kilos e seu IMC é de {imc:.2f}'

print(linha_1)