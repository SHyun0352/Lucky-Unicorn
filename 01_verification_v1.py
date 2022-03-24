check_played = input("Have you played this game before? (yes/no): ").lower()

if check_played == "yes":
    print("Processing the game")

elif check_played == "no":
    print("Show instruction")

else:
    print("Please enter valid answer. (yes/no)")
