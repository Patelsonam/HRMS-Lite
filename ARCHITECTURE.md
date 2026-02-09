# HRMS Lite - Architecture Documentation

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER BROWSER                          │
│                 (http://localhost:3000)                  │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ HTTP/HTTPS
                       │
┌──────────────────────▼──────────────────────────────────┐
│                  REACT FRONTEND                          │
│              (Vite + Tailwind CSS)                       │
│                                                          │
│  ┌────────────────────────────────────────────────┐     │
│  │  Pages:                                        │     │
│  │  - Employee Management                         │     │
│  │  - Attendance Management                       │     │
│  └────────────────────────────────────────────────┘     │
│                                                          │
│  ┌────────────────────────────────────────────────┐     │
│  │  Components:                                   │     │
│  │  - Navigation                                  │     │
│  │  - Loading                                     │     │
│  │  - Alert                                       │     │
│  └────────────────────────────────────────────────┘     │
│                                                          │
│  ┌────────────────────────────────────────────────┐     │
│  │  Services:                                     │     │
│  │  - API Client (Axios)                         │     │
│  └────────────────────────────────────────────────┘     │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ REST API (JSON)
                       │
┌──────────────────────▼──────────────────────────────────┐
│                 FASTAPI BACKEND                          │
│              (http://localhost:8000)                     │
│                                                          │
│  ┌────────────────────────────────────────────────┐     │
│  │  Routers:                                      │     │
│  │  - /api/employees/                            │     │
│  │  - /api/attendance/                           │     │
│  └────────────────────────────────────────────────┘     │
│                                                          │
│  ┌────────────────────────────────────────────────┐     │
│  │  Business Logic:                               │     │
│  │  - CRUD Operations                             │     │
│  │  - Validation (Pydantic)                       │     │
│  │  - Error Handling                              │     │
│  └────────────────────────────────────────────────┘     │
│                                                          │
│  ┌────────────────────────────────────────────────┐     │
│  │  Data Access:                                  │     │
│  │  - SQLAlchemy ORM                             │     │
│  │  - Database Models                             │     │
│  └────────────────────────────────────────────────┘     │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ SQL Queries
                       │
┌──────────────────────▼──────────────────────────────────┐
│               POSTGRESQL DATABASE                        │
│                                                          │
│  ┌─────────────────┐    ┌─────────────────┐            │
│  │   employees     │    │   attendance    │            │
│  ├─────────────────┤    ├─────────────────┤            │
│  │ id (PK)         │    │ id (PK)         │            │
│  │ employee_id     │◄───┤ employee_id(FK) │            │
│  │ full_name       │    │ date            │            │
│  │ email           │    │ status          │            │
│  │ department      │    │ created_at      │            │
│  │ created_at      │    │                 │            │
│  └─────────────────┘    └─────────────────┘            │
└─────────────────────────────────────────────────────────┘
```

## 📊 Request Flow

### Example: Creating an Employee

```
1. User fills form in EmployeeManagement.jsx
   ↓
2. Form submission triggers handleSubmit()
   ↓
3. employeeAPI.create(formData) called
   ↓
4. Axios POST request to /api/employees/
   ↓
5. FastAPI receives request
   ↓
6. Pydantic validates EmployeeCreate schema
   ↓
7. Router checks for duplicates
   ↓
8. CRUD function creates database record
   ↓
9. SQLAlchemy commits transaction
   ↓
10. PostgreSQL stores data
   ↓
11. Success response (201 Created)
   ↓
12. Frontend updates UI
   ↓
13. Alert shows success message
```

## 🔄 Data Flow Diagram

```
Frontend State → API Call → Backend Validation → Database
     ↑                                               ↓
     └──────── Response ← JSON ← ORM Model ←────────┘
```

## 🗂️ Directory Structure Explained

### Backend Structure

```
backend/
├── app/
│   ├── __init__.py          # Package initializer
│   ├── main.py              # FastAPI app, CORS, routes
│   ├── database.py          # DB connection, session
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   └── routers/
│       ├── __init__.py
│       ├── employees.py     # Employee endpoints
│       └── attendance.py    # Attendance endpoints
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── .gitignore              # Git ignore rules
```

**Key Files:**

- **main.py**: Application entry point, middleware setup
- **database.py**: Database connection and session management
- **models.py**: ORM models (tables definition)
- **schemas.py**: Request/response validation
- **crud.py**: Reusable database queries
- **routers/**: API endpoints organized by resource

### Frontend Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Navigation.jsx   # Top navbar
│   │   ├── Loading.jsx      # Loading state
│   │   └── Alert.jsx        # Notifications
│   ├── pages/
│   │   ├── EmployeeManagement.jsx
│   │   └── AttendanceManagement.jsx
│   ├── services/
│   │   └── api.js           # API configuration
│   ├── App.jsx              # Root component
│   ├── main.jsx             # React entry
│   └── index.css            # Global styles
├── public/                  # Static assets
├── package.json             # Dependencies
├── vite.config.js           # Vite configuration
├── tailwind.config.js       # Tailwind setup
└── .env                     # Environment variables
```

## 🔌 API Endpoints

### Employee Endpoints

| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| POST | /api/employees/ | Create employee | EmployeeCreate | EmployeeResponse (201) |
| GET | /api/employees/ | Get all employees | - | List[EmployeeResponse] (200) |
| GET | /api/employees/{id} | Get specific employee | - | EmployeeResponse (200) |
| DELETE | /api/employees/{id} | Delete employee | - | Message (200) |

### Attendance Endpoints

| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| POST | /api/attendance/ | Mark attendance | AttendanceCreate | AttendanceResponse (201) |
| GET | /api/attendance/ | Get all attendance | - | List[AttendanceResponse] (200) |
| GET | /api/attendance/employee/{id} | Get employee attendance | - | List[AttendanceResponse] (200) |

## 🔒 Error Handling Strategy

### Frontend
```javascript
try {
  await employeeAPI.create(data);
  showAlert('success', 'Employee added');
} catch (error) {
  const message = error.response?.data?.detail || 'Failed';
  showAlert('error', message);
}
```

### Backend
```python
# Validation errors → 400
raise HTTPException(status_code=400, detail="Invalid data")

# Not found → 404
raise HTTPException(status_code=404, detail="Employee not found")

# Duplicate → 409
raise HTTPException(status_code=409, detail="Already exists")

# Server errors → 500
raise HTTPException(status_code=500, detail="Server error")
```

## 🎨 Component Hierarchy

```
App
├── Navigation
└── Router
    ├── EmployeeManagement
    │   ├── Alert
    │   ├── Loading (conditional)
    │   └── Employee Form (conditional)
    │       └── Table
    └── AttendanceManagement
        ├── Alert
        ├── Loading (conditional)
        ├── Attendance Form (conditional)
        └── Table
```

## 🔐 Security Considerations

### Frontend
- Input sanitization
- Client-side validation
- HTTPS in production
- Environment variables for API URL

### Backend
- CORS configuration
- SQL injection prevention (ORM)
- Input validation (Pydantic)
- Environment variables for secrets
- PostgreSQL parameter binding

## 📦 Technology Stack Rationale

### Why FastAPI?
- **Performance**: Built on Starlette (async)
- **Documentation**: Automatic OpenAPI/Swagger
- **Type Safety**: Python type hints
- **Validation**: Built-in with Pydantic
- **Modern**: Python 3.9+ features

### Why React?
- **Component-Based**: Reusable UI components
- **Virtual DOM**: Efficient updates
- **Ecosystem**: Large library ecosystem
- **Developer Experience**: Hot reload, dev tools

### Why PostgreSQL?
- **ACID Compliance**: Data integrity
- **Relational**: Perfect for HR data
- **Reliable**: Battle-tested
- **Free**: Open-source

### Why Tailwind CSS?
- **Utility-First**: Fast development
- **Responsive**: Mobile-first design
- **Customizable**: Easy to extend
- **Small Bundle**: Unused CSS purged

## 🔄 Development Workflow

```
1. Frontend Development
   └─ npm run dev (port 3000)
   
2. Backend Development
   └─ uvicorn --reload (port 8000)
   
3. Database Development
   └─ PostgreSQL (port 5432)
   
4. Testing
   └─ Manual testing via UI
   └─ API testing via /docs
   
5. Deployment
   └─ Git push
   └─ Auto-deploy (Railway + Vercel)
```

## 🚀 Production Deployment

```
Development          Staging           Production
    ↓                   ↓                 ↓
localhost:3000     →   preview.url   →  your-app.vercel.app
localhost:8000     →   staging.url   →  your-app.railway.app
```

## 📈 Scalability Considerations

### Current (Single Server)
- Suitable for 100-1000 users
- Single database instance
- No caching layer

### Future Enhancements
- Add Redis for caching
- Load balancer for multiple instances
- Database replication
- CDN for static assets
- Background job queue

## 🧪 Testing Strategy

### Manual Testing
- UI functionality
- Form validation
- Error handling
- Responsive design

### Suggested Automated Tests
- Unit tests (pytest for backend)
- Integration tests (API endpoints)
- Component tests (React Testing Library)
- E2E tests (Playwright/Cypress)

## 📊 Performance Optimization

### Frontend
- Code splitting (React.lazy)
- Image optimization
- Minimize bundle size
- Caching strategies

### Backend
- Database indexing
- Query optimization
- Connection pooling
- Response caching

## 🔍 Monitoring & Logging

### Production Monitoring
- Railway: Built-in logs and metrics
- Vercel: Analytics and logs
- Database: Query performance

### Recommended Tools
- Sentry (error tracking)
- LogRocket (session replay)
- Datadog (APM)

---

This architecture provides a solid foundation for an enterprise-grade HRMS system while remaining simple enough for easy maintenance and future enhancements.
