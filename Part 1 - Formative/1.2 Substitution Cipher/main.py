# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    """
    takes the text that needs to be encoded and the alphabet that is used to encode; returns the encoded text
    :param text: the text that needs to be encoded
    :param codebet: the alphabet that is used to encode the text
    :return: the encoded text
    """
    new_str = ""
    for let in text:
        if let in alpha:
            index = alpha.index(let)
            new_str += codebet[index]
        else:
            new_str += let
    return new_str


def sub_decode(text, codebet):
    """
    takes the encoded text and the alphabet that is used to encode/decode; returns the decoded text
    :param text: the text that needs to be decoded
    :param codebet: the alphabet that is used to encode/decode the text
    :return: the decoded text
    """
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
