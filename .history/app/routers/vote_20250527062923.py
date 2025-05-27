from fastapi import APIRouter, Depends, Response, status, HTTPException
from ..import schemas

router = APIRouter(
    prefix = "/vote",
    tags = ['Vote']
    )

@router.post("/", status_code=status.HTTP_201_CREATED)
