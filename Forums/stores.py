class MemberStore:
    members = []
    last_id = 1

    def __init__(self):
        pass

    def get_all(self):
        return self.members

    def add(self, member):
        member.id = self.last_id
        self.members.append(member)
        self.last_id += 1

    def get_by_id(self, _id):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.id == _id:
                result = member
                break

        return result

    def entity_exists(self, member):
        # check if member exists or not
        return member in self.get_all()

    def delete(self, _id):
        scan = self.get_by_id(_id)
        self.members.remove(scan)

    def get_by_name(self, member_name):
        all_members = self.get_all()
        all_name = []
        for member in all_members:
            # algorithm for searching by name
            if member_name == member.name:
                all_name.append(member_name)
        return all_name

    def update(self, member):
        member_id = member.id
        for member_re in self.get_all():
            if member_id == member_re.id:
                member_re.name = member.name
                member_re.age = member.age
        return member_re


class PostStore:
    posts = []
    last_id = 1

    def __init__(self):
        pass

    def get_all(self):
        return self.posts

    def add(self, post):
        post.id = self.last_id
        self.posts.append(post)
        post.id += 1

    def get_by_id(self, _id):
        all_posts = self.get_all()
        result = None
        for post in all_posts:
            if post.id == _id:
                result = post
                break
        return result