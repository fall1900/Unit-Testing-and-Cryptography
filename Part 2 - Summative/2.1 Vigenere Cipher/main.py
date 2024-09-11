# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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
    for let in text:
        if let not in alpha:
            new_str += let
        else:
            index_a = alpha.index(let)
            for let in keyword_str:
                index_b = alpha.index(let)
            index_sum = (index_a + index_b)
            new_str += alpha[index_sum - 26]
    return new_str


def vig_decode(text, keyword):
    new_str = ""

    return new_str


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!





























