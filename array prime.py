# print prime numbers

num=[1,2,3,4,5,6,7,8,9]
prime_numbers=[]
for i in num:
    k=0
    for j in range(1,i):
        if i%j==0:
            k+=1
    if k==1:
        prime_numbers.append(i)
print(prime_numbers)





