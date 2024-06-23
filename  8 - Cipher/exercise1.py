import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height,width,cover):
    number_of_cans = math.ceil((height*width)/cover)
    print(f"You'll need {number_of_cans} cans of paint")

paint_calc(test_h,test_w,coverage)
