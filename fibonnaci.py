def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-1))
nterms=int(input("How many terms?" ))
if nterms<=0:
    print("Please enter a integer ")
else:
    print("Fibbonaci sequences:")
for i in range(nterms):
    print(recur_fibo(i))