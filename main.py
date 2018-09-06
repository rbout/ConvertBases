inputBase = input("Enter a input base (1-16): ")

# Error Checking
while (not inputBase in "012345678910111213141516") or (int(inputBase) > 16 or int(inputBase) < 1):
    print("Must be a number from 1-16")
    inputBase = input("Enter a input base (1-16): ")

outputBase = input("Enter a output base (1-16): ")

# Error Checking
while (not outputBase in "012345678910111213141516") or (int(outputBase) > 17 or int(outputBase) < 1):
    print("Must be a number from 1-16")
    outputBase = input("Enter a output base (1-16): ")

inputBase = int(inputBase)

s = input("Enter a input number: ")

# More error checking on the value to convert
if int(inputBase) <= 10:
    while (not s in "0123456789") or (int(s) > inputBase - 1 or int(s) < 0):
        s = input("Bad input, try again: ")
elif int(inputBase == 11):
    checkInput = True
    while checkInput:
        for x in s:
            if x in "BCDEFGHIJKLMNOPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz":
                s = input("Bad input, try again: ")
                break
        else:
            checkInput = False
elif int(inputBase == 12):
    checkInput = True
    while checkInput:
        for x in s:
            if x in "CDEFGHIJKLMNOPQRSTUVWXYZcdefghijklmnopqrstuvwxyz":
                s = input("Bad input, try again: ")
                break
        else:
            checkInput = False
elif int(inputBase == 13):
    checkInput = True
    while checkInput:
        for x in s:
            if x in "DEFGHIJKLMNOPQRSTUVWXYZdefghijklmnopqrstuvwxyz":
                s = input("Bad input, try again: ")
                break
        else:
            checkInput = False
elif int(inputBase == 14):
    checkInput = True
    while checkInput:
        for x in s:
            if x in "EFGHIJKLMNOPQRSTUVWXYZefghijklmnopqrstuvwxyz":
                s = input("Bad input, try again: ")
                break
        else:
            checkInput = False
elif int(inputBase == 15):
    checkInput = True
    while checkInput:
        for x in s:
            if x in "FGHIJKLMNOPQRSTUVWXYZfghijklmnopqrstuvwxyz":
                s = input("Bad input, try again: ")
                break
        else:
            checkInput = False
elif int(inputBase == 16):
    checkInput = True
    while checkInput:
        for x in s:
            if x in "GHIJKLMNOPQRSTUVWXYZghijklmnopqrstuvwxyz":
                s = input("Bad input, try again: ")
                break
        else:
            checkInput = False

outputBase = int(outputBase)
decimalNum = 0
exp = len(s) - 1

# Goes through the input s and checks if the digit is a number
# or a letter used in hexadecimal
for digit in s:
    if digit in "0123456789":
        digit = int(digit)
    elif digit in "ABCDEF":
        digit = ord(digit) - 55
    else:
        digit = ord(digit) - 87
    decimalNum += digit * (inputBase ** exp)
    exp -= 1

# Have to use quotient and remainders to convert to the output base
quotient = decimalNum
endNum = ""
while quotient != 0:
    rem = quotient % outputBase
    quotient = quotient // outputBase
    if rem >= 10:
        rem = chr(rem + 55)
    else:
        rem = str(rem)
    endNum = rem + endNum
print(endNum)
