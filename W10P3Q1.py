attractions = {
    "Kathmandu": "Pashupatinath Temple",
    "Pokhara": "Fewa Lake",
    "Nepalgunj": "Bageshwori Temple",
    "Birgunj": "Birgunj Ghanta Ghar"
}

while True:
    try:
        city = input("Enter a city name: ")
        attraction = attractions[city]
        print(f"The tourist attraction of {city} is {attraction}.")
        break
    except KeyError:
        print(f"Sorry, {city} is not in our database. Please enter a valid city name.")
