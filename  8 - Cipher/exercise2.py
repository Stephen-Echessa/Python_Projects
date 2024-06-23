n = int(input("Check this number: "))

def prime_checker(number):
    is_prime = ""
    for num in range(2,number):
        if number%num==0:
            is_prime = True
        else:
            is_prime = False
    
    if is_prime==False:
        print("This is not a prime number")
    elif is_prime==True:
        print("This is a prime number")

prime_checker(n)
