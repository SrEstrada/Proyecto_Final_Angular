import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-navbar',
  imports: [CommonModule,RouterModule],
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
