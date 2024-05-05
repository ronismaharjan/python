row1 =["1", "2", "3"]
row2 =["4", "5", "6"]
row3 =["7", "8", "9"]

map = [row1, row2, row3]
print(str(row1)+ "\n"+str(row2)+"\n"+str(row3))

place = input(("Where do you want to put the tressure?  column row :"))


user_column = int(place[0]) - 1
user_row = int(place[1 ]) - 1
map[user_row][user_column] = "x"


print(str(row1) +"\n"+ str(row2) + "\n" + str(row3))

