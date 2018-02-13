import models

user1 = models.Member("user1", 1)
user2 = models.Member("user2", 2)
post1 = models.Post("title1","body1")
post2 = models.Post("title2","body2")
post3 = models.Post("title3","body3")

user_list = [user1,user2]
post_list =[post1,post2,post3]

for user in user_list:
    print(user)
    for post in post_list:
        print(post)
