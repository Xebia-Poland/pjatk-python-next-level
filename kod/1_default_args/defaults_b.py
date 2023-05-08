
def add_person(name, country=None):
    if country is None:
        country = []
    country.append(name.upper())
    return country

italian = []
german = []


polish = add_person('janek')
italian = add_person('Tomaso')
german = add_person('Dietrich')

print(polish, id(polish))
print(italian, id(italian))
print(german, id(german))
