# Python daily pills - Day 010: Python Operators (Part 1)

Python divides the operators in the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

This is the last of a serie of two pills about Python operators. In this one we are going to cover Identity, Membership and Bitwise operators. For the first pill in this serie, [click here](../day-010).

## Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator | Description | Example
--- | --- | ---
`is` | Returns True if both variables are the same object | `x is y`
`is not` | Returns True if both variables are not the same object | `x is not y`

## Python Membership Operators

Membership operators are used to test if a sequence is presented in an object:

Operator | Description | Example
--- | --- | ---
`in` | Returns True if a sequence with the specified value is present in the object | `x in y`
`not in` | Returns True if a sequence with the specified value is not present in the object | `x not in y`

## Python Bitwise Operators

Bitwise operators are used to compare (binary) numbers:

Operator | Name | Description
--- | --- | ---
& | AND | Sets each bit to 1 if both bits are 1
\| | OR | Sets each bit to 1 if one of two bits is 1
 ^ | XOR | Sets each bit to 1 if only one of two bits is 1
~ |  NOT | Inverts all the bits
<< | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off
\>\> | Signed right shift | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

## References

More information about all Python operators in [this link](https://www.w3schools.com/python/python_operators.asp).
