#Enter name==santoshi
'''
s  
s a  
s a n  
s a n t  
s a n t o  
s a n t o s  
s a n t o s h  
s a n t o s h i 
 '''

name=input("Enter name==")
for i in range(len(name)):
    for j in range(i+1):
        print(name[j],end=" ")
    print(" ")
        