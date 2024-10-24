'''  
      *  

    *   *   

   *     *     

  *       *       

 *  *  *  *  *  

'''










n=int(input("Enter no of rows=="))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    if i==n-1:
        for j in range(i+1):
            print("* ",end=" ") 
    else:
        if i==0:
            for j in range(i+1):
                print('* ',end=" ")
        else:
            for j in range(2):
                print("* ", "  "*(i-1),end=" ")
    print("\n")
        