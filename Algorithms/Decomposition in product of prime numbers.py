def is_prime(n):
    """This function returns if n is prime (True) or not (False)"""
    for i in range(2, n):
        if n % i == 0:  # here we don't have to specify that n has not to be equal with n because the for loop
            return False  # stops before arriving to n
    return True


def find_prime(n):
    """This function returns the list of all prime numbers from 2 to
    n (chosen number)."""
    all_prime_numbers = []
    for i in range(2, n):
        if is_prime(i):
            all_prime_numbers.append(i)

    return all_prime_numbers


def find_product_of_prime_numbers(n):
    """This function returns the list representing the decomposition in product of prime number of n"""
    all_prime_number = find_prime(n)  # recovering the list of prime numbers from 2 to n
    product = []

    # reversing the list to get the list descending so we can go from the highest to the lowest
    all_prime_number.reverse()

    for prime in all_prime_number:
        while n % prime == 0:  # here we set up not only a if condition but a while in case if we can divide
            n //= prime  # the number twice or more
            product.append(prime)

    if is_prime(n):
        if len(product) == 0:  # in case if n was already a prime number that can't being decomposed
            return n  # the list would have a null length so we return the chosen number
        else:
            product.sort  # we sort the list so that can more readable
            return product

print(find_product_of_prime_numbers(152235))