import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Nosotros } from './pages/nosotros/nosotros';
import { ReservarCitaComponent } from './features/reservar-cita/reservar-cita';

export const routes: Routes = [
    { path: '', component: Home },
    { path: 'nosotros', component: Nosotros },
    { path: 'reservar-cita', component: ReservarCitaComponent }
];
