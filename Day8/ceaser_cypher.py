# ceaser_cypher.py

from functions import caesar



option = input("Type 'encode' to encode and 'decode' to decode the message: ").lower()

text = input("Input the text: ").lower()
shift = int(input('Type the shift number: '))

caesar(text,shift, option)

