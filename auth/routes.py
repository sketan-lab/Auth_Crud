from fastapi import Depends, APIRouter,HTTPException
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash,check_password_hash
from jose import JWTError,jwt

from database import  get_db
from auth.models import Client
from auth.schemas import UserCreate,UserOut
from utils.auth import Create_Access_Token


router=APIRouter(prefix='/auth',tags=['Auth'])

@router.post('/register',response_model=UserOut)
def register(user: UserCreate,db: Session=Depends(get_db)):
    existing=db.query(Client).filter(Client.username==user.username).first()
    print(existing)
    if existing:
        raise HTTPException(400,'Username Already Exist')

    hashed=generate_password_hash(user.password)
    new_user=Client(username=user.username,password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/login')
def login(user:UserCreate,db: Session=Depends(get_db)):

    db_user=db.query(Client).filter(Client.username==user.username).first()
    if not db_user or not check_password_hash(db_user.password,user.password):
        raise HTTPException(401,'Invalid Credentials')
    token=Create_Access_Token({"sub":db_user.username})

    return {"access_token": token, "token_type": "bearer"}

