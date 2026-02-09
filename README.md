# HRMS Lite - Human Resource Management System

A production-ready, full-stack web application for managing employees and tracking attendance. Built with React, FastAPI, and PostgreSQL.

## 🎯 Features

### Employee Management
- Add new employees with unique Employee ID, name, email, and department
- View all employees in a clean, responsive table
- Delete employees with confirmation
- Duplicate detection for Employee ID and email
- Email format validation

### Attendance Management
- Mark attendance for employees (Present/Absent)
- View attendance records per employee or all employees
- Automatic update if attendance already exists for a date
- Filter attendance by employee
- Clean, intuitive UI with status badges

## 🛠️ Tech Stack

### Frontend
- **React 18** with Vite
- **React Router** for navigation
- **Tailwind CSS** for styling
- **Axios** for API communication

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **PostgreSQL** - Production database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## 📁 Project Structure

```
hrms-lite/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── routers/      # API endpoints
│   │   ├── models.py     # Database models
│   │   ├── schemas.py    # Pydantic schemas
│   │   ├── crud.py       # Database operations
│   │   ├── database.py   # DB configuration
│   │   └── main.py       # App entry point
│   └── requirements.txt
├── frontend/             # React frontend
│   ├── src/
│   │   ├── components/   # Reusable components
│   │   ├── pages/        # Page components
│   │   └── services/     # API service
│   └── package.json
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL 12+

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Update `.env` with your PostgreSQL credentials:
```
DATABASE_URL=postgresql://username:password@localhost:5432/hrms_lite
```

6. Run the server:
```bash
uvicorn app.main:app --reload
```

Backend will run at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file:
```bash
cp .env.example .env
```

4. Update `.env` with backend URL:
```
VITE_API_URL=http://localhost:8000/api
```

5. Run the development server:
```bash
npm run dev
```

Frontend will run at `http://localhost:3000`

## 🌐 Deployment

### Backend Deployment (Railway)

1. Create account on [Railway](https://railway.app)

2. Install Railway CLI:
```bash
npm install -g @railway/cli
```

3. Login and deploy:
```bash
cd backend
railway login
railway init
railway up
```

4. Add PostgreSQL database:
- Go to Railway dashboard
- Click "New" → "Database" → "PostgreSQL"
- Railway will automatically set `DATABASE_URL` environment variable

5. Your backend will be deployed at: `https://your-app.railway.app`

### Frontend Deployment (Vercel)

1. Create account on [Vercel](https://vercel.com)

2. Install Vercel CLI:
```bash
npm install -g vercel
```

3. Deploy:
```bash
cd frontend
vercel
```

4. Set environment variable in Vercel dashboard:
- Go to Project Settings → Environment Variables
- Add `VITE_API_URL` with your Railway backend URL

5. Your frontend will be deployed at: `https://your-app.vercel.app`

## 📚 API Documentation

Once backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Key Endpoints

#### Employees
- `POST /api/employees/` - Create employee
- `GET /api/employees/` - Get all employees
- `GET /api/employees/{employee_id}` - Get specific employee
- `DELETE /api/employees/{employee_id}` - Delete employee

#### Attendance
- `POST /api/attendance/` - Mark attendance
- `GET /api/attendance/` - Get all attendance records
- `GET /api/attendance/employee/{employee_id}` - Get employee attendance

## 🔒 HTTP Status Codes

- `200` - Success
- `201` - Created
- `400` - Bad Request (validation error)
- `404` - Not Found
- `409` - Conflict (duplicate entry)
- `500` - Internal Server Error

## ⚙️ Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@host:port/database
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000/api
```

## 🧪 Testing the Application

### Test Employee Management:
1. Click "Add Employee"
2. Fill in all fields (Employee ID, Name, Email, Department)
3. Click "Add Employee" button
4. Employee appears in the table
5. Try adding duplicate Employee ID - should show error
6. Click "Delete" on an employee - should show confirmation

### Test Attendance Management:
1. Click "Mark Attendance" button
2. Select an employee from dropdown
3. Choose date and status (Present/Absent)
4. Click "Mark Attendance"
5. Record appears in the table
6. Click on employee name button to filter their attendance

## 🎨 Design Decisions

### Why FastAPI?
- Automatic API documentation
- Built-in data validation
- High performance
- Modern Python features

### Why React + Vite?
- Fast development with HMR
- Component-based architecture
- Large ecosystem
- Production-ready builds

### Why PostgreSQL?
- ACID compliance
- Robust and reliable
- Great for relational data
- Free and open-source

### Why Tailwind CSS?
- Utility-first approach
- Fast development
- Small bundle size
- Consistent design

## 📝 Database Schema

### Employee Table
```sql
id: INTEGER (Primary Key)
employee_id: VARCHAR (Unique)
full_name: VARCHAR
email: VARCHAR (Unique)
department: VARCHAR
created_at: TIMESTAMP
```

### Attendance Table
```sql
id: INTEGER (Primary Key)
employee_id: VARCHAR (Foreign Key → employees.employee_id)
date: DATE
status: VARCHAR ('Present' or 'Absent')
created_at: TIMESTAMP
```

## 🔍 Assumptions & Limitations

### Assumptions:
- Single admin user (no authentication required)
- English-only interface
- One attendance record per employee per day
- Employee ID is set at creation and cannot be changed

### Limitations:
- No user authentication/authorization
- No employee profile editing
- No bulk operations
- No export functionality
- No reporting dashboard (can be added as bonus)

## 🐛 Troubleshooting

### Backend won't start:
- Check PostgreSQL is running
- Verify DATABASE_URL in .env
- Ensure all dependencies are installed

### Frontend can't connect to backend:
- Check VITE_API_URL in .env
- Verify backend is running
- Check CORS settings in backend

### Database errors:
- Check PostgreSQL credentials
- Ensure database exists
- Check network connectivity

## 📧 Support

For issues or questions, please create an issue in the repository.

## 📄 License

MIT License - feel free to use this project for learning or production.

---

Built with ❤️ for production-ready HR management
