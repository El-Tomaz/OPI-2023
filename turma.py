

nest = int(input()) # nest : numero de estudantes

habpg = list(map(lambda item:int(item),input().split())) # habpg: habilidade dos alunos
habpg.sort()

print(habpg)
#usando two pointers
maxgp = 0
fp = 0 #first pointer
lp = 0 #last pointer
while lp < nest:                
    if habpg[lp] - habpg[fp] <= 5:  #a diferença entre dois alunos nao pode ultrapassar 5
        if lp - fp + 1>= maxgp:     #compara se o grupo atual é o maior
            maxgp = lp - fp +1
        lp+=1                       #move primeiro ponteiro para frente 
    else:
        fp+=1                       

print(maxgp)

"""exemplo de two pointers:
1 2 10 12 15
lp = 0,fp = 0

a diferença entre dois ponteiros + 1 é igual a o número de alunos entre eles

como 1 - 1 <=5,lp se move para frente
como 2 - 1 <=5, lp se move para frente
como 10 - 1 não é <= 5, fp se move para frente
como 2 - 10 não é <=5, fp se move para frente
como 10 - 10 <= 5, lp se move para frente ...


"""