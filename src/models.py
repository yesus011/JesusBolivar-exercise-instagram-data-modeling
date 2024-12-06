import os 
import sys 
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Enum 
from sqlalchemy.orm import relationship, declarative_base 
from sqlalchemy import create_engine 
from eralchemy2 import render_er 
from datetime import datetime


Base = declarative_base() 

class User(Base):
     __tablename__ = 'user' 
     id = Column(Integer, primary_key=True)
     username = Column(String(50), nullable=False, unique=True) 
     email = Column(String(80), nullable=False, unique=True) 
     password = Column(String(100), nullable=False) 
     firstname =  Column(String(50)) 
     lastname = Column(String(50)) 
      
     
class Post(Base): 
     __tablename__ = 'post' 
     id = Column(Integer, primary_key=True) 
     user_id = Column(Integer, ForeignKey('user.id'), nullable=False) 
     content = Column(Text, nullable=False) 
    
     user = relationship(User, back_populates='posts') 
     
class Comment(Base): 
    __tablename__ = 'comment' 
    id = Column(Integer, primary_key=True) 
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False) 
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False) 
    content = Column(Text, nullable=False) 
    
    user = relationship(User)
    post = relationship(Post) 
    
class Like(Base):
     __tablename__ = 'like'
     id = Column(Integer, primary_key=True) 
     post_id = Column(Integer, ForeignKey('post.id'), nullable=False) 
     user_id = Column(Integer, ForeignKey('user.id'), nullable=False) 
      
     user = relationship(User)
     post = relationship(Post) 
     
class Follower(Base):
     __tablename__ = 'follower'
     id = Column(Integer, primary_key=True) 
     user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
     user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False) 
    
     user_from = relationship(User, foreign_keys=[user_from_id])
     user_to = relationship(User, foreign_keys=[user_to_id])
    


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
