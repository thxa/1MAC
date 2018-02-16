import models
import stores


user1 = models.Member("user1", 1)
user2 = models.Member("user2", 2)
post1 = models.Post("title1", "body1")
post2 = models.Post("title2", "body2")
post3 = models.Post("title3", "body3")

user_list = stores.MemberStore()
post_list = stores.PostStore()

user_list.add(user1)
user_list.add(user2)

post_list.add(post1)
post_list.add(post2)
post_list.add(post3)

print(user_list.get_by_id(1))
print(user_list.entity_exists(user1))
user_list.delete(1)
print(user_list.entity_exists(user1))
print(user_list.get_by_id(2))