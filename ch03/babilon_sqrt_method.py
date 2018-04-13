import math

# 用户输入两个整数（两个整数、一个浮点数）
numStr = input("Find the square root of integer: ")
while not numStr.isdigit():
    print("Pay attention")
    numStr = input("Find the square root of integer: ")
number = int(numStr)

guess_Str = input("Initial guess: ")
while not guess_Str.isdigit():
    print("Pay attention")
    guess_Str = input("Initial guess: ")
guess_float = float(guess_Str)

originalGuess_float = guess_float  # hang onto the original guess
count_int = 0  # count the number of guesses

# get the float tolerance
tolerance_float = float(input("What tolerance: "))

# 按上述步骤完成算法
previous_float = 0
count_int = 0
while math.fabs(previous_float - guess_float) > tolerance_float:
    previous_float = guess_float
    quotient = number / guess_float
    guess_float = (quotient + guess_float) / 2
    count_int = count_int + 1

# 输出三个原始值
# 输出循环次数和平方根
print("Square root of %d is: %.8f" % (number, guess_float))
print("Took %d reps to get it to tolerance: %.8f" % (count_int, tolerance_float))
print("Starting from a guess of: %.8f" % (originalGuess_float,))
