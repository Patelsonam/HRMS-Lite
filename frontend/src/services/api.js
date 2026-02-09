import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Employee API calls
export const employeeAPI = {
  getAll: () => api.get('/employees/'),
  getById: (employeeId) => api.get(`/employees/${employeeId}`),
  create: (data) => api.post('/employees/', data),
  delete: (employeeId) => api.delete(`/employees/${employeeId}`),
};

// Attendance API calls
export const attendanceAPI = {
  getAll: () => api.get('/attendance/'),
  getByEmployee: (employeeId) => api.get(`/attendance/employee/${employeeId}`),
  mark: (data) => api.post('/attendance/', data),
};

export default api;
