fazenda = list(map(int,input().split()))
mapa = []

for i in range(fazenda[0]):
    mapa.append(list(input()))

seguro = 'SIM'
for i in range(fazenda[0]):
    for e in range(fazenda[1]):
        if mapa[i][e] == 'O':
            if i < fazenda[0] - 1 and  mapa[i+1][e] == 'L' or \
            mapa[i - 1][e] == 'L' and i > 0 or \
            mapa[i][e + 1] == 'L' and e < fazenda[1] - 1 or \
            mapa[i][e-1] == 'L' and e > 0:
               seguro = 'NÃO' 
               break

print(seguro)