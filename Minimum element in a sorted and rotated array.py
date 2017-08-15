res = 0

def test(begin, end):
  global res
  mid = int((begin + end) / 2)
  
  if(begin == end):
    res = mid  
    return

  if(numbers[mid] > numbers[end]): 
    test(mid + 1, end)
  else:
    res = mid
    test(begin, mid)

n = int(input())

for i in range(n):
  qnt = int(input())
  numbers = list(map(int, input().split()))
  res = 0
  
  test(0, qnt - 1)
  print(numbers[res])