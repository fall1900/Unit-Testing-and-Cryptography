# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    new_str = ""
    for let in text:
        if let in alpha:
            index = alpha.index(let)
            new_str += codebet[index]
        else:
            new_str += let
    return new_str


def sub_decode(text, codebet):
    new_str = ""
    for let in text:
        if let in alpha:
            index = codebet.index(let)
            new_str += alpha[index]
        else:
            new_str += let
    return new_str


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)