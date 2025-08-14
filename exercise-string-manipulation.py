# 1. Given a string, split the values into individual values.
to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_value = to_be_changed.split('|')
print(changed_value)

# 2. We were given these lyrics to split for a karaoke machine. Split the lyrics by line using split().
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""

lyrics_split = lyrics.split()
print(lyrics_split)

# 3. Split the lyrics by line using something other than split().
lyrics_split_by_line = lyrics.splitlines()
print(lyrics_split_by_line)

# 4. How long is the long village name string?
long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print(string_length)

# 5. We want all folders in this path without additional spaces. How would you get that?
my_path = ' /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM'
my_folders = my_path.strip()
print(my_folders)

# 6. Given this list of names, change the third name in the list to be "Wolfgang Mozart".
composers="Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
# Separate the composers
composers_split = composers.split(';')
# Get the third composer
third_composer = composers_split[2]
# Find the comma in the name
comma_position = third_composer.find(',')
# Use the slicing notation to get the last name
last_name = third_composer[:comma_position]
# Use the slicing notation to get the first name
first_name = third_composer[comma_position + 1:]
# Join the names to get the 3rd composer's name in "first last" format
third_composer_name = first_name + " " + last_name
# Print the composer's name
print(third_composer_name)

