def positive(num):
  l=[]
  for i in num:
    if i>0:
      l.append(i)
  return l

positive(list(map(int,input().split())))
