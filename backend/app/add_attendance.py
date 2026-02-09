from database import SessionLocal
from models import Employee, Attendance
from datetime import datetime

db = SessionLocal()
employees = db.query(Employee).all()

today = datetime.now().date()

for emp in employees:
    existing = db.query(Attendance).filter(
        Attendance.employee_id == emp.employee_id,
        Attendance.date == today
    ).first()

    if existing:
        print(f"Attendance for {emp.full_name} today already exists, skipping...")
        continue

    attendance = Attendance(
        employee_id=emp.employee_id,
        date=today,
        status="Present"
    )
    db.add(attendance)
    print(f"Attendance for {emp.full_name} today added")

db.commit()
print("All attendance records added safely!")

# Verify attendance
for emp in employees:
    records = db.query(Attendance).filter(
        Attendance.employee_id == emp.employee_id
    ).all()
    
    print(f"\n{emp.full_name} ({emp.department}) - {emp.email}")
    if records:
        for r in records:
            print(f"  {r.date} : {r.status}")
    else:
        print("  No attendance records found")

db.close()
