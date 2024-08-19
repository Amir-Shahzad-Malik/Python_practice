#Assign message to variable
my_hobby = "I love python"
print(my_hobby)
#change value of variable
weather = "weather is rainy today in lahore."
print(weather)
#assigning a name to variable and print some message to that person
name = "uzair"
message1 = f"Hello {name}, would you like to eat pizza at domino, {weather}"
print(message1)
#famous quote
famous_quote = "All the world’s a stage, and all the men and women merely players."
author_name = "William Shakespeare"
quote = f'{author_name} once said, "{famous_quote}"'
print(quote)
#famous person quote2
famous_person = "John Kennedy"
message = "Ask not what your country can do for you; ask what you can do for your country."
print(f'{famous_person} once said, "{message}"')
#variable sum
x, y, z = 5, 10, 15
sum = x+y+z
print(sum)
#variable swap
a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")
#favorite color
favorite_color = "green"
print(favorite_color)
new_color = favorite_color
print(new_color)
# favorite pet
favorite_pet = "Buddy"
print(favorite_pet)
favorite_pet = "Max"
print(f"New favorite_pet: {favorite_pet}")
#observing name error
name = "Sunshine"
print(Sunshine)
#print(f" The variable name contain: {name}")
#print(f" The variable 'sunshine': {sunshine})
print(name)
#reassigning score
score: int = 100
print(f"initial value: {score}")
score: int = 150
print(f"new value: {score}")
#city name
city: str = "Multan"
print(city)
#title case text
text = "python programming"
print(text.title())
#lower case text
mixed_cases: str = "I work In Tehzeeb BAKERS"
print(mixed_cases.lower())
#upper case text
upper_cases: str = "long live pakistan"
print(upper_cases.upper())
#current temperature
temperature = 25
print(f"The current temperature is {temperature} degrees")
#poem
poem: str ="Roses are red,\nViolets are blue, \nSugar is sweet, \nAnd so are you"
print(poem)
#stripping names
name = " Amir "
stripped_name = name.strip()
print(f"Original: {name}")
print(f"Stripped: {stripped_name}")
print(name.rstrip())
print(name.lstrip())

