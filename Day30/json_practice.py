import json
name = "eliot"
age = 14
gender = "male"
data_dict = {
    name: {
        "age": age,
        "gender": gender, }
}
with open("Day30/password.json", mode="r") as files:
    # json.dump(data_dict, files, indent=4)
    data = json.load(files)
    print(data)
