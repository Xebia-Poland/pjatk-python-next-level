
def add_person(name, country=[]):
    country.append(name.upper())
    return country

italian = []
german = []

polish = add_person('Janek')
italian = add_person('Alberto')
german = add_person('Dietrich')

print(polish, id(polish))
print(italian, id(italian))
print(german, id(german))
