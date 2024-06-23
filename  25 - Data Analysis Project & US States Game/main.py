import pandas
import pandas as pd

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color_varieties = fur_color.drop_duplicates().tolist()
fur_color_list = [x for x in fur_color_varieties if pd.isnull(x) == False]

gray_count = fur_color[fur_color == "Gray"].count()
cinnamon_count = fur_color[fur_color == "Cinnamon"].count()
black_count = fur_color[fur_color == "Black"].count()

data_dict = {
    "Fur Color": fur_color_list,
    "Count": [gray_count, cinnamon_count, black_count]
}

print(data_dict)

pandas.DataFrame(data_dict).to_csv("squirrel_count.csv")
