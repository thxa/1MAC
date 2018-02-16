class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name:%s\nAge:%d" % (self.name, self.age)


class Post:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __str__(self):
        return "Title: %s\nBody: %s" % (self.title, self.body)
