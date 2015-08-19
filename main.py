
from flask import Flask, request, render_template, redirect, url_for
from flask.ext.mongoengine import MongoEngine

from blog.models import Post

from blog.views import blog_page

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "flask_post"}
app.config["SECRET_KEY"] = "123123123"
app.register_blueprint(blog_page, url_prefix="/blog")

db = MongoEngine(app)


@app.route("/")
def index():
	posts = Post.objects.all()
	return render_template("index.html", posts=posts)

if __name__ == '__main__':
	print "Init MAIN"
	use_debugger = True
	app.run(use_debugger=use_debugger, debug=use_debugger)