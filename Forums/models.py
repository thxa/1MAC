class Member:
    def __init__(self, name , age):

        self.name = name
        self.age = age


    def info(self):
        distance(35)
        print("Name:%s \nAge:%d " %(self.name , self.age))


class Post:

    def __init__(self,title , body):
        self.title = title
        self.body = body


    def info(self):
        distance(34)
        print("title: %s\nbody: %s" %(self.title, self.body))


def distance(x):
    print("-" * x)