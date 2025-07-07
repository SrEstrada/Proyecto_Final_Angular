import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-reservar-cita',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './reservar-cita.html',
  styleUrls: ['./reservar-cita.css']
})
export class ReservarCitaComponent {
  especialidades: string[] = ['Cardiología', 'Dermatología', 'Neurología', 'Pediatría'];
  horarios: string[] = ['09:00', '10:00', '11:00', '12:00', '15:00', '16:00'];
  selectedEspecialidad = '';
  selectedFecha = '';
  selectedHora = '';
  mensaje = '';

  constructor(private http: HttpClient) {}

  reservarCita() {
    if (!this.selectedEspecialidad || !this.selectedFecha || !this.selectedHora) {
      this.mensaje = 'Por favor completa todos los campos.';
      return;
    }

    const cita = {
      especialidad: this.selectedEspecialidad,
      fecha: this.selectedFecha,
      hora: this.selectedHora
    };

    this.http.post('http://localhost:8000/api/citas/', cita).subscribe({
      next: () => {
        this.mensaje = '✅ Cita reservada con éxito.';
      },
      error: (err) => {
        console.error(err);
        this.mensaje = '❌ Ocurrió un error al reservar la cita.';
      }
    });
  }
}

