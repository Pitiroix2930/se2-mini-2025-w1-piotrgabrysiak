import re
import string
from logging import exception

def calc(input):

    delimiters = []

    if input == "":
        return 0

    if input.isnumeric():
        return int(input)


    if input[0] == input[1] and input[0] == "/":
        for i in range(2,len(input)):
            delim = ""
            if input[i] == "\n":
                input = input[i+1:]
                break
            if input[i] == "[":
                for j in range(i+1,len(input)):
                    if input[j] == "]":
                        delimiters.append(delim)
                        i = j + 1
                        break
                    else:
                        delim += input[j]

            delimiters.append(input[i])

    for delimiter in delimiters:
        input = input.replace(delimiter, ",")

    numbers = re.split(r"[,\n]", input)
    numbers_int = [int(x) if int(x) <= 1000 else 0 for x in numbers]

    for num in numbers_int:
        if num < 0:
            raise ValueError("Negative values are not allowed")

    return sum(numbers_int)


