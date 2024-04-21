def est_premier (n):
""" Teste la primalit é du nombre entier positif n"""
if n ==1: # test avec alternative
return False
10 elif n ==2: # autre alternative
return True
else : # sinon ...
for i in range (2 ,n):
if n%i ==0:
15 return False
return True
for n in range (1 ,1000):
if est_premier (n):
20 print (n)
12.a. Saisir ce programme d
