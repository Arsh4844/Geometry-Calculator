#Author = Arshdeep Singh
#Date created = january 31, 2022
#Date Modified = January 31, 2022
length = input("Enter Length of Rectangle in cm's :- ")#length input asked from user
width = input("Enter width of Rectangle in cm's :- ")#width input asked form user
area = float(length) * float(width)#rectangle area formula used with float function as input can be decimal
perimeter = 2*float(length + width)#perimeter calculated with common float function for length and width
print("Area = " + str(area) + " cm sq")#Area printed
print("Perimeter = "+ str(perimeter) + " cm")#perimeter printed