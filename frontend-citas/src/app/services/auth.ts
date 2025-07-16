import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class Auth {
  private apiUrl = '/api';

  constructor(private http: HttpClient) {}

  login(credentials: { username: string; password: string }) {
    return this.http.post<{ access: string }>(`${this.apiUrl}/login/`, credentials, {
      withCredentials: true
    }).pipe(
      tap(response => {
        this.guardarToken(response.access, credentials.username);
      })
    );
  }

  register(data: { username: string; password: string; email: string }) {
    return this.http.post(`${this.apiUrl}/register/`, data, {
      withCredentials: true
    });
  }

  guardarToken(token: string, username: string) {
    localStorage.setItem('token', token);
    localStorage.setItem('username', username);
  }

  obtenerToken(): string | null {
    return localStorage.getItem('token');
  }

  obtenerNombreUsuario(): string | null {
    return localStorage.getItem('username');
  }

  cerrarSesion() {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
  }

  estaAutenticado(): boolean {
    return !!this.obtenerToken();
  }
}