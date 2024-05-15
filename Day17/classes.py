# The name of first leeter of class should be capital its called PascalCase
class User:
    """creating a user"""

    def __init__(self, username, user_id):
        self.username = username
        self.id = user_id

    def details(self):
        print(f"{self.username}, {self.id}")


# Initialize the class
user1 = User("hel", 2)
user1.details()

# Adding attributes for class from outside of the class
print(user1.username)
print(user1.id)
# Creating the constructor
# format : def __init__(self):
