import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class MyEnum(enum.Enum):
    reels = 1
    post = 2
    historias = 3


class User (Base):
        __tablename__ = 'User'
        id = Column(Integer, primary_key=True)
        username = Column(String(250), nullable=False)
        firstname = Column(String(250), nullable=False)
        lastname = Column(String(250), nullable=False)
        email= Column(String(250))
        

        def to_dict(self):
            return {}


class Post(Base):
        __tablename__ = 'Post'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('User.id'))

        def to_dict(self):
            return {}
        
        
class Media(Base):
      __tablename__ = "Media"
      id = Column(Integer, primary_key=True)
      typo = Column (Enum(MyEnum),nullable=False )
      url = Column (String (250))
      post_id = Column (Integer, ForeignKey('Post.id'))

      def to_dict(self):
            return {}
      

class Comment (Base):
        __tablename__ = "Comment"
        id = Column(Integer, primary_key=True)
        comment_text = Column (Enum(MyEnum),nullable=False )
        author_id = Column (Integer, ForeignKey ('User.id'))
        post_id = Column (Integer, ForeignKey('Post.id'))

        def to_dict(self):
            return {}


class Followers (Base):
      __tablename__ = "Followers"
      id = Column(Integer, primary_key=True)
      user_from_id = Column (Integer, ForeignKey ('User.id'))
      user_to_id = Column (Integer, ForeignKey ('User.id'))

      def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
