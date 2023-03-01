import json

from database.db import session
from database.models import Author


with open('authors.json', 'r', encoding='utf=8') as file:
    data_authors = json.load(file)

with open('quotes.json', 'r', encoding='utf=8') as file:
    data_quotes = json.load(file)


# for item in data_quotes:
#     for tag in item['tags']:
#         print(tag)


# authors = session.query(Author).all()
# for a in authors:
#     if a.fullname == "Alfred Tennyson":
#         print("Found Alfred Tennyson")


value = "Alfred Tennyson"
query = session.query(Author).filter(Author.fullname == value)
exists = session.query(query.exists()).scalar()

if exists:
    print('Alfred Tennyson exists in authors')
else:
    print('Alfred Tennyson does not exist in authors')


# value = "Alfred Tennyson"
# query = session.query(Author.id).filter_by(fullname=value)
# author_id = query.scalar()
#
# print(author_id)
