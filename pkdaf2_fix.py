list_final = []
with open('pbkdf2_1.broken','r') as temp:
    list_des = temp.readlines()
temp.close()
list_q = [i.split()[0] for i in list_des]
list_w = [i.split()[1] for i in list_des]
list_z = [i.split()[2] for i in list_des]
for l,m,z in zip(list_q,list_w,list_z):
    list_final.append(l + '$' + m + " "+ z + "\n")
    
with open('pbkdf2_1_f.broken','w') as f:
    for item in list_final:
        f.writelines(item)
    