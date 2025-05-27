from fastapi import APIRouter, Depends, Response, status, HTTPException
from ..

router = APIRouter(
    prefix = "/vote",
    tags = ['Vote']
    )

@router.post