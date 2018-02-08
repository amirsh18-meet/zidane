from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True

db = SQLAlchemy(app)


class Comment(db.Model):
	id= db.Column(db.Integer, primary_key=True, autoincrement=True)
	text = db.Column(db.String(200), nullable=False)
	def __repr__(self):
		return 'Comment %r' % self.text

db.create_all()

@app.route('/comment', methods=['GET', 'POST'])
def comment():
	if request.method=='POST':
		new_comment=Comment()
		print(1)
		new_comment.text = request.form.get('comment')
		print(2)
		db.session.add(new_comment)
		print(3)
		db.session.commit()
		print(4)
		all_comments = Comment.query.all()
		return render_template('heart.html', all_comments=all_comments)

	elif request.method=='GET':
		return render_template('heart.html')

@app.route('/')
def heart():
	return render_template('heart.html')


@app.route('/france')
def france():
    return render_template('france.html')

@app.route('/juventus')
def juventus():
    return render_template('juventus.html')

@app.route('/realmadrid')
def realmadrid():
    return render_template('realmadrid.html')

@app.route('/cannes')
def cannes():
    return render_template('cannes.html')

@app.route('/bordeaux')
def bordeaux():
    return render_template('bordeaux.html')

@app.route('/awards2')
def awards2():
    return render_template('awards2.python')

if __name__ == '__main__':
	app.run(debug=True)