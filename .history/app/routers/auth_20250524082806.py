from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from 


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(db: Session = Depends(database.get_db)):