def test(length, mid):
  aux = 0
  for i in range(length):
    #print(trees[i], trees[mid], trees[i] - trees[mid])
    if((trees[i] - trees[mid]) > 0):
      aux += trees[i] - trees[mid]
  return aux    

def findHeight(begin, end, length, needed):
  global height
  
  if(begin == end): return

  mid = int((begin + end) / 2)
  aux = test(length, mid)
  if(aux < needed):
    findHeight(begin, mid, length, needed)
  else:
    height = trees[mid]
    findHeight(mid + 1, end, length, needed)
  
  
inp = input()
line = inp.split()
n = int(line[0])
needed = int(line[1])
trees = list(map(int, input().split()))
trees.sort()
height = trees[0]

findHeight(0, n, n, needed)

print(height)