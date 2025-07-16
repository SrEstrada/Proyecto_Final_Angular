import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EspecialidadService {
  private baseUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getEspecialidades(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/especialidades/`);
  }

  getMedicosPorEspecialidad(id: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/medicos/?especialidad=${id}`);
  }
  crearEspecialidad(nombre: string): Observable<any> {
  return this.http.post(`${this.baseUrl}/especialidades/crear/`, {
    nombre
  });
  }
  eliminarEspecialidad(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/especialidades/${id}/eliminar/`);
  }
  editarEspecialidad(id: number, nombre: string): Observable<any> {
    return this.http.put(`${this.baseUrl}/especialidades/${id}/editar/`, { nombre });
  }
  confirmarEliminar(id: number) {
    if (confirm('¿Seguro que quieres eliminar esta especialidad?')) {
      this.eliminarEspecialidad(id);
    }
  }
}
