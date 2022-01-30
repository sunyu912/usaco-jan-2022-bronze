def wins(a , b):
  wins = 0
  ties = 0
  for i in a:
    for j in b:
      if i > j:
        wins+=1
      if i == j:
        ties+=1
  wins/=16
  ties/=16
  if wins == 1:
    return True
  if ties == 1:
    return False
  return wins / (1 - ties) > .5

N = int(input())

for times in range(N):
  line = list(map(int, input().split()))
  a = line[0:4]
  b = line[4:]

  trans = False

  for i in range(1,11):
    if trans:
      break
    for j in range(1,11):
      if trans:
        break
      for k in range(1,11):
        if trans:
          break
        for h in range(1,11):
          if trans:
            break
          awins = 0
          bwins = 0
          cwins = 0
          c = [i,j,k,h]
          awins+=wins(a,b) + wins(a,c)
          bwins+=wins(b,a) + wins(b, c)
          cwins+=wins(c,a) + wins(c,b)
          if awins == bwins and awins == cwins:
            trans = True
  if trans:
    print("yes")
  else:
    print("no")

