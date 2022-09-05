pessoas = dict()
galera = list()
media = 0

while True:
    pessoas.clear()  ## Dando clear nos dicionários.
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] '))
    while pessoas['sexo'] not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F. ')
        pessoas['sexo'] = str(input('Sexo: [M/F] '))
    pessoas['idade'] = int(input('Idade: '))
    media = media + pessoas['idade']
    galera.append(pessoas.copy()) ## Adicionando valores às listas.
    continuar = str(input('Quer continuar? [S/N] '))
    while continuar not in 'SsNn':
        print('ERRO! Responda apenas S ou N')
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = media / len(galera)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')