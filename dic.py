cities = {
    "Colombo": 100,
    "Gampaha": 11000,
    "Kandy": 20000,
    "Jaffna": 40000,
    "Galle": 80000,
    "Anuradhapura": 50000,
    "Negombo": 11500,
    "Matara": 81000,
    "Kurunegala": 60000,
    "Ratnapura": 70000,
}

print(cities.keys())
print(cities.values())

print(cities.get("thihagda", "tr"))

del cities["Gampaha"]
print(cities)

cities.clear()
print(cities)
print(cities)
