def sumOfNaturalNum(number):
    if number <= 1:
        return number
    else:
        return number + sumOfNaturalNum(number - 1)


print(sumOfNaturalNum(100))
