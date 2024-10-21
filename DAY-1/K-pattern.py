'''

* * * * *   

* * * *    

* * *     

* *      

*       

* *  

* * *  

* * * *  

* * * * * 

'''




n=int(input("Enter No of rows="))
for i in range(n):
    print("* "*(n-i), " "*(i),end=" ")
    print("\n")
for i in range(2,n+1):
    print("* "*i,end=" ")
    print("\n")