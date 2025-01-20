f1_data = [int(i) for i in open("file1.txt").readlines()]
f2_data = [int(i) for i in open("file2.txt").readlines()]
duplicates = [i for i in f1_data if i in f2_data]
print(duplicates)
