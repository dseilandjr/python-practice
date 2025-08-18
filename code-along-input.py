import array

#first_name = input("Please enter your first name: ")
#print(first_name)

#Age = int(input("Please enter your Age: "))
#print(Age)
#print(type(Age))

temp = array.array('f', [72.5, 74.0, 69.8, 70.2, 73.1, 75.6, 71.3])
print(temp)

temp = [x + 1.0 for x in temp]
print(temp)