# Favorite Color Checker

favorite_colors = ["red", "blue", "black", "white"]

user_color = input("Enter a color you like: ").lower()

if user_color in favorite_colors:
    print("Yes! That's one of my favorite colors too.")
else:
    print("Hmm... that's not in my top favorites.")
