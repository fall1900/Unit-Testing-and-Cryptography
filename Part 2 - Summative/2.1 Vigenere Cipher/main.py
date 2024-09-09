# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  new_str = ""
  for let in text:
    index_a = alpha.index(let)
    index_b = alpha.index(keyword[index_a])
    index_sum = (index_a + index_b) % 26
    new_str += alpha[index_sum]
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