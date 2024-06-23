import pandas as pd

data = pd.read_csv('Morse_code.csv')

word_space = '       '
letter_space = '   '

class Code_to_String:
    STRING_LIST = data.STRING.values.tolist()
    MORSE_CODE_LIST = data.MORSE_CODE.values.tolist()
    
    def __init__(self):
        pass
    
    def convert(self):
        code = input("\nEnter Morse Code Here: ").strip()
        code_list = []
        output_code_list = []
        
        if word_space in code:
            sentence_list = code.split(word_space)   
            for t in sentence_list:
                if letter_space in t:
                    for letter in t.split(letter_space):
                        code_list.append(letter)
                    code_list.append(' ')  
                else:
                    code_list.append(t.strip())
                    code_list.append(' ')
                    
        elif letter_space in code:              
            code_list = code.split(letter_space)
            
        else:
            code_list.append(code.strip())  
        
        print(code_list)
                
        for t in code_list:
            if t == ' ':
                output_code_list.append(' ')
            else:
                try:
                    id = self.MORSE_CODE_LIST.index(t)
                except ValueError:
                    print("The value given cannot be translated.")
                    output_code_list.clear()
                    break
                except:
                    print("Something went wrong.")
                    output_code_list.clear()
                    break
                else:
                    output_code_list.append(self.STRING_LIST[id])     
        
        output_code = ''.join(output_code_list)
        return output_code