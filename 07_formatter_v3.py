""" Component 5: statement formatter v1.0
"""


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("-", "Welcome to the Lucky Unicorn game"))
print()
print(formatter("!", "Congratulations, you got Unicorn"))
print()
print(formatter("*", "Goodbye"))
