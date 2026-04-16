n=int(input("enter a no:"))
def prime(n): 
     if n<=1:
        print("not a prime")
     else:
        for i in range(2,int(n/2)+1):
          if n%i==0:
            flag=False
            break
          else:
            flag=True
        
if prime(n):
     print("not a prime")
else:
        print("prime")