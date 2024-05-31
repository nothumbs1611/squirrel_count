import csv
import pandas


# pull in squirrel census
#with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as squirrel_file:
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# create a list of just the colors:
grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]
red_squirrel = data[data["Primary Fur Color"] ==  "Cinnamon"]

# count the number of squirrels of a particular color
grey_count = (grey_squirrel["Primary Fur Color"].size)
black_count = (black_squirrel["Primary Fur Color"].size)
red_count = (red_squirrel["Primary Fur Color"].size)

# create a dataframe
squirrel_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Number": [grey_count, black_count, red_count]
}
colors = pandas.DataFrame(squirrel_dict)

# output into a squirrel_count.csv that contains fur color (from primary fur color) and count each color
colors.to_csv("Squirrel_count.csv")
print(colors)