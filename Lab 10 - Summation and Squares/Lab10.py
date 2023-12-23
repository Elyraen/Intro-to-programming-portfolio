def sumN(x, y):
    sumResult = x + y
    return sumResult

def sumNSquares(N):
    square_sum = sum(i ** 2 for i in range(1, N + 1))
    return square_sum

def main():
    x = int(input("Input initial value of sum: "))
    y = 2
    sum_result = sumN(x, y)
    print("Sum of", x, "and", y, "is:", sum_result)

    N = int(input("Input a value for N: "))
    square_sum_result = sumNSquares(N)
    print("Sum of squares from 1 to", N, "is:", square_sum_result)

main()