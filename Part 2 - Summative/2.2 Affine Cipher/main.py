import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    """
    takes the text, the caesar shift number, and the multiply number; encodes the message
    :param text: the input message that needs to be encoded
    :param a: what you want to multiply the index of the letter by
    :param b: amount of times to caesar shift the letter by
    :return: returns the encoded message
    """
    new_str = ""
    for let in text:
        index = (alpha.index(let) * a + b) % 26
        new_str += alpha[index]
    return new_str

def affine_decode(text, a, b):
    """
    takes the encoded message, the caesar shift number, and the multiply number; decodes the message
    :param text: the encoded message that needs to be decoded
    :param a: what you want to multiply the index of the letter by
    :param b: amount of times to caesar shift the letter by
    :return: returns the decoded message
    """
    new_str = ""
    for let in text:
        index = (alpha.index(let) - b) * mod_inverse(a, 26) % 26
        new_str += alpha[index]
    return new_str

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!


# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    """
    takes the text and encodes it into a number
    :param ngram: the message you want to encode
    :return: returns the ngram as an encoded number
    """
    number = 0
    for i in range(len(ngram)):
        index = alpha.index(ngram[i])
        number += index * (26**i)
    return number

def convert_to_text(num, n):
    """
    takes a number and converts it back into a string of letters
    :param num: the number that you want to convert into text
    :param n: length of the original ngram
    :return: the original ngram
    """
    new_str = ""
    for i in range(n):
        index = num % 26
        new_str += alpha[index]
        num = num // 26
    return new_str

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    pass
    # loop_times = len(text) // n
    # num = 0
    # new_str = ""
    # for i in range(loop_times):
    #     str_slc = (text[n * i:n * (i+1)])
    #     for i in range(len(str_slc)):
    #         index = alpha.index(str_slc[i])
    #         num += index * (26 ** i)
    #         index = (alpha.index(str_slc[i]) * a + b) % 26
    #         new_str += alpha[index]
    #         index = num % 26
    #         new_str += alpha[index]
    #         num = num // 26
    # return new_str


def affine_n_decode(text, n, a, b):
    return ''

test = "CO0L"
n = 5
a = 347
b = 1721
# enc = affine_n_encode(test, 2, 3, 121)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!