from models import *

user1 = Member("user1", 1)
user2 = Member("user2", 2)
post1 = Post("title1","body1")
post2 = Post("title2","body2")
post3 = Post("title3","body3")

user_list = [user1,user2]
post_list =[post1,post2,post3]

for user in user_list:
    print(user)
    for post in post_list:
        print(post)
