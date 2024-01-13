file_obj = open('file.txt', 'r')

# for line in file_obj:
#     print(line, end='')

print(file_obj.fileno())
file_obj.seek(13)

a = file_obj.readline()
print(a, end='')


print(file_obj.tell())

file_obj.close()
