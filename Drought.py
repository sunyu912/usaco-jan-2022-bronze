T = int(input())

for times in range(T):
  N = int(input())
  nums = list(map(int, input().split()))

  low = 0
  high = 10e9

  for x in nums:
    high = min(high, x)

  answer = -1
  if N == 1:
    answer = 0
  elif N == 2:
    if nums[0] == nums[1]:
      answer = 0
  else:
    while low <= high:
      mid = (low + high) // 2
      temp = []
      temp.extend(nums)
      val = 0
      for x in range(N - 1):
        diff = min(temp[x] - mid, temp[x + 1] - mid)
        val+=(2 * diff) 
        temp[x]-=diff
        temp[x + 1]-=diff
      equals = True
      for x in range(N - 1):
        if temp[x] != mid:
          equals = False
          break
      if equals:
        if answer == -1:
          answer = val
        else:
          answer = min(val, answer)
        low = mid + 1
      else:
          high = mid - 1
  print(answer)

