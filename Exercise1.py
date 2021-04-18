# Create a Python project to get the value of Pi to n number of decimal places.
# Used decorator
import math

def pi_calc(func):
    while True:
        try:
            def wrapper():
                return func()
            return wrapper
            break
        except ValueError:
            # If the user does not enter a integer then ask them to try again
            print("That was not a valid number. Please enter a number. Try again...")
            return


@pi_calc
def pi_uptoNdigits():
    # Ask the user to input n
    user_input = int(input("Please input an integer n, to get n number of decimal places: "))
    approx_pi_fp = lambda x: round(math.pi, x)
    return print(approx_pi_fp(user_input))


pi = pi_uptoNdigits()

