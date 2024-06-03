import pandas 


squirrel_data = pandas.read_csv("Day25/squirrel_data.csv")
squirrel_color = squirrel_data["Primary Fur Color"].to_list()
total_gray_squirrel = 0
total_cinnamon_squirrel = 0
total_black_squirrel = 0
for color in squirrel_color:
    if color == "Gray":
        total_gray_squirrel += 1
    elif color == "Cinnamon":
        total_cinnamon_squirrel += 1
    elif color == "Black":
        total_black_squirrel += 1
    
squirrel_color_data = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[total_gray_squirrel, total_cinnamon_squirrel,total_black_squirrel ],
    

}
# squirrel_black= squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
# print(type(squirrel_black))
# print(squirrel_black)

datas = pandas.DataFrame(squirrel_color_data)
print(squirrel_color_data)

datas.to_csv("Day25/squirrel_color_data.csv")