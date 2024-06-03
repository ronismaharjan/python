import pandas

data = pandas.read_csv("data.csv")

data_to_dict = data.to_dict()
print(data_to_dict)
# print(type(data))
rolls = data["roll"]

print(rolls.max())


print(type(data))
print(data[data.fname == "ronish"])


pandas.DataFrame()