from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import get_db

router = APIRouter(
    prefix="/attendance",
    tags=["attendance"]
)


@router.post("/", response_model=schemas.AttendanceResponse, status_code=status.HTTP_201_CREATED)
def mark_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    """
    Mark attendance for an employee
    """
    # Check if employee exists
    employee = crud.get_employee_by_employee_id(db, attendance.employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID '{attendance.employee_id}' not found"
        )
    
    # Check if attendance already exists for this employee on this date
    existing_attendance = crud.get_attendance_by_employee_and_date(
        db, attendance.employee_id, attendance.date
    )
    if existing_attendance:
        # Update existing attendance
        try:
            updated = crud.update_attendance(db, existing_attendance.id, attendance.status)
            return updated
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An error occurred while updating attendance"
            )
    
    # Create new attendance record
    try:
        return crud.create_attendance(db, attendance)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while marking attendance"
        )


@router.get("/employee/{employee_id}", response_model=List[schemas.AttendanceResponse])
def get_employee_attendance(employee_id: str, db: Session = Depends(get_db)):
    """
    Get all attendance records for a specific employee
    """
    # Check if employee exists
    employee = crud.get_employee_by_employee_id(db, employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID '{employee_id}' not found"
        )
    
    try:
        return crud.get_attendance_by_employee(db, employee_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching attendance records"
        )


@router.get("/", response_model=List[schemas.AttendanceResponse])
def get_all_attendance(db: Session = Depends(get_db)):
    """
    Get all attendance records
    """
    try:
        return crud.get_all_attendance(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching attendance records"
        )
