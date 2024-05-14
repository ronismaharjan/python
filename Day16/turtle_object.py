import turtle
import prettytable
table = prettytable.PrettyTable()
pokemon = {
    "Pikachu": "Electric",
    "Squirtal": "Water",
    "Charmander": "Fire",
    "Blastoid": "Water"
}
pokemon_names = []
pokemon_types = []
for name in pokemon:
    pokemon_names.append(name)
    pokemon_types.append(pokemon[name])


table.add_column("Pokemon", pokemon_names)
table.add_column("Types", pokemon_types)
table.align = "l"
print(table)

# tinny = turtle.Turtle()
# my_screen = turtle.Screen()
# print(my_screen.window_height())
# print(my_screen.window_width())
# tinny.shape("turtle")
# tinny.color("coral")
# tinny.speed(1)
# tinny.forward(100)

# my_screen.exitonclick()
