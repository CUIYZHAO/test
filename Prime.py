x = int(input())
isprime = True
for k in range(2, x):
    if x % k == 0:
        isprime = False
        break  
if isprime:
    print('{} is prime'.format(x))
else:
    print('{} is not prime'.format(x))
