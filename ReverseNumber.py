def reverseNumber(Number):
    rev = str(Number)[::-1]
    return rev

Number = int(input())

result = reverseNumber(Number)
print(result)