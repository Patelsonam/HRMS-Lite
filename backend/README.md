# HRMS Lite - Backend API

FastAPI-based REST API for HRMS Lite application.

## 🚀 Quick Start

### Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your database URL
```

4. Run the server:
```bash
uvicorn app.main:app --reload
```

Server runs at `http://localhost:8000`

## 📚 API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🗃️ Database

### Create PostgreSQL Database

```bash
# Login to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE hrms_lite;

# Exit
\q
```

### Environment Variable

```
DATABASE_URL=postgresql://username:password@localhost:5432/hrms_lite
```

## 🧱 Project Structure

```
app/
├── __init__.py
├── main.py           # FastAPI app initialization
├── database.py       # Database configuration
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas
├── crud.py           # Database operations
└── routers/
    ├── employees.py  # Employee endpoints
    └── attendance.py # Attendance endpoints
```

## 🔌 API Endpoints

### Employee Management

**Create Employee**
```http
POST /api/employees/
Content-Type: application/json

{
  "employee_id": "EMP001",
  "full_name": "John Doe",
  "email": "john@example.com",
  "department": "IT"
}
```

**Get All Employees**
```http
GET /api/employees/
```

**Get Employee by ID**
```http
GET /api/employees/{employee_id}
```

**Delete Employee**
```http
DELETE /api/employees/{employee_id}
```

### Attendance Management

**Mark Attendance**
```http
POST /api/attendance/
Content-Type: application/json

{
  "employee_id": "EMP001",
  "date": "2024-02-09",
  "status": "Present"
}
```

**Get All Attendance**
```http
GET /api/attendance/
```

**Get Employee Attendance**
```http
GET /api/attendance/employee/{employee_id}
```

## ⚙️ Configuration

### CORS

CORS is enabled for all origins in development. For production, update `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🚀 Deployment

### Railway

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login and deploy:
```bash
railway login
railway init
railway up
```

3. Add PostgreSQL:
- Dashboard → New → Database → PostgreSQL
- DATABASE_URL is set automatically

### Alternative: Render

1. Create account on Render.com
2. New Web Service → Connect repository
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add PostgreSQL database
6. Set DATABASE_URL environment variable

## 🧪 Testing

Test with curl:

```bash
# Health check
curl http://localhost:8000/health

# Create employee
curl -X POST http://localhost:8000/api/employees/ \
  -H "Content-Type: application/json" \
  -d '{
    "employee_id": "EMP001",
    "full_name": "John Doe",
    "email": "john@example.com",
    "department": "IT"
  }'

# Get all employees
curl http://localhost:8000/api/employees/
```

## 🔒 Error Handling

The API returns appropriate HTTP status codes:

- `200` - Success
- `201` - Resource created
- `400` - Validation error
- `404` - Resource not found
- `409` - Duplicate resource
- `500` - Server error

Error response format:
```json
{
  "detail": "Error message here"
}
```

## 📦 Dependencies

- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **SQLAlchemy** - ORM
- **Pydantic** - Data validation
- **psycopg2-binary** - PostgreSQL adapter
- **python-dotenv** - Environment variables
- **email-validator** - Email validation

## 🐛 Troubleshooting

**Database connection failed:**
- Check PostgreSQL is running
- Verify DATABASE_URL format
- Check database exists

**Import errors:**
- Activate virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

**CORS errors:**
- Check allow_origins in main.py
- Verify frontend URL is correct
