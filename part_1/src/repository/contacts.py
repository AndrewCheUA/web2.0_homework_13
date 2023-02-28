from datetime import datetime, timedelta
from typing import List

from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel


async def create_contact(body: ContactModel,user: User, db: Session):
    contact = Contact(**body.dict(), user_id=user.id)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def get_contacts(user: User, db: Session):
    contacts = db.query(Contact).filter(Contact.user_id == user.id).all()
    return contacts


async def get_contact(contact_id: int, user: User, db: Session):
    contact = db.query(Contact).filter_by(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    return contact


async def update_contact(body: ContactModel, contact_id: int, user: User, db: Session):
    contact = db.query(Contact).filter_by(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.additional_info = body.additional_info
        db.commit()
    return contact


async def remove_contact(contact_id: int, user: User, db: Session):
    contact = db.query(Contact).filter_by(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def search_field(field_to_search: str, user: User, db: Session):
    contacts_list = []
    contacts_all = db.query(Contact).filter(Contact.user_id == user.id).all()
    for contact in contacts_all:
        if field_to_search.capitalize() in contact.name.capitalize() and contact not in contacts_list:
            contacts_list.append(contact)
        if field_to_search.capitalize() in contact.surname.capitalize() and contact not in contacts_list:
            contacts_list.append(contact)
        if field_to_search.capitalize() in contact.email.capitalize() and contact not in contacts_list:
            contacts_list.append(contact)

    return contacts_list


async def birthday_list(user: User, db: Session):
    contacts_list = []
    dt_now = datetime.now()
    now_year = datetime.now().strftime('%Y')
    contacts_all = db.query(Contact).filter(Contact.user_id == user.id).all()
    for contact in contacts_all:
        delta = contact.birthday.replace(year=int(now_year)) - dt_now
        if timedelta(days=-1) < delta < timedelta(days=7):
            contacts_list.append(contact)
    return contacts_list
