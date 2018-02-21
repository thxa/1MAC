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
        # algorithm for searching by name
        return (member for member in all_members if member.name == member_name)

    def update(self, member):
        all_member = self.get_all()
        member_id = member.id
        for index, e in enumerate(all_member):
            if e.id == member_id:
                all_member[index] = member

    def get_members_with_posts(self, all_posts):
        all_member = self.get_all()
        for member in all_member:
            for post in all_posts:
                if member.id == post.member_id:
                    member.posts.append(post)
        return all_member

    def get_top_two(self, all_posts):
        all_posts_s = self.get_members_with_posts(all_posts)
        all_members = self.get_all()
        all_post = sorted(all_members, key=lambda top: len(top.posts), reverse=True)
        return all_post[:2]


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