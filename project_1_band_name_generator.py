'''Concatenate two strings.'''

print("Welcome to the Band Name Generator!")

# ask the user, city and pet's name
city = input("What is the name of the city where you grew up? ")
pet_name = input("What is your pet's name? ")

# concatenate the strings to form the band name
band_name = city + pet_name
print(f"Your band name could be {band_name}.")
