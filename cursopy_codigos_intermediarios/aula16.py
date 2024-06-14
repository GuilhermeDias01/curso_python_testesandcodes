# Operações condicionais:
# if /    elif   /  else
# se / se não se / se não

entrada = input('Você deseja "entrar" ou "sair" do sistema? ')
entrada_upper = entrada.upper()

if entrada_upper == 'ENTRAR':
    print('Voce entrou no sistema')
elif entrada_upper == 'SAIR':
    print('Voce saiu do sistema')
else:
    print('Erro de digitação')

 