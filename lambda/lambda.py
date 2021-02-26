import math

isOdd = lambda x: False if x % 2 == 0 else True
print(isOdd(13))

isPrime = lambda x: all(x % y != 0 for y in range(2,int(math.sqrt(x)) + 1))
print(isPrime(15))

isPalindrome = lambda x: list(str(x)) == list(reversed(str(x)))
print(isPalindrome(1612))


