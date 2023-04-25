color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

color1_difference = list(set(color1) - set(color2))
color2_difference = list(set(color2) - set(color1))

print("Color1-Color2:", color1_difference)
print("Color2-Color1:", color2_difference)
