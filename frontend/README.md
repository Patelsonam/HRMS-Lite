# HRMS Lite - Frontend

React-based frontend application for HRMS Lite.

## 🚀 Quick Start

### Setup

1. Install dependencies:
```bash
npm install
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with your backend API URL
```

3. Run development server:
```bash
npm run dev
```

App runs at `http://localhost:3000`

## 🏗️ Build for Production

```bash
npm run build
```

Preview production build:
```bash
npm run preview
```

## 📁 Project Structure

```
src/
├── components/
│   ├── Navigation.jsx    # Top navigation bar
│   ├── Loading.jsx       # Loading spinner
│   └── Alert.jsx         # Alert/notification component
├── pages/
│   ├── EmployeeManagement.jsx    # Employee CRUD page
│   └── AttendanceManagement.jsx  # Attendance page
├── services/
│   └── api.js           # Axios API configuration
├── App.jsx              # Main app component
├── main.jsx             # React entry point
└── index.css            # Tailwind CSS imports
```

## 🎨 Features

### Employee Management Page
- Add new employees with form validation
- View all employees in responsive table
- Delete employees with confirmation
- Error handling with user-friendly messages
- Empty state when no employees exist

### Attendance Management Page
- Mark attendance for employees
- View all attendance or filter by employee
- Date picker for attendance date
- Status selection (Present/Absent)
- Color-coded status badges
- Empty state when no records exist

## 🔌 API Integration

API calls are centralized in `src/services/api.js`:

```javascript
import { employeeAPI, attendanceAPI } from './services/api';

// Employee operations
await employeeAPI.getAll();
await employeeAPI.create(data);
await employeeAPI.delete(employeeId);

// Attendance operations
await attendanceAPI.mark(data);
await attendanceAPI.getAll();
await attendanceAPI.getByEmployee(employeeId);
```

## ⚙️ Environment Variables

Create `.env` file:

```
VITE_API_URL=http://localhost:8000/api
```

For production (Vercel):
```
VITE_API_URL=https://your-backend.railway.app/api
```

## 🎨 Styling

Uses Tailwind CSS utility classes for styling:

- Professional color palette (blue theme)
- Responsive design
- Hover effects and transitions
- Consistent spacing
- Clean typography

## 🚀 Deployment

### Vercel (Recommended)

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy:
```bash
vercel
```

3. Set environment variables in Vercel dashboard:
- Project Settings → Environment Variables
- Add `VITE_API_URL` with backend URL

### Alternative: Netlify

1. Build the project:
```bash
npm run build
```

2. Deploy `dist` folder to Netlify

3. Set environment variable:
- Site Settings → Environment → Environment variables
- Add `VITE_API_URL`

## 🧩 Components

### Navigation
Top navigation bar with route highlighting.

### Loading
Reusable loading spinner with custom message.

### Alert
Toast-style notifications for success/error messages.

## 📱 Responsive Design

- Mobile-first approach
- Responsive tables
- Touch-friendly buttons
- Optimized for all screen sizes

## 🔍 State Management

Uses React hooks for state management:

- `useState` - Component state
- `useEffect` - Data fetching
- `useLocation` - Route detection

## 🐛 Error Handling

- API errors displayed with Alert component
- Form validation
- Network error handling
- User-friendly error messages

## 📦 Dependencies

### Core
- **React 18** - UI library
- **React Router DOM** - Routing
- **Axios** - HTTP client

### Dev Dependencies
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **PostCSS** - CSS processing
- **Autoprefixer** - CSS vendor prefixes

## 🔧 Development Tips

### Hot Reload
Vite provides instant hot module replacement (HMR) during development.

### Code Organization
- Keep components small and focused
- Use meaningful component names
- Extract reusable logic to custom hooks
- Centralize API calls in services

### Best Practices
- Use PropTypes or TypeScript for type checking
- Add loading states for async operations
- Handle errors gracefully
- Provide user feedback

## 🧪 Testing Locally

1. Start backend server first
2. Verify API_URL in .env matches backend
3. Start frontend development server
4. Test all CRUD operations
5. Check responsive design on different screen sizes

## 🐛 Troubleshooting

**API connection failed:**
- Check backend is running
- Verify VITE_API_URL in .env
- Check browser console for errors

**Build errors:**
- Clear node_modules: `rm -rf node_modules`
- Reinstall: `npm install`
- Clear cache: `npm run build --force`

**Styling not working:**
- Check Tailwind CSS is properly configured
- Verify postcss.config.js exists
- Rebuild: `npm run build`

## 📖 Learn More

- [React Documentation](https://react.dev)
- [Vite Guide](https://vitejs.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [React Router](https://reactrouter.com)
