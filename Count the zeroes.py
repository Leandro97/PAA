res = 0

def test(begin, end):
  global res
  mid= int((begin + end) / 2)
  if(numbers[mid] == 0): res = mid
  
  if(begin == end): return  

  if(numbers[mid] == 1):
    test(mid + 1, end)
  else:
    res = mid
    test(begin , mid)
  
n = int(input())

for i in range(n):
  qnt = int(input())
  numbers = list(map(int, input().split()))
  res = qnt
  
  test(0, qnt - 1)
  print(qnt - res)
  