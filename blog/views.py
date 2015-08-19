from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import Post
from mongoengine import ValidationError

blog_page = Blueprint('blog', __name__)

@blog_page.route("/create", methods=['POST'])
def create():
	try:
		post = Post()
		post.title = request.form['title']
		post.save()
		flash("Post created!", 'success')
	except ValidationError as validation:
		msg = validation.to_dict()
		print msg
		print dir(msg)
		for field in msg.viewkeys():
			flash(field + ": "+ msg[field], 'error')

	return redirect(url_for("index"))

@blog_page.route("/delete/<string:post_id>")
def delete(post_id):
	print "Delete: " + post_id
	Post.objects.get(id= post_id).delete()
	return redirect(url_for("index"))
