fim = 0
#funções
def testa(a, g):
  for j in range(1, len(a)):
    if(a[j] - a[j - 1] == g):
      g -= 1
    elif(a[j] - a[j - 1] > g):
      return False
  return True
  
def procura(alturas, menor, maior):
  global fim
  fim = 0
  guess = int((menor + maior) / 2)
  #print("Menor: {}. Maior: {}. Guess: {}.".format(menor, maior, guess))

  res = testa(alturas, guess)
  #print(res)
  
  
  if(res):
    fim = guess
    if(menor == maior): return
    procura(alturas, menor, guess)
  else:
    if(menor == maior): return
    procura(alturas, guess + 1, maior)
  
#main  
alturas = []
n = int(input())

for i in range(n):
  degraus = int(input())
  alturas = []
  alturas.append(0)
  alturas += list(map(int, input().split())) #importante (ler inteiros na memsa linha)6

  if (len(alturas) > 1):
    menor = int(alturas[1])
    maior = int(alturas[len(alturas) - 1])
    
    procura(alturas, menor, maior)
    
  else: fim = alturas[0]  
  print("Case {}: {}".format((i + 1), fim))
print("")  