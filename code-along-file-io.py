file_path = (r'data.csv')
print(file_path)

f = open("samplefile.txt", "w")
for i in range (1,4):
    f.write(f"{i}, row{i}, data{i}, data{i+1}, data{i+2}\r\n")
f.close()