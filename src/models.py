from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    birth=db.Column(db.String(120), unique=False, nullable=True)
    country=db.Column(db.String(120),unique=False, nullable=True)
    city=db.Column(db.String(120),unique=False, nullable=True)
    url_image=db.Column(db.String(120), unique=False, nullable=True)

    # relacion one to many con tabla User (un usuario puede tener muchos centros)
    friends=db.relationship("Friend",back_populates="user")
    posts=db.relationship("Post",back_populates="user")
    comments=db.relationship("Comment",back_populates="user")


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userfriend_id=db.Column(db.Integer, unique=False, nullable=False)
    username = db.Column(db.String(120), unique=False, nullable=False)
    url_image=db.Column(db.String(120), unique=False, nullable=True)

    # relacion one to many con tabla User (un usuario puede tener muchos centros)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    user=db.relationship("User",back_populates="friends")


class Post(db.Model):
    __tablename__ = 'post'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(120), unique=False, nullable=True)
    user_url_image=db.Column(db.String(120), unique=False, nullable=True)
    text=db.Column(db.String(120), unique=False, nullable=True)
    url_image=db.Column(db.String(120), unique=False, nullable=False)
    datetime=db.Column(db.DateTime,unique=False,nullable=True)
    
    # relacion one to many con tabla User (un usuario puede tener muchos centros)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    user=db.relationship("User",back_populates="posts")

    #relacion many to one con tabla User (un post puede tener muchos comments)
    comments=db.relationship("Comment",back_populates="post")


class Comment(db.Model):
    __tablename__ = 'comment'

    id=db.Column(db.Integer, primary_key=True)
    text=db.Column(db.String(120), unique=False, nullable=True)
    username=db.Column(db.String(120), unique=False, nullable=True)
    datetime=db.Column(db.DateTime,unique=False,nullable=True)
    user_url_image=db.Column(db.String(120), unique=False, nullable=False)

   # relacion one to many con tabla User(un user puede tener muchos comentarios)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    user=db.relationship("User",back_populates="comments")
    # relacion one to many con tabla Post(un post puede tener muchos comentarios)
    post_id=db.Column(db.Integer,db.ForeignKey('post.id'))
    post=db.relationship("Post",back_populates="comments")