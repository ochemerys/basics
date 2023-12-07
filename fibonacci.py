def fibs(n):
  if n<=1:
    return n
  else:
    return (fibs(n-1)+ fibs(n-2))

## import pdb; pdb.set_trace() 
result = fibs(10)
print('fibs(10) = ' + str(result))