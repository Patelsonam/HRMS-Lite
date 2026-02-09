from sqlalchemy.orm import Session
from sqlalchemy import and_
from app import models, schemas
from datetime import date
from typing import List, Optional

# Employee CRUD Operations
def get_employee_by_employee_id(db: Session, employee_id: str):
    return db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()


def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()


def get_all_employees(db: Session):
    return db.query(models.Employee).order_by(models.Employee.created_at.desc()).all()


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: str):
    db_employee = get_employee_by_employee_id(db, employee_id)
    if db_employee:
        db.delete(db_employee)
        db.commit()
        return True
    return False


# Attendance CRUD Operations
def get_attendance_by_employee(db: Session, employee_id: str):
    return db.query(models.Attendance).filter(
        models.Attendance.employee_id == employee_id
    ).order_by(models.Attendance.date.desc()).all()


def get_attendance_by_employee_and_date(db: Session, employee_id: str, attendance_date: date):
    return db.query(models.Attendance).filter(
        and_(
            models.Attendance.employee_id == employee_id,
            models.Attendance.date == attendance_date
        )
    ).first()


def get_all_attendance(db: Session):
    return db.query(models.Attendance).order_by(models.Attendance.date.desc()).all()


def create_attendance(db: Session, attendance: schemas.AttendanceCreate):
    db_attendance = models.Attendance(**attendance.model_dump())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance


def update_attendance(db: Session, attendance_id: int, status: str):
    db_attendance = db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()
    if db_attendance:
        db_attendance.status = status
        db.commit()
        db.refresh(db_attendance)
        return db_attendance
    return None
