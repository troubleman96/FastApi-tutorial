from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import database, schemas, models, utilis


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):

    user = db.query(models.User)
