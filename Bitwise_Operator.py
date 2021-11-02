# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# To learn about the Bitwise operator
Num1=10
Num2=4
Num1Bin=bin(Num1)
Num2Bin=bin(Num2)
Bin1=Num1Bin.replace('0b','')
Bin2=Num2Bin.replace('0b','0')
print("The corresponding Binary values of 10 and 4 are :\n",Bin1,"\n",Bin2)
# Bitwise "and" operation (&)
print(Num1&Num2) # Here it compares each bit and returns 1 if both the values are 1 or 0 if one of the value or both 0
# Bitwise "or" operation (|)
print(Num1|Num2) # Here it compares each bit and returns 1 if one of the values or both of them are 1 and returns the respective decimal of it.
# Bitwise "not" operator
print(~Num1) # Returns the compliment of it.
# Bitwise "xor" operator
print(Num1^Num2) # Return 1 if atleast one of them is 1,returns 0 if both of them are 1, returns 0 if both of them are 0.

"""
Bitwise shift operations
"""

# Bitwise Right shift operation
print(Num2>>2)
# Bitwise Left shift operation
print(Num2<<2)

"""
Explanation for Num2:

Before right shift by 2   
Num2 = 0000 0100 | Decimal value = 4
After right shift by 2 (Dividing twice with 2[Because it's Binary 😥'])
Num2 = 0000 0001 | Decimal value = 1

Before left shift by 2
Num2 = 0000 0100 | Decimal value = 4
After left shift by 2 (Multiplying twice with 2)
Num2 = 0001 0000 | Decimal value = 16
"""

Num3=-10
Num4=-4
print(Num3>>2)
# 0000 1010  10
# 0000 1001  9
# 1111 0110 -10
# 1111 1101 -3
print(Num3<<2)
# 0000 1010  10
# 1111 0110 -10
# 1101 1000 -40
print(Num4>>2)
# 0000 0100  4
# 0000 0011  3
# 1111 1100 -4
# 1111 1111 -1
print(Num4<<2)
# 0000 0100  4
# 0000 0011  3
# 1111 1100 -4
# 1111 0000 -16

"""
Explanation for Num4:

Before right shift by 2   
Num4 = 1111 1100 | Decimal value = -4
After right shift by 2 (Dividing twice with 2)
Num4 = 1111 1111 | Decimal value = -1

Before left shift by 2
Num4 = 1111 1100 | Decimal value = -4
After left shift by 2 (Multiplying twice with 2)
Num4 = 1111 0000 | Decimal value = -16

So my conclusion is whenever we perform a right and left shift to a positive decimal integer,
the execution push the binary in the res.direction and add two 0's in the beginning(means the start position of the push 😑).
But negative decimal integers are the trickier part for me!
In the case of them, For a right push; it execute the kick and add two 1's instead of 0's in the case of positive integers.
And for a left shift, it performs the kick and add two 0's instead of 1 (I expected '1',but it turns out that am wrong).

⚡The End!⚡
"""