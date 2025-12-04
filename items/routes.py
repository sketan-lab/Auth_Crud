from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from jose import jwt,JWTError
from dotenv import load_dotenv
from database import  get_db
from items.models import Item
import os
from items.schemas import ItemCreate,ItemOut
# from ..utils.auth import


load_dotenv()
router=APIRouter(prefix='/items',tags=["Items"])


def get_current_user(token:str):
    try:
        payload=jwt.decode(token,os.getenv('SECRET_KEY'),os.getenv('ALGORITHM'))
    except JWTError:
        raise HTTPException(401,'Invalid or Expired Token')


@router.post('/',response_model=ItemOut)
def create_item(item:ItemCreate,db:Session=Depends(get_db)):
    new_item=Item(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.get("/{item_id}",response_model=ItemOut)
def get_items(item_id:int,db:Session=Depends(get_db)):
    item=db.query(Item).filter(Item.id==item_id).first()
    if not item:
        raise HTTPException(404,"Item Not Found")
    return item


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(404, "Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}