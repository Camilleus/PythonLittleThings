import time
from functools import lru_cache


@lru_cache()
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


start = time.time()
n = int(input("Which number of Fibonacci sequence do you want to see? (If it is bigger than 20, this can take a little bit more time)"))
for i in range(n+1):
    print(f"{i}. Fibonacci sequence number is {fibonacci(i)}")

end = time.time()
print(f"This operation took {end - start} seconds")
