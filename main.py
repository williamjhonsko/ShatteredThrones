
#### main.py

```python
#!/usr/bin/env python3
import random

empires = [
    "The Sunken Kingdom of Ilmora – Destroyed when the sea claimed its cities, but its golden crown remains hidden beneath the waves.",
    "The Ashen Empire – Ruled the world before being consumed by firestorms, leaving behind the Eternal Scepter.",
    "The Shadow Dynasty – Vanished overnight, leaving only their cursed obsidian thrones behind.",
    "The Stormborn Dominion – A powerful empire that fell after angering the gods, now only its thunderforged weapons remain.",
    "The Ivory Keep – Once a beacon of knowledge, now only the Tome of Lost Kings survives."
]

def get_random_empire():
    return random.choice(empires)

def main():
    print("Welcome to Shattered Thrones!")
    print("Here is a randomly generated fallen empire and its relic:")
    print(get_random_empire())

if __name__ == "__main__":
    main()
