def DecimalToBinary(decimal:int, result=""):
    if decimal == 0:
        return result

    result = str(decimal % 2) + str(result)
    return DecimalToBinary(int(decimal / 2), result)
    # return result



print(DecimalToBinary(1))
