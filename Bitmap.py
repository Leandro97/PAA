import math
res = []

def printMat():
  for j in range(len(res)): 
    if(j % 50 == 0): print("")
    print(res[j], end = '')

def dec(mat, bLinha, bCol, eLinha, eCol):
  if(bLinha >= eLinha or bCol >= eCol): return 0 
  primeiro = mat[bLinha][bCol]

  for lCount in range(bLinha, eLinha):
    for cCount in range(bCol, eCol):
      if(mat[lCount][cCount] != primeiro): 
        res.append("D")
        
        midL = math.ceil((bLinha + eLinha) / 2)
        midC = math.ceil((bCol + eCol) / 2)
        
        dec(mat, bLinha, bCol, int(midL), int(midC))
        dec(mat, bLinha, int(midC), int(midL), eCol)
        dec(mat, int(midL), bCol, eLinha, int(midC))
        dec(mat, int(midL), int(midC), eLinha, eCol)
        return 0
  res.append(primeiro)
  
n = int(input())
for i in range(n):
  inp = input()
  lc = inp.split(" ")
  linhas = int(lc[0])
  colunas = int(lc[1])
  mat = []
  
  for j in range(linhas):
    mat.append(input())
    
  dec(mat, 0, 0, linhas, colunas)  
  printMat()

  
  del res[::]  
