from flask import Flask, render_template
from Forums import models
from Forums import stores
app = Flask("__name__")

post_story = stores.PostStore()
post_story.add(models.Post("Life", "Life is alawys  great"))
post_story.add(models.Post("Sunshine", "Sunshine is amazing"))


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=post_story.get_all())


if __name__ == '__main__':
    app.run()
