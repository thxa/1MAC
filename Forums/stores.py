class MemberStore():
    members = []

    def get_all(self):
        if len(MemberStore.members) > 0:
            for get in MemberStore.members:
                print(get)
        else:
            print(None)

    def add(self, member):
        MemberStore.members.append(member)


class PostStore(MemberStore):
    posts = []

    def get_all(self):
        if len(PostStore.posts) > 0:
            for get in PostStore.posts:
                print(get)
        else:
            print(None)

    def add(self, post):
        PostStore.posts.append(post)
