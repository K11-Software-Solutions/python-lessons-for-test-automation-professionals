import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine("sqlite:///movie.db")

theBase = declarative_base()

class Article(theBase):
    __tablename__ = 'articles'
    id = sa.Column(sa.Integer, primary_key=True)
    comments = sa.relationship("Comment")


class Comment(theBase):
    __tablename__ = 'comments'
    id = sa.Column(sa.Integer, primary_key=True)
    article_id = sa.Column(sa.Integer, sa.ForeignKey('articles.id'))