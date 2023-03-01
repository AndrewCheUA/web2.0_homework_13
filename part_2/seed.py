import json

from database.db import session
from database.models import Author, Quote, Tag, QuoteTags

with open('authors.json', 'r', encoding='utf=8') as file:
    data_authors = json.load(file)

with open('quotes.json', 'r', encoding='utf=8') as file:
    data_quotes = json.load(file)


def seed_authors():
    for item in data_authors:
        author = Author(
            fullname=item['fullname'],
            born_date=item['born_date'],
            born_location=item['born_location'],
            description=item['bio']
        )
        session.add(author)
    session.commit()


def seed_quotes():
    for item in data_quotes:
        value = item['author']
        query = session.query(Author.id).filter_by(fullname=value)
        author_id = query.scalar()
        quote = Quote(
            text=item['quote'],
            author_id=author_id,
        )
        session.add(quote)
    session.commit()


def seed_tags():
    for item in data_quotes:
        for tag in item['tags']:
            query = session.query(Tag).filter(Tag.name == tag)
            exists = session.query(query.exists()).scalar()
            if not exists:
                tag_ps = Tag(
                    name=tag,
                )
                session.add(tag_ps)
    session.commit()


def seed_quote_tags():
    for item in data_quotes:
        query = session.query(Quote.id).filter_by(text=item["quote"])
        quote_id = query.scalar()
        for tag in item['tags']:
            query = session.query(Tag.id).filter_by(name=tag)
            tag_id = query.scalar()
            quote_tag = QuoteTags(
                quote_id=quote_id,
                tag_id=tag_id
            )
            session.add(quote_tag)
    session.commit()


if __name__ == '__main__':
    seed_quote_tags()
