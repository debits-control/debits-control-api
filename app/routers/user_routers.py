from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.factory.user_factory import user_factory
from app.schema.user_schema import User, UserCreate

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get('', response_model=list[User])
async def get_user_list(
        session: Session = Depends(get_db)
):
    service = user_factory(session)
    return service.get_list()


@router.post('', response_model=User)
async def create_user(
        user: UserCreate,
        session: Session = Depends(get_db)
):
    service = user_factory(session)
    return service.add(user)


@router.post('/{user_id}', response_model=User)
async def get_user_by_id(
        user_id: int,
        session: Session = Depends(get_db)
):
    service = user_factory(session)
    return service.get_by_id(user_id)
