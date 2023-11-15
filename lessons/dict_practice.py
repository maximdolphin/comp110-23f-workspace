"""Practice with dictionary syntax."""

ice_cream: dict[str, int] = {"Chocolate": 12, "Vanilla": 8, "Strawberry": 5}

ice_cream["Mint"] = 3
print("Added mint to the dictionary:")
print(ice_cream)
ice_cream.pop("Mint")
print("Removed mint:")
print(ice_cream)

print(f"There are {ice_cream['Chocolate']} orders of chocolate")
ice_cream["Vanilla"] += 2
print("Added 2 orders of vanilla to the dictionary:")
print(ice_cream["Vanilla"])

print(len(ice_cream))

if "Chocolate" in ice_cream:
    print("Chocolate is in ice cream")
else: 
    print("Chocolate is not in ice cream")

for orders in ice_cream:
    print(ice_cream[orders])
