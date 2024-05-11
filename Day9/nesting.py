# Nesting dictionaries within a dictionary
capital = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting lists in a dictionary
travel_log = [
    {
        "country":"france", 
        "visits":2, 
        "cities":["Paris", "Lille", "Dijon"]

    }, 
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin", "Hamburg", "Stuttgart"]
    }
]

#Function to add country in list in dict form
def add_new_country(country_name, visits, places):
    
    new_dictionary = {}
    new_dictionary["country"] = country_name
    new_dictionary["visits"] = visits
    new_dictionary["places"] = places
    travel_log.append(new_dictionary)
     
     or
    travel_log.append({
        "country":country_name,
        "visits": visits, 
        "places":places
    })


add_new_country("Russia", 2, ["Moscow", "Saint"])

# Printing the travel_log
print(travel_log)
