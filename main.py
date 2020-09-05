number = 0
number_str = ''


while True:
   number_str = input("Enter a Number: ")

   if number_str.isdecimal():
     number = int(number_str)
     prime = True     #Reset the 'prime' flag to True and start checking if 'number' is a prime
     #print(prime_number_str)   #Debugging message to check the code
     break
   else:
     print("You Entered an Incorrect Number - Please Try Again")




#Step through from 2 to the 'number' and see if 'number' can be divided by any of these number between 2-'number'
for i in range(2, number):

  #Print debugging messages to help us understand the code
  #print("Divide", prime_number, "by", i, "remainder is", prime_number%i)

  if number%i == 0:
    #If it can be divided by at least one number between 2-'number' then it is not a prime number - so set the 'prime' flag to False and break the loop as we know 'number' is not a prime
    prime = False
    break

#Check the 'prime' flag and if True we know it is a prime, if False we know it is not a prime
if prime == True:
   print("Yes it is a Prime Number")
else:
   print("No it is not a Prime Number")