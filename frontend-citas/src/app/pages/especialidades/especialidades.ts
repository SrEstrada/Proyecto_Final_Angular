import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { EspecialidadService } from '../../services/especialidad.service';

@Component({
  selector: 'app-especialidades',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './especialidades.html',
  styleUrls: ['./especialidades.css']
})
export class Especialidades implements OnInit {
  especialidades: any[] = [];
  medicos: any[] = [];
  especialidadSeleccionada: number = 0;

  constructor(private servicio: EspecialidadService) {}

  ngOnInit(): void {
    this.servicio.getEspecialidades().subscribe(data => {
      this.especialidades = data;
    });
  }

  buscarMedicos(): void {
    if (this.especialidadSeleccionada) {
      this.servicio.getMedicosPorEspecialidad(this.especialidadSeleccionada).subscribe(data => {
        this.medicos = data;
      });
    } else {
      this.medicos = [];
    }
  }
}
