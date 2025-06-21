def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def prime_numbers(start,end):
    prime_list = []
    for num in range(start,end+1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

a = int(input("Enter start value : "))
b = int(input("Enter end value : "))

primes = prime_numbers(a,b)

print(primes)