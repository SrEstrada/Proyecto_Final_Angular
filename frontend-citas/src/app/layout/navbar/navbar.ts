import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-navbar',
  imports: [CommonModule],
  templateUrl: './navbar.html',
  styleUrl: './navbar.css'
})
export class Navbar {
  get usuarioLogueado(): boolean {
    return localStorage.getItem('token') !== null;
  }
  get nombreUsuario(): string {
    return localStorage.getItem('username') || '';
  }
  cerrarSesion() {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    location.reload();
  }

}
