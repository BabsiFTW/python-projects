"""
Mad Libs are poems, where the user should add words to!
"""

# The template for the story

print("Mad Libs has started!")
name = raw_input("Enter a name: ")
adj_one = raw_input("Enter the first adjective: ")
adj_two = raw_input("Enter the second adjective: ")
adj_three = raw_input("Enter the third adjective: ")
required_verb = raw_input("Enter a verb: ")
noun_one = raw_input("Enter the first noun: ")
noun_two = raw_input("Enter the second noun: ")
required_animal = raw_input("Please enter an animal: ")
required_food = raw_input("Please enter a food: ")
required_fruit = raw_input("Please enter fruit: ")
required_superhero = raw_input("Please enter a superhero: ")
required_country = raw_input("Please enter a country: ")
required_dessert = raw_input("Please enter a dessert: ")
required_year = raw_input("Please enter a year: ")

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s s ruled the world." % (name, adj_one, adj_two, required_animal, required_food, required_verb, noun_one, required_fruit, adj_three, name, required_superhero, name, required_country, name, required_dessert, name, required_year, noun_two)

print(STORY)
print("Mad Libs has ended!")
