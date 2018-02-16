class MemberStore:
    def __init__(self):
        pass
    members = []
    last_id = 1

    def get_all(self):
        return self.members

    def add(self, member):
        member.id = self.last_id

        self.members.append(member)

        self.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        for result in all_members:
            if result.id == id:
                return result

    def entity_exists(self, member):
        result = True
        # check if member exists or not
        if member in self.get_all():
            return result

    def delete(self, id):
        scan = self.get_by_id(id)
        self.members.remove(scan)


class PostStore:
    def __init__(self):
        pass
    posts = []

    def get_all(self):
        return self.posts

    def add(self, post):
        self.posts.append(post)