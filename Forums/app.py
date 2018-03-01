from flask import Flask, render_template
import dummy_data
app = Flask("__name__")

post_story = dummy_data.post_story


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=post_story.get_all())


if __name__ == '__main__':
    app.run()
