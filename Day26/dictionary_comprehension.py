# new_dict = {new_key: new_value for (key, value) in dict.items()}

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence_list = sentence.split()

# new_dict = {word:len(word) for word in sentence_list}
# print(new_dict)

# Exercise 1

# weather_c = {
#     "Monday": 12, 
#     "Tuesday": 14, 
#     "Wednesday": 15, 
#     "Thursday": 14, 
#     "Friday": 21, 
#     "Saturday":22, 
#     "Sunday":24
# }

# weather_f = {day:int(temp_c * 9/5)+32 for (day,temp_c) in weather_c.items()}
# print(weather_f)