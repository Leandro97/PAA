numbers = []
res = 0

def test(begin, end, ratio):
  global res

  mid = int((begin + end) / 2)
  print("Mid: {}. Begin: {}. End: {}.".format(mid, begin, end))
  if(begin == end): return
  guess = numbers[0] + ratio * mid
  #print(guess)
  
  if(guess == numbers[mid]):
    res = numbers[mid] + ratio
    test(mid + 1, end, ratio)    
  else:
    res = numbers[mid] - ratio
    test(begin, mid, ratio)


n = int(input())

for i in range(n):
  qnt = int(input())
  numbers = list(map(int, input().split()))
  res = 0
  
  ratio = int((numbers[qnt - 1] - numbers[0])/qnt)
  test(0, qnt - 1, ratio)
  print(res)
  