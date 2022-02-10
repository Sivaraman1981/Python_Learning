#area of rectangle l*b
#perimeter of rectangle 2*l+2*b

length=10
bre=float(input("enter the float value:"))
area = length*bre
print(int(area))
peri= 2 * length + 2 * bre
print(int(peri))

print("The area of rectangle is:",int(area))
print("The perimeter of rectangle is:",int(peri))


print(f"The area of rectangle is: {int(area)}")
print(f"The perimeter of rectangle is: {int(peri)}")
#format
print("the Area of rectangle with length {} and breadth {} is {} ".format(length, breadth,int(Area)))
print(f"the Area of rectangle with length {length} and breadth {breadth} is {int(Area)}")


print("the perimeter of rectangle with length {} and breadth {} is {} ".format(length, breadth,int(Area)))

#format with Indexing columns
length = 10

breadth = float(input("please enter breadth (float value): "))

Area = length * breadth
perimeter = 2 * (length + breadth)

print("the Area of rectangle with breadth {1} and length {0} is {2} ".format(length, breadth,int(Area)))