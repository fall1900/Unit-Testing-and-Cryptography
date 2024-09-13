# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"


def vig_encode(text, keyword):
    text = text.upper()
    keyword = keyword.upper()
    new_str = ""
    extra_word = ""
    if len(text) % len(keyword) == 0:
      times_printed = int(len(text) / len(keyword))
    else:
      for i in range(len(text) % len(keyword)):
        extra_word += keyword[i]
      times_printed = int((len(text) - len(extra_word)) / len(keyword))
    keyword_str = keyword * times_printed
    full_keyword = keyword_str + extra_word
    for i in range(len(text)):
        text_let = text[i]
        keyword_let = full_keyword[i]
        index_a = alpha.index(text_let)
        index_b = alpha.index(keyword_let)
        index_sum = (index_a + index_b) % 27
        new_str += alpha[index_sum]
    return new_str


def vig_decode(text, keyword):
    low = 0
    if text == text.lower():
        low += 1
    text = text.upper()
    keyword = keyword.upper()
    new_str = ""
    extra_word = ""
    if len(text) % len(keyword) == 0:
        times_printed = int(len(text) / len(keyword))
    else:
        for i in range(len(text) % len(keyword)):
            extra_word += keyword[i]
        times_printed = int((len(text) - len(extra_word)) / len(keyword))
    keyword_str = keyword * times_printed
    full_keyword = keyword_str + extra_word
    for i in range(len(text)):
        text_let = text[i]
        keyword_let = full_keyword[i]
        index_a = alpha.index(text_let)
        index_b = alpha.index(keyword_let)
        index_sum = (index_a - index_b)
        if index_sum < 0:
            index_sum += 27
        else:
            index_sum -= 27
        new_str += alpha[index_sum]
    if low == 1:
        new_str = new_str.lower()
    return new_str


test = "NAHIDWIN"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!





























