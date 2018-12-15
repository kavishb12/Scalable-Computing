filename = 'hid.txt'
f1 = open('shah_256_file','w')
f2 = open('shah_512_file','w')
f3 = open('md5_file','w')
f4 = open('pbkdf2_shah_file','w')
f5 = open('des_file','w')
f6 = open('unknown_hash_file','w')
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
with open(filename,'r') as file:
    
    for num,line in enumerate(file,1):
        if '[+] Unknown hash' in line:
            l6.append(num)
        elif '[+] SHA-256 Crypt' in line:
            l1.append(num)

        elif 'SHA-512 Crypt' in line:
            l2.append(num)
        elif 'MD5 Crypt' in line:
            l3.append(num)
        elif '[+] PBKDF2-SHA256(Generic)' in line:
            l4.append(num)
        elif '[+] DES(Unix)' in line:
            l5.append(num)
l_1 = [x-1 for x in l1]            
l_2 = [x-1 for x in l2]            
l_3 = [x-1 for x in l3]            
l_4 = [x-1 for x in l4]            
l_5 = [x-1 for x in l5]            
l_6 = [x-1 for x in l6]            

with open(filename,'r') as file:
    for num,line in enumerate(file,1):
        if num in l_1:
            f1.writelines(line)
        elif num in l_2:
            f2.writelines(line)
        elif num in l_3:
            f3.writelines(line)
        elif num in l_4:
            f4.writelines(line)
        elif num in l_5:
            f5.writelines(line)
        elif num in l_6:
            f6.writelines(line)
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()