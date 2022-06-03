def get_alphabet():
    alphabet = ""
    for i in range(65, 90+1):
        alphabet += chr(i);
    return alphabet


print(get_alphabet()) #ABCDEFGHIJKLMNOPQRSTUVWXYZ