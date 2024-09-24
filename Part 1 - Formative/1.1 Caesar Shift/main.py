# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    """
    takes the number of shift times and the text; returns the encoded text
    :param text: the text that needs to be encoded
    :param n: amount of times to shift the text
    :return: the encoded text
    """
    new_str = ""
    for let in text:
        if let in alpha:
            index = alpha.index(let)
            new_str += alpha[(index + n) % 26]
        else:
            new_str += let
    return new_str


def caesar_decode(text, n):
    """
    takes the number of shift times and the encoded text; returns the decoded text
    :param text: the encoded text
    :param n: amount of times to shift the text
    :return: the decoded text
    """
    new_str = ""
    for let in text:
        if let in alpha:
            index = alpha.index(let)
            new_str += alpha[(index - n) % 26]
        else:
            new_str += let
    return new_str


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
