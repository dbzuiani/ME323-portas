from random import randint
import matplotlib.pyplot as plt

i = 0
cont_stroca = 0
cont_ctroca = 0
vetor_stroca = []
vetor_ctroca = []
eixo_x = []

vetor_stroca.append(0.5)
vetor_ctroca.append(0.5)
eixo_x.append(0)

while (i < 5000):
	porta_certa = randint(0,2)
	porta_escolha = randint(0,2)

	if (porta_escolha == porta_certa):
		cont_stroca = cont_stroca + 1

	i += 1
	vetor_stroca.append(cont_stroca/i)
	eixo_x.append(i)


i = 0	

while (i < 5000):
	porta_certa = randint(0,2)
	porta_escolha = randint(0,2)

	if (porta_escolha != porta_certa):
		cont_ctroca = cont_ctroca + 1

	i += 1
	vetor_ctroca.append(cont_ctroca/i)

print("Sem trocar de porta = " + str(cont_stroca))
print("Trocando de porta = " + str(cont_ctroca))

fig = plt.figure()

ax = fig.add_subplot(111)

ax.set_title('Proporção Acumulada - Porta dos desesperados')
plt.xlabel('Número de tentativas')
plt.ylabel('Porcentagem de sucesso')

ax.plot(eixo_x, vetor_stroca, color='r', label='Sem troca de porta')
ax.plot(eixo_x, vetor_ctroca, color='b', label='Com troca de porta')

ax.set_xlim(left=0)

leg = ax.legend()

plt.show()