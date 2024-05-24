# lista de 15 nomes
nomes = ['alex', 'simone', 'bernardo', 'césar', 'alexandra', 'robert', 'ricardo', 'joana', 'carla', 'sueli', 'acacia', 'gabriela', 'paloma', 'paricia', 'fatima']

# usuário digita nome que deseja pesquisar
nome = input('Digite o nome para pesquisa: ').lower()

# retorna indice do nome pesquisado
indice = nomes.index(nome)

# verifica se o nome ta na lista ou não
if nome in nomes:
    print(f'Nome encontrado: {nome}, no indice {indice}.')
else:
    print(f'{nome} não encontrado na lista.')
