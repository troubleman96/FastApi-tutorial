from fastapi import APIRouter, Depends, Response, status, HTTPException

router = APIRouter(
    prefix = "/vote",
    tags = ['Vote']
    )

@router.post    