from sqlalchemy import Column, Integer, String, func, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class Author(Base):
    __tablename__ = "quoteapp_author"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(), nullable=False)
    born_date = Column(String(), nullable=False)
    born_location = Column(String(), nullable=False)
    description = Column(String(), nullable=False)


class Quote(Base):
    __tablename__ = "quoteapp_quote"
    id = Column(Integer, primary_key=True)
    text = Column(String(), nullable=False)
    author_id = Column('author_id', ForeignKey('quoteapp_author.id', ondelete='CASCADE'), nullable=False)



class Tag(Base):
    __tablename__ = "quoteapp_tag"
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)


class QuoteTags(Base):
    __tablename__ = "quoteapp_quote_tags"
    id = Column(Integer, primary_key=True)
    quote_id = Column('quote_id', ForeignKey('quoteapp_quote.id', ondelete='CASCADE'), nullable=False)
    tag_id = Column('tag_id', ForeignKey('quoteapp_tag.id', ondelete='CASCADE'), nullable=False)
