import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Nosotros } from './pages/nosotros/nosotros';
import { Login } from './pages/login/login';
import { Register } from './pages/register/register';
import { Especialidades } from './pages/especialidades/especialidades';

export const routes: Routes = [
    { path: '', component: Home },
    { path: 'nosotros', component: Nosotros },
    { path: 'login', component: Login },
    { path: 'register', component: Register },
    { path: 'especialidades', component: Especialidades }
];
