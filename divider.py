import numpy as np


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

number1_np = np.array([number1])
number2_np = np.array([number2])

numbers_sum = number1_np / number2_np

print(f"{number1_np[0]} / {number2_np[0]} = {numbers_sum[0]}")

input("Hit enter to close")
