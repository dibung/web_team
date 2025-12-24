from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.db.deps import get_db
from app.crud import result_type as crud
from app.schemas.result_type import ResultTypeCreate, ResultTypeUpdate, ResultTypeResponse
from app.core.error_codes import RESOURCE_NOT_FOUND
from app.core.exception import AppException

router = APIRouter(prefix="/result-types", tags=["ResultTypes"])

@router.post("/", response_model=ResultTypeResponse, status_code=status.HTTP_201_CREATED)
def create_result_type(request: ResultTypeCreate, db: Session = Depends(get_db)):
    return crud.create_result_type(db, request)

@router.get("/", response_model=List[ResultTypeResponse])
def list_result_types(db: Session = Depends(get_db)):
    return crud.get_all_result_types(db)

@router.get("/{result_type_id}", response_model=ResultTypeResponse)
def get_result_type(result_type_id: str, db: Session = Depends(get_db)):
    db_result = crud.get_result_type(db, result_type_id)
    if not db_result:
        raise AppException(**RESOURCE_NOT_FOUND, details={"result_type": result_type_id})
    return db_result

@router.put("/{result_type_id}", response_model=ResultTypeResponse)
def update_result_type(result_type_id: str, request: ResultTypeUpdate, db: Session = Depends(get_db)):
    db_result = crud.update_result_type(db, result_type_id, request)
    if not db_result:
        raise AppException(**RESOURCE_NOT_FOUND, details={"result_type": result_type_id})
    return db_result

@router.delete("/{result_type_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_result_type(result_type_id: str, db: Session = Depends(get_db)):
    result = crud.delete_result_type(db, result_type_id)
    if not result:
        raise AppException(**RESOURCE_NOT_FOUND, details={"result_type": result_type_id})
    return {"ok": True}
