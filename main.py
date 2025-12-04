from fastapi import FastAPI
from database import base,engine
from auth.routes import router as auth_router
from items.routes import router as item_router

base.metadata.create_all(bind=engine)

app=FastAPI()


app.include_router(auth_router)
app.include_router(item_router)