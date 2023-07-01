"""Create a function called generate_random_number() that
 generates and returns a random number between a given
minimum and maximum value. Use the random module in Python
 to accomplish this. """

import random


def generate_random_numer(min,max):
    return random.randint(min,max)


random_num = generate_random_numer(1,100)
print(random_num)