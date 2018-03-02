from flask import Flask
from forums import stores, dummy_data
app = Flask("__name__")

member_store = stores.MemberStore()
post_store = stores.PostStore()

from forums.views import *

if __name__ == '__main__':
    dummy_data.seed_stores(member_store, post_store)
    app.run()
