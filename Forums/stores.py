class MemberStore():
    members = []

    def get_all(self):
        if len(self.members) > 0:
            return self.members
        else:
            return None

    def add(self, member):
        self.members.append(member)


class PostStore(MemberStore):
    posts = []

    def get_all(self):
        if len(self.posts) > 0:
            return self.posts
        else:
            return None

    def add(self, post):
        self.posts.append(post)