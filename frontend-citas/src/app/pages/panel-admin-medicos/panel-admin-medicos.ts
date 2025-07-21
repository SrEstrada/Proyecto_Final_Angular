import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { AdminMedicosService, MedicoAdmin } from '../../services/admin-medicos.service';
import { EspecialidadService, Especialidad } from '../../services/especialidad.service';

@Component({
  selector: 'app-panel-admin-medicos',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './panel-admin-medicos.html',
  styleUrls: ['./panel-admin-medicos.css']
})
export class PanelAdminMedicos implements OnInit {

  medicos: MedicoAdmin[] = [];
  especialidades: Especialidad[] = [];

  cargando = true;
  mensaje = '';
  busqueda = '';

  mostrandoFormulario = false;
  modo: 'crear' | 'editar' = 'crear';

  formMedico: any = this.formPorDefecto();

  constructor(
    private svc: AdminMedicosService,
    private espSvc: EspecialidadService
  ) {}

  ngOnInit(): void {
    this.cargarEspecialidades();
    this.cargarMedicos();
  }

  private formPorDefecto() {
    return {
      id: null,
      nombres: '',
      correo: '',
      especialidad: null as number | null
    };
  }

  cargarEspecialidades() {
    this.espSvc.listar().subscribe({
      next: data => this.especialidades = data,
      error: err => console.error('Error cargando especialidades', err)
    });
  }

  cargarMedicos() {
    this.cargando = true;
    this.svc.listar(this.busqueda).subscribe({
      next: data => {
        this.medicos = data;
        this.cargando = false;
      },
      error: err => {
        console.error('Error cargando médicos:', err);
        this.mensaje = 'Error cargando médicos';
        this.cargando = false;
      }
    });
  }

  nombreDeEspecialidad(id: number): string {
    const e = this.especialidades.find(x => x.id === id);
    return e ? e.nombre : `#${id}`;
  }

  buscar() {
    this.cargarMedicos();
  }

  nuevoMedico() {
    this.modo = 'crear';
    this.formMedico = this.formPorDefecto();
    this.mostrandoFormulario = true;
  }

  editarMedico(m: MedicoAdmin) {
    this.modo = 'editar';
    this.formMedico = { ...m };
    this.mostrandoFormulario = true;
  }

  cancelarFormulario() {
    this.mostrandoFormulario = false;
    this.formMedico = this.formPorDefecto();
    this.modo = 'crear';
  }

  guardarMedico() {
    if (this.modo === 'crear') {
      this.svc.crear(this.formMedico).subscribe({
        next: () => {
          this.mensaje = 'Médico creado.';
          this.cancelarFormulario();
          this.cargarMedicos();
        },
        error: err => {
          console.error('Error creando médico:', err);
          this.mensaje = 'Error creando médico.';
        }
      });
    } else {
      this.svc.actualizar(this.formMedico.id, this.formMedico).subscribe({
        next: () => {
          this.mensaje = 'Médico actualizado.';
          this.cancelarFormulario();
          this.cargarMedicos();
        },
        error: err => {
          console.error('Error actualizando médico:', err);
          this.mensaje = 'Error actualizando médico.';
        }
      });
    }
  }

  eliminarMedico(m: MedicoAdmin) {
    if (!confirm(`¿Eliminar al médico "${m.nombres}"?`)) return;
    this.svc.eliminar(m.id).subscribe({
      next: () => {
        this.mensaje = 'Médico eliminado.';
        this.cargarMedicos();
      },
      error: err => {
        console.error('Error eliminando médico:', err);
        this.mensaje = 'Error eliminando médico.';
      }
    });
  }
}