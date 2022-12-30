def prime_check(n):
    if n==1:
        print("1 is neither prime nor composite")
    for i in range(2,n):
        if n%i==0:
            return False
    return True

a=int(input("Enter the starting number: "))
b=int(input("Enter the ending number: "))
prime=0
composite=0
for i in range(a,b+1):
    if i==1:
        print("1 is neither prime nor composite")
        pass
    elif prime_check(i):
        print(i,"is prime")
        prime=prime+1
    else:
        print(i,"is composite")
        composite=composite+1

print(f'{prime} prime number and {composite} composite number in the range')