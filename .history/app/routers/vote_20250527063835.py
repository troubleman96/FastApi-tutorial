from fastapi import APIRouter, Depends, Response, status, HTTPException
from ..import schemas, models, database, oauth2

router = APIRouter(
    prefix = "/vote",
    tags = ['Vote']
    )

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db : Session = Depends(database.get))