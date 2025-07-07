import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Auth } from '../../services/auth';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class Login {
  username = '';
  password = '';
  mensaje = '';

  constructor(private auth: Auth) {}

  login() {
    this.auth.login({ username: this.username, password: this.password }).subscribe({
      next: (res: any) => {
        // Guarda token y nombre
        this.auth.guardarToken(res.access, this.username);
        this.mensaje = 'Login exitoso';

        // Redirige al home
        location.href = '/';
      },
      error: err => {
        this.mensaje = 'Error de login';
      }
    });
  }
}