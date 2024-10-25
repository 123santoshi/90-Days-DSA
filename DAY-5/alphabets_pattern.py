#Enter n valyue==5
'''
A  
B C  
D E F  
G H I J  
K L M N O 

'''

n=int(input("Enter n valyue=="))
a=65
for i in range(n):
    for j in range(i+1):
        print(chr(a),end=" ")
        a+=1
    print(" ")
        