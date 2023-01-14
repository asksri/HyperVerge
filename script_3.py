#Promt the user to enter the DNA sequence of desired species
seq = input("Enter the DNA sequence: ")
#initializing the variale named length to 0.
length = 0 
#using for loop to iterate through the elements of the seq list. 
for s in seq:
  #if the conditon provided in the conditional syntax is true then an 1 will be added to the length which will be the length of the seq entered.
  if(s == "a" or s == "t" or s == "c" or s == "g"):
    length += 1
#printing the desired results on the screen for user.
print("Length of the sequence is " + str(length))