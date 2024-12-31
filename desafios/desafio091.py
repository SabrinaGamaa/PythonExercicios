ranking = []
sorteios = {}

from random import randint
from operator import itemgetter

for d in range(1, 5):
    dados = randint(1, 6)
    sorteios[f"jogador{d}"] = dados


for k, v in sorteios.items():
    print(f'O {k} tirou {v} no dado')
ranking = sorted(sorteios.items(), key=itemgetter(1), reverse=True)
print('=' * 30)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
