from random import randint

projetoValor = []

for i in range(0, 127):
   projetoValor.append(randint(55.000, 150.000) * 1000) 
   i += 1



criterios = ['Ótimo(a)', 'Bom(b)', 'Regular(c)', 'Ruim(d)']

print('-=-' * 20)
print('{:^60}'.format('CRITÉRIOS'))
print('-=-' * 20)

for n in criterios:
       print('|', end="")
       print(n,end='')
print('|')



projetosOtimos = []    

for i in range(len(projetoValor)):
   
   if (projetoValor[i] <= 80000):
      projetosOtimos.append(projetoValor[i])

print('\n A quantidade de projetos considerados ótimo(A) é igual à: ', len(projetosOtimos), '\n')


print('-=-' * 20)

projetosRuins = []    

for i in range(len(projetoValor)):
   
   if (projetoValor[i] > 120000):
      projetosRuins.append(projetoValor[i])

print('\n A quantidade de projetos considerados ruim(D) é igual à: ', len(projetosRuins))


print('-=-' * 20)


projetosPorcentagem = []

for i in range(len(projetoValor)):
   
   if (projetoValor[i] > 100001):
      projetosPorcentagem.append(projetoValor[i])

porcentagem = len(projetosPorcentagem) * 100 / 127

print(f'\n A porcentagem de projetos que não foram considerados bons ou ótimos é de: {porcentagem:.0f}%')


print('-=-' * 20)


projetosMenor = []    

for i in range(len(projetoValor)):
   
   if (projetoValor[i] < 75000):
      projetosMenor.append(projetoValor[i])

print('\n A quantidade de projetos menores que 75.000 é de: ', len(projetosMenor))