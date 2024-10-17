# Initial toy collection with two toys
toy_collection = {
    "Teddy Bear": {
        "age_suitability": 3,
        "is_electronic": False
    },
    "Remote Control Car": {
        "age_suitability": 6,
        "is_electronic": True
    }
}

# Adding more toys to the collection
toy_collection["Lego Set"] = {
    "age_suitability": 5,
    "is_electronic": False
}

toy_collection["Drone"] = {
    "age_suitability": 10,
    "is_electronic": True
}

# Find a toy by name
def find_toy(toy_name):
    if toy_name in toy_collection:
        return toy_collection[toy_name]
    else:
        return f"Toy '{toy_name}' is not in the collection."

# Add a new toy to the collection
def add_toy(toy_name, age_suitability, is_electronic):
    if toy_name in toy_collection:
        return f"Toy '{toy_name}' already exists in the collection."
    toy_collection[toy_name] = {
        "age_suitability": age_suitability,
        "is_electronic": is_electronic
    }
    return f"Toy '{toy_name}' has been added to the collection."

# Remove a toy from the collection
def remove_toy(toy_name):
    if toy_name in toy_collection:
        del toy_collection[toy_name]
        return f"Toy '{toy_name}' has been removed from the collection."
    else:
        return f"Toy '{toy_name}' does not exist in the collection."

# List all toys in the collection
def list_toys():
    if toy_collection:
        return list(toy_collection.keys())
    else:
        return "The toy collection is empty."

# Testing the functions

# 1. Finding a toy
print(find_toy("Teddy Bear"))  # Should return the details of 'Teddy Bear'
print(find_toy("Robot"))       # Should indicate 'Robot' is not in the collection

# 2. Adding a new toy
print(add_toy("Robot", 7, True))   # Adding 'Robot' to the collection
print(add_toy("Teddy Bear", 3, False))  # Trying to add an existing toy

# 3. Removing a toy
print(remove_toy("Drone"))     # Should remove 'Drone'
print(remove_toy("Drone"))     # Trying to remove a non-existent toy

# 4. Listing all toys
print(list_toys())  # Should list all remaining toys
