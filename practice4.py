x = 0b01001100
print(bin(x))
shifted_x = x >> 3
print(bin(shifted_x))
#  00001001
#& 00000011

# Apply the mask to the shifted number
# 00000011
masked = bin(shifted_x & 0b00000011)
print(bin(shifted_x & 0b00000011))
print(masked)