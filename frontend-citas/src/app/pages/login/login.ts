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
    next: (res: { access: string; refresh: string }) => {
      this.auth.guardarToken(res.access, res.refresh, this.username);
      this.mensaje = 'Login exitoso';
      location.href = '/';
    },
    error: err => {
      console.error('Error login:', err);
      this.mensaje = 'Error de login';
    }
  });
}
}