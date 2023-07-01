"""Create a function called fibonacci(n) that generates
and returns the Fibonacci sequence up to the nth term.
The Fibonacci sequence starts with 0 and 1, and each subsequent
term is the sum of the two previous terms. """

def fibonacci(n):
    sequence = [0, 1]

    if n <= 1:
        return sequence[:n+1]

    while len(sequence) <= n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence


fib = fibonacci(15)
print(fib)