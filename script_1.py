#Promt the user to enter the DNA sequence of desired species
seq = input("Enter the sequence of your choice: ")
#initiallising the variables to 0. the variable will be used as individial sum of the content of the sequence.
a = 0
t = 0
c = 0
g = 0
#Calculating the length of the sequence.
#Alternative way to claculate the sequence is to sum a, t, c, g.
seq_len = len(seq)
#Using for loop on seq to iterate through the seq list.
for s in seq:
    #if element present in seq is comaparable to the conditions below then one will be added to the corresponding variable initallised 0 earlier.
    if(s == "a" or s == "A"):
        a = a + 1
    elif(s == "t" or s == "T"):
        t = t + 1    
    elif(s == "c" or s == "C"):
        c = c + 1 
    elif(s == "g" or s == "G"):
        g = g + 1 
#Dispalying the result to the user.
print("Total length of the sequence is " + str((seq_len)))
print("A content in sequence is " + str((a)))
print("T content in sequence is " + str((t)))
print("C content in sequence is " + str((c)))
print("G content in sequence is " + str((g)))