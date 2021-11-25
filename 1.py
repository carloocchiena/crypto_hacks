# xor conversion
a = "label"
b = 12
label_uni = []
hex_string = []

for i in a:
  print(ord(i))
  label_uni.append(ord(i))

for i in label_uni:
  hex_string.append(hex(int(i) ^ int(13))[2:])

alfa = "".join(hex_string)

print(hex_string)
print(alfa)

bytes_object = bytes.fromhex(alfa)
ascii_string = bytes_object.decode("ASCII")

print(ascii_string)
