# this program takes a number and prints all of the prime numbers up to that number

number = 0
count_prime = 0

# Functions starts here

# function for checking if a number is a prime
# the input is the number to check if it is a prime
# the output is True if it is a prime or False if it is not a prime
def check_if_prime(number_to_check):
  for i in range(2, number_to_check):
    #Print debugging messages to help us understand the code
    #print("Divide", prime_number, "by", i, "remainder is", prime_number%i)

    if number_to_check%i == 0:
      #If it can be divided by at least one number between 2-'j' then it is not a prime number - so set the 'prime' flag to False and break the loop as we know 'j' is not a prime
      return False
  return True
# function for input number
# takes no input
# outputs the number entered by the user
def get_input():
  while True:
    number_str = input("Enter a Number: ")

    if number_str.isdecimal():
      return int(number_str)
      #print(prime_number_str)   #Debugging message to check the code
    else:
      print("You Entered an Incorrect Number - Please Try Again")

# Functions ends here

# Main code starts here
number = get_input()

print("The Prime Numbers Are: ",end='')

# counts from 2 to number
for j in range(2, number + 1):

  if check_if_prime(j):
    print(j,end=', ')
    count_prime += 1

# prints the total amount of prime numbers
print("")
print("There were a Total of", count_prime, "Prime Numbers")


    