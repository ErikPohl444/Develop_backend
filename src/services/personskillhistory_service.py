from fastapi import HTTPException
from sqlmodel import Session
from src.models.personskillhistory import PersonSkillHistory
from src.services.generic_return_all_items_service import read_all_items_service


def create_personskillhistory_service(personskillhistory: PersonSkillHistory, session: Session):
    session.add(personskillhistory)
    session.commit()
    session.refresh(personskillhistory)
    return {
        "message": f"PersonSkillHistory {personskillhistory.name} created successfully!",
        "data": personskillhistory
    }


def read_personskillhistory_service(personskillhistory_id: int, session: Session):
    personskillhistory_id = session.get(PersonSkillHistory, personskillhistory_id)
    if not personskillhistory_id:
        raise HTTPException(status_code=404, detail="PersonSkillHistory not found")
    return personskillhistory_id


def read_all_personskillhistories_service(session: Session):
    return read_all_items_service(session, PersonSkillHistory)
