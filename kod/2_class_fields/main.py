class Human:
    say = 'Hello!'

class Student(Human):
    ...
    say = 'Please pretty gimme C'

class Professor(Human):
    ...
    # say = 'No'


if __name__ == '__main__':
    h = Human()
    s = Student()
    p = Professor()

    s.say = 'gimme 3'
    p.title = 'PhD'

    print(h.say, s.say, p.say)
    print(h.__dir__(), s.__dict__, p.__dict__)
