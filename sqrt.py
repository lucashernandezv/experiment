import math

def check_sqrt():
  num1=int(input("Type a number: "))
  num1_sqrt=math.sqrt(num1)
  
# rounds the number to the third decimal
  num1_sqrt_round=round(num1_sqrt, 3)
  
# if the sqroot != float, prints sqroot without decimal parts.
  if num1%num1_sqrt_round==0:
    print(int(num1_sqrt_round))
# if the sqroot is a float, prints the rounded sqroot.
  else:
    print(num1_sqrt_round)

  return(num1_sqrt)
  
check_sqrt()
