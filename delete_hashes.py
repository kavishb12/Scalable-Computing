filename_part = 'md5_4.broken'
filename_main = 'md5_file'

with open(filename_main,'r') as file_main:
    list_main = file_main.readlines()
file_main.close()


with open(filename_part,'r') as file_part: 
    list_part_temp = file_part.readlines()
file_part.close()

list_part = [i.split(':')[0]+"\n" for i in list_part_temp]

for i in list_part:
    if i in list_main:
        list_main.remove(i)

with open(filename_main,'w') as f:
    for item in list_main:
        f.writelines(item)
        