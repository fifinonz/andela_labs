#RECURSIVE LAB
#Create both a recursive function called recursive_factorial and iterative function called iterative_factorial that does the following

#Accepts as parameter an Integer n
#Computes the factorial of n
#Returns the factorial of n

def recursive_factorial(n):
  if n <= 1:
    return 1
    
  else:
    return (n * recursive_factorial(n-1))
    
    
def iterative_factorial(n):
  factorial = 1
  
  for i in range(n):
    factorial= factorial * (i+1)
  return factorial