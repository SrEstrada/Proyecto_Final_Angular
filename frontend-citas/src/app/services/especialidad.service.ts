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

  getMedicosPorEspecialidad(especialidadId: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/medicos/?especialidad=${especialidadId}`);
  }
}
