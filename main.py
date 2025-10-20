person = {
    "name" : "田中太郎",
    "age" : 25,
    "city" : "東京"
}

print(person["name"])
print(person.get("age"))
print(person.get("email", "なし"))

person["email"] = "tanaka@example.com"
person["age"] = 26