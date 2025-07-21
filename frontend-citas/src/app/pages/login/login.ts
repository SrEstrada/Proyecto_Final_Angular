import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Auth } from '../../services/auth';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class Login {
  username = '';
  password = '';
  mensaje = '';

  constructor(private auth: Auth, private router: Router) {}

  login() {
    this.auth.login({ username: this.username, password: this.password }).subscribe({
      next: (resp: { rol: string }) => {
        // resp.rol viene de obtenerRol() (switchMap en el servicio)
        const rol = resp.rol || 'Paciente';
        localStorage.setItem('rol', rol); // redundante, pero seguro

        this.mensaje = 'Login exitoso';

        // Redirigir según rol
        if (rol === 'Administrador') {
          this.router.navigate(['/panel-admin']);
        } else {
          this.router.navigate(['/panel-paciente']);
        }
      },
      error: err => {
        console.error('Error login:', err);
        this.mensaje = 'Error de login';
      }
    });
  }
}