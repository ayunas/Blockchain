import locale

e = locale.getpreferredencoding()
print(e)

hw = 'hello'.encode("utf-8")
print(hw)
print("amir".encode("utf-8"))

cool = '😎'
print(len(cool))
cool_encoded = cool.encode("utf-8")

print('cool encoded',cool_encoded, list(cool_encoded))

print(ascii('hello world'))

print(bin(1981))

compare = (
    "a" ==
    "\x61" == 
    "\N{LATIN SMALL LETTER A}" ==
    "\u0061" ==
    "\U00000061"
)

print(compare)

binary_literal = 0b111
octal_literal = 0o11
hex_literal = 0x11

print(binary_literal,octal_literal,hex_literal)



