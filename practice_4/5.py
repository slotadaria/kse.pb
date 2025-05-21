people = {
    "Anna": "Kyiv",
    "Bohdan": "Lviv",
    "Oksana": "Kyiv",
    "Dmytro": "Odesa"
}
names = people.keys()
cities = set(people.values())
new_dic = {}
for i in cities:
  new_dic[i] = []
for key, value in people.items():
  new_dic [value].append(key)
print(new_dic)