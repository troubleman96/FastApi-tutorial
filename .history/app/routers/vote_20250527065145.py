from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from ..import schemas, models, database, oauth2

router = APIRouter(
    prefix = "/vote",
    tags = ['Vote']
    )

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db : Session = Depends(database.get_db),
          current_user : int = Depends(oauth2.get_current_user)):

        vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, 
                                                  models.Vote.user_id == current_user.id)
        found_vote = vote_query.first()

     if(vote.dir == 1):
          if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CO)