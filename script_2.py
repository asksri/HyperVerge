#sum of square of n natural number
#prompting user to enter the number upto witch user desires to find the sum of squares.
number = input("Enter the number : ")
#converting the string into integer data type
number = int(number)
#initiallising a list according to the input user has entered.
l = [x**2 for x in range(1, number+1)]
#initiallising the sum of squares of the first natural numbers. 
sum = 0
#for loop to iterate through the list to calculate the sum.
for i in l:
  sum += i
#displaying sum on the screen.
print("Sum of the squares of " + str(number) + " is " + str(sum))