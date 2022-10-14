def SumDigits(number):
    if number < 10:
        return number
    else:
        return(number%10) + SumDigits(int(number/10))

print(SumDigits(10123))