from code_to_string import Code_to_String
from string_to_code import String_to_Code

print('\n----------------------------------------------------------------------------')
print('                           Morse Code Converter                             ')
print('----------------------------------------------------------------------------')
print('Please note that morse code here is represented by . for dots and - for bars\n')
print('Readings for the morse code are as follows:\n'
              'Seven spaces between words\n'
              'Three spaces between letters\n'
              'One space between symbols\n\n')

choice = input("What will you pick as an input: Text or Code \n").strip()
output = ''

if choice == 'Text':
    output = String_to_Code().convert()
elif choice == 'Code':
    output = Code_to_String().convert()
    
print(output)

