def get_prime_factors(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(get_prime_factors(num))
