class Member:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        distance(14)
        return "Name:%s\nAge:%d" % (self.name, self.age)


class Post:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __str__(self):
        distance(14)
        return "Title: %s\nBody: %s" % (self.title, self.body)


def distance(x):
    print("-" * x)