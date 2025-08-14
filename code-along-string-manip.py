string1 = 'This is a valid string'
string2 = "This is also a valid string"

palindrome = "Go hang a salami, I'm a lasagna hog."

# Using the other quote for the nested quote
string3 = "'Always look on the bright side of life', he said."

# Using escaped quotes for the nested quote
string4 = "\"Always look on the bright side of life\", he said."

print(string3)
print(string4)

len(string4)

filepath = '       /var/www/java/packages/are/too/long/here             '
print(filepath)

filepath = filepath.strip()
print(filepath)

folders = filepath.split('/')
print(folders)
print(type(folders))

windowsPath = "\\".join(folders)
print(windowsPath)
print(type(windowsPath))

multi = '''
Now this is a story all about how
My life got flipped turned upside down'''
print(multi)

print(multi.splitlines())

reservation_name = "Froman, abe"
char_to_find = ","
# Where is the comma?
char_location = reservation_name.find(char_to_find)
print(char_location)

char_location2 = reservation_name.index(char_to_find)
print(char_location2)




