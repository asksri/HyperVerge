#initiallizing a list to an empty list.
lst = []
#prompting the user to provide input.
number = input("Enter the data : ")
#converting the single string data into the segments by spliting them from the point of spaces.
w = number.split()
#Using for loop to iterate theugh the w to convert string into integers for further calculations.
for n in w:
    #converting string into the integers.
    x = int(n)
    #saving the integers in the list names "lst"
    lst.append(x)
#sorting the ddata of list in assecnding order.
sorted_list = sorted(lst)
#applying if condition to check if the number of elements in list are even or odd.
if len(sorted_list) % 2 != 0:
    #odd number of elements
    index = int((len(sorted_list))/2) 
    #displaying the user results through screen.
    print(sorted_list[index])
elif len(sorted_list) % 2 == 0:
    #even no. of elements
    index_1 = int((len(sorted_list)/2) - 1)
    index_2 = int(len(sorted_list)/2)
    #mean is being sed as number of elements in the list are even.
    mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
    #Displaying the result to the user through screen.
    print(mean)