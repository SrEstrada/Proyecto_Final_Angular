import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Nosotros } from './pages/nosotros/nosotros';
import { Especialidades } from './pages/especialidades/especialidades';


export const routes: Routes = [
    { path: '', component: Home },
    { path: 'nosotros', component: Nosotros },
    { path: 'especialidades', component: Especialidades }
];
