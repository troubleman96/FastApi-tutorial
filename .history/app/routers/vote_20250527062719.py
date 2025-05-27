from fastapi import APIRouter, Depends, Response, status, HTTPException
from ..import schemas

router = APIRouter(
    prefix = "/vote",
    tags = ['Vote']
    )

@router.post()