f_name = input("What is your firstname? ")
l_name = input("What is your lastname? ")

def format_name(firstname,lastname):
    return firstname.title() + " " + lastname.title()

print(format_name(f_name,l_name))