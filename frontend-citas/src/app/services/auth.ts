import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class Auth {
  private apiUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  login(credentials: { username: string; password: string }) {
    return this.http.post(`${this.apiUrl}/login/`, credentials, { withCredentials: true });
  }

  register(data: { username: string; password: string; email: string }) {
    return this.http.post(`${this.apiUrl}/register/`, data, { withCredentials: true });
  }

  guardarToken(token: string) {
    localStorage.setItem('token', token);
  }

  obtenerToken() {
    return localStorage.getItem('token');
  }

  cerrarSesion() {
    localStorage.removeItem('token');
  }
}