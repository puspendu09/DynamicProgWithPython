def DecimalToBinary(decimal, result=""):
    if decimal == 0:
        return result

    result = str(decimal % 2) + str(result)
    return DecimalToBinary(decimal // 2, result)


print(DecimalToBinary(10))
