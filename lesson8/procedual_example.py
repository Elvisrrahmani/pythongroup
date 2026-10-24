def calculate_area(length,width):
    return length*width

def calculate_perimetri(length,width):
    return  2*(length+width)

length = 5
width = 3

area = calculate_area(length,width)
Perimetri = calculate_perimetri(length,width)


print(f"Perimetri:{Perimetri}")
print(f"area:{area}")