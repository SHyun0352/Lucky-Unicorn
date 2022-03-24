"""
convert answer to lower case, accepting abbreviations as answer.
"""
check_played = input("Have you played this game before? (yes/no): ").lower()

if check_played == "yes" or check_played == "y":
    print("Processing the game")

elif check_played == "no" or check_played == "n":
    print("Show instruction")

else:
    print("Please enter valid answer. (yes/no)")

print(f"You have chosen {check_played}.")
