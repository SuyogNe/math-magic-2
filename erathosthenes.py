def SieveOfEratosthenes(n):
   prime=[True for i in range(n+1)]
   p=2
   while (p*p<=n):
        if (prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    
   for p in range(2,n+1):
        if prime[p]:
            print(p)


num=int(input())
print("Following are the prime numbers smaller than or equal to", num)
SieveOfEratosthenes(num)