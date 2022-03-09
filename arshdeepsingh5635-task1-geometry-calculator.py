from xml.sax.saxutils import prepare_input_source


length = input("Enter Length of Rectangle in cm's :- ")
width = input("Enter width of Rectangle in cm's :- ")
area = float(length) * float(width)
perimeter = 2*float(length + width)
print("Area = " + str(area) + " cm sq")
print("Perimeter = "+ str(perimeter) + " cm")
