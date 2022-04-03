import re

easter_string = input()
regex = r"[@|#]+(?P<color>[a-z]{3,})[@|#]+\W*[/]+(?P<amount>\d+)[/]+"
easter_eggs = {}

result = re.finditer(regex, easter_string)
for egg in result:
    egg_color = egg.group("color")
    egg_count = int(egg.group("amount"))
    print(f"You found {egg_count} {egg_color} eggs!")
