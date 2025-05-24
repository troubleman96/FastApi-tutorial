from fastapi import APIRouter, Depends, status, HTTPException, Response


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")