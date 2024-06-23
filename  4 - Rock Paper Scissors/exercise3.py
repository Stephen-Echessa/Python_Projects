from turtle import position


row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]

map=[row1,row2,row3]

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[horizontal][vertical] = "X"

print(f"{row1}\n{row2}\n{row3}")
