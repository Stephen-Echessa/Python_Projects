import pandas as pd

data = pd.read_csv('Morse_code.csv')

class String_to_Code:
    STRING_LIST = data.STRING.values.tolist()
    MORSE_CODE_LIST = data.MORSE_CODE.values.tolist()
    
    def __init__(self):
        pass
        
    def convert(self):
        text = input("Enter Text Here: ").strip()
        text_list = [letter for letter in text]
        print(text_list)
        output_code_list = []
        
        for t in text_list:
            if t == ' ':
                output_code_list.append('       ')
                space_index = output_code_list.index('       ')
                output_code_list.pop(space_index - 1)
            else:
                try:
                    id = self.STRING_LIST.index(t.upper())
                except ValueError:
                    print("The value given cannot be translated.")
                    pass
                except:
                    print("Something went wrong")
                    pass
                else:
                    output_code_list.append(self.MORSE_CODE_LIST[id])     
                    output_code_list.append('   ')
        
        output_code = ''.join(output_code_list[:-1])
        return output_code
    