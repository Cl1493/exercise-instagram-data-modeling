import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    user_id = Column(Integer, ForeignKey('profile.id'))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)

    def to_dict(self):
        return {}
    

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    profile = relationship(Users)

    def to_dict(self):
        return {}
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comments.id'))
    user_income_id = Column(Integer)
    post = relationship(Profile)

    def to_dict(self):
        return {}
    
class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250))
    user_name = Column(String(250), ForeignKey('user_name'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comments = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
