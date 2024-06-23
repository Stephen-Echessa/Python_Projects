with open("file1.txt") as file1:
    data1 = file1.read()
    data1_list = data1.splitlines()

with open("file2.txt") as file2:
    data2 = file2.read()
    data2_list = data2.splitlines()

result = [int(n) for n in data1_list if n in data2_list]
print(result)

