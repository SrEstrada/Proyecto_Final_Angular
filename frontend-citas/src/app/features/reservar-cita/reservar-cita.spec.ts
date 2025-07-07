import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReservarCita } from './reservar-cita';

describe('ReservarCita', () => {
  let component: ReservarCita;
  let fixture: ComponentFixture<ReservarCita>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ReservarCita]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ReservarCita);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
