import sys
from ctypes import *

# Define user-defined union
class tBits(Union):
    _fields_ = [
        ("f", c_float),
        ("i", c_uint32),
    ]

# Define user-defined structure
class tParts(Structure):
    _fields_ = [
        ("sign", c_uint32),
        ("exponent", c_uint32),
        ("significand", c_uint32)
    ]

def main():
    # initialization
    bits = tBits(0, 0)
    part = tParts(0, 0, 0)
    number = 0

    # User input
    number = int(input("Enter the number: "))

    # Dump actual input.
    print("Integer Number: {0}, Bits: 0x{1:>08x}, Size: {2}".format(number, number,  number.__sizeof__()))

    # Make an IEEE-754 number from its parts.
    part = Normalize(number)
    bits = MakeFloatBits(part)
    # Dump for debugging purposes.
    print("By Software, Number: {0:>12.6f}, Bits: 0x{1:>08x}".format(bits.f, bits.i));

    # Solve using hardware.
    bits.f = float(number)
    # Dump for debugging purposes.
    print("By Hardware, Number: {0:>12.6f}, Bits: 0x{1:>08x}".format(bits.f, bits.i));

def Normalize(num):
    part = tParts(0,0,0)

    if num == 0:
        return num

    # Handle sign
    if num < 0:
        part.sign = 1
        num *= -1

    # Bias the exponent by 127, also the number is not normalized at this point.
    # So, the exponent is in the low order bit, which is exponent 2^0.
    part.exponent += 127 + 32

    #  Normalize until the 1 appears in the high order bit.
    #  Adjust exponent at each step.
    while True:
        part.exponent -= 1
        num <<= 1
        strval = str(bin(num))

        # bin --> '0b0000 0000 0000 0000 0000 0000 0000 0000' 의 형식
        # 따라서 실제 수는 bin[2]부터 시작. (앞 자리는 '0b')
        if strval[2] == '1' and len(strval)-2 == 32:
            break;

    part.exponent -= 1

    # The high order bit is 1, but this is the phantom bit.
    # Shift it out
    num <<= 1

    # The high-order bit of the significand is in bit 31.
    # It should be in bit 22.
    part.significand = num
    part.significand >>= 9

    # Dump part for debugging.
    print("Sign: %u, Exponent: %u, Significand: 0x%08X" % (part.sign, part.exponent, part.significand));
    return part

def MakeFloatBits(part):
    bits = tBits(0,0)

    # Place each part in its proper IEEE-754 position.
    bits.i = (part.sign << 31) | (part.exponent << 23) | (part.significand)
    return bits

# Call the main function
main()