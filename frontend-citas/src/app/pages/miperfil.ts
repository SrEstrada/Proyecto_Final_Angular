import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Auth } from '../../services/auth';

@Component({
  standalone:true,
  selector: 'app-miperfil',
  imports: [CommonModule, HttpClientModule],
  templateUrl: './miperfil.html',
  styleUrl: './miperfil.css',
})
export class Miperfil implements OnInit {
  usuario: any = null;
  error = '';

  constructor(private auth: Auth) {}

  ngOnInit() {
    this.auth.obtenerUsuario().subscribe({
      next: (data) => {
        this.usuario = data;
      },
      error: (err) => {
        this.error = 'No se pudo cargar la información del usuario';
        console.error(err);
      }
    });
  }
}
