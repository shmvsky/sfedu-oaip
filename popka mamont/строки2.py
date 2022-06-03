def clear_str_from_letters(str):
    clear_str = ""
    for ch in str:
        ascii_code = ord(ch)
        if (48 <= ascii_code <= 57) or ascii_code == 43 or ascii_code == 45:
            clear_str += ch
    return clear_str


def split_arithmetic(string):
    lis = []
    current = ""
    for ch in string:
        if ch in ["+", "-"]:
            lis.append(current)
            lis.append(ch)
            current = ""
        else:
            current += ch
    lis.append(current)
    return lis

def evaluate(string):
    lis = split_arithmetic(string)
    if len(lis) == 1:
        return lis[0]
    output = float(lis[0])
    lis = lis[1:]
    while len(lis) > 0:
        operator = lis[0]
        number = float(lis[1])
        lis = lis[2:]
        if operator == "+":
            output += number
        elif operator == "-":
            output -= number
    
    return output