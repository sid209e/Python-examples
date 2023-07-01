"""Create a Python program that collects data from the user
and stores it in a text file as a log. Prompt the user for
input and append the input to the file with a timestamp."""

from datetime import datetime


def log_data(filename):
    with open(filename,"a") as file:
        data = input("Enter data: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {data}\n")


filename = "log.txt"
log_data(filename)
