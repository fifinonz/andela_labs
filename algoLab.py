#ALGO LAB
#Create a function get_algorithm_result to implement the algorithm below

#Get a list of numbers L1, L2, L3....LN as argument
#Assume L1 is the largest, Largest = L1
#Take next number Li from the list and do the following
#If Largest is less than Li
#Largest = Li
#If Li is last number from the list then
#return Largest and come out
#Else repeat same process starting from step 3

#Create a function prime_number that does the following

#Takes as parameter an integer and
#Returns boolean value true if the value is prime or
#Returns boolean value false if the value is not prime



def get_algorithm_result(numbers):
  largest=numbers[0]
  for item in range(0,len(numbers)):
    if largest < numbers[item]:
      largest=numbers[item]
  #end for loop
  return largest
        

def prime_number(n): 
  # make sure n is a positive integer
  n = abs(int(n))
  
  # 0 and 1 are not primes
  if n < 2:
    return False
  
  # 2 is the only even prime number
  if n == 2:
    return True
    
  # all other even numbers are not primes
  if not n & 1: 
    return False
    
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
  for x in range(3, int(n**0.5)+1, 2):
    if n % x == 0:
      return False
      
  return True