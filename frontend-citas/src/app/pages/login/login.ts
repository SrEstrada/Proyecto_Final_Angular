import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Auth } from '../../services/auth';

@Component({
  selector: 'app-login',
  imports: [CommonModule, FormsModule],
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
        this.auth.guardarToken(res.access);
        localStorage.setItem('username', this.username);
        this.mensaje = 'Login exitoso';
        location.href = '/';  // redirigir al inicio
      },
      error: err => this.mensaje = 'Error de login'
    });
  }

}
