# UNIVERSIDAD NACIONAL DE SAN AGUSTÍN DE AREQUIPA  
## FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS  
### ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS  

---

### 🧑‍🏫 **Asignatura:** Programación Web II  
### 👨‍🏫 **Docente:** Ing. Corrales Delgado, Carlo Jose Luis 
### 📘 **Tema:** Proyecto final (Aplicación Web de Citas Médicas)

---

### 👥 **Integrantes:**
  
- Estrada Arce, Sergio Emilio  
- Mamani Quispe, Renzo Geomar  
- Schreiber Landeo, Diego Hans  
- Tijero Dávila, Lucciano Valentino  

---

📍 **Arequipa - Perú**  
📅 **2025**

# 🏥 Aplicación Web de Citas Médicas

## 📌 Descripción

Sistema completo de gestión de citas médicas desarrollado con Django en el backend y Angular en el frontend. La aplicación permite a los pacientes registrarse, reservar citas, consultar su historial, y a los administradores gestionar médicos, pacientes, especialidades y horarios.

Proyecto desarrollado para el curso de Desarrollo Web con Frameworks - Semestre 2025-I.

---

## 🧩 Estructura del Proyecto

- **Frontend:** Angular (`frontend-citas/`)
- **Backend:** Django + REST Framework (`clinica/`)
- **Base de Datos:** SQLite (modo desarrollo) - PostgreSQL (render)
- **Despliegue:** Render.com con HTTPS

---

## ✅ Funcionalidades Implementadas

### 🌐 Estructura general

- Aplicación web dividida en frontend y backend
- URL propias con uso de `reverse()` en Django 
- Plantillas personalizadas para login, vistas administrativas y públicas 
- Formularios con widgets elegantes y validaciones 

### 🔁 CRUD Completo

- **Especialidades**: Crear, editar, listar y eliminar
- **Pacientes**: Listado y eliminación
- **Médicos**: Crear, editar, listar y eliminar
- **Horarios de médicos**: CRUD embebido en el módulo de médicos
- **Citas**: CRUD completo desde el panel del administrador y desde el perfil del paciente 

### 🔒 Seguridad

- Autenticación basada en JWT (login/register)
- Restricciones por rol (administrador/paciente)
- Protección CSRF, validación de formularios, y token en cabeceras 

### 📦 API REST y JSON

- Endpoints protegidos por JWT para administradores y pacientes
- Vista de consulta que devuelve datos en JSON (`/api/paciente/citas/`, `/api/especialidades-con-medicos/`) 

### ⚙️ AJAX + Framework JS

- Operaciones CRUD asíncronas usando `HttpClient` de Angular
- Consumo de APIs con Angular + manejo de estado de carga 

### 📚 Modelos

- Modelo de Especialidad
- Modelo de Médico (ForeignKey a Especialidad)
- Modelo de Cita (ForeignKey a Médico y Paciente) 

### 🎨 Diseño

- Uso de **Bootstrap 5** para interfaz limpia y responsive 
- Tablas, formularios y tarjetas adaptadas a pantallas pequeñas

### 🌐 Despliegue en la Web

- Aplicación desplegada con dominio HTTPS en [Render](https://proyecto-final-5fj4.onrender.com/) 

---

## 🔧 Tecnologías Usadas

| Backend         | Frontend        | Otras herramientas          |
|-----------------|-----------------|-----------------------------|
| Django          | Angular         | Bootstrap 5                 |
| Django REST     | RxJS            | Render (hosting)            |
| SQLite          | HTML/CSS        | Git + GitHub                |
| JWT Auth        | TypeScript      |                             |

---

## 📂 Rutas Principales

| Vista                    | URL                              | Rol         |
|--------------------------|----------------------------------|-------------|
| Inicio                   | `/`                              | Público     |
| Login                    | `/login`                         | Público     |
| Registro                 | `/register`                      | Público     |
| Panel de Paciente        | `/panel-paciente`                | Paciente    |
| Perfil de Paciente       | `/perfil`                        | Paciente    |
| Panel de Administrador   | `/panel-admin`                   | Admin       |
| Médicos                  | `/panel-admin-medicos`           | Admin       |
| Especialidades           | `/panel-admin-especialidades`    | Admin       |
| Citas                    | `/panel-admin-citas`             | Admin       |



## 📄 Funcionalidades Opcionales Completadas

- [x] Publicación en la web con HTTPS 
- [x] Uso de dominio render.com 
- [x] Modelo con ForeignKey (Cita → Médico / Paciente) 
- [x] Envío de correos electrónicos 

---

## 📤 Despliegue

- 🌐 [Página en Render](https://proyecto-final-5fj4.onrender.com/)

---

## 📥 Instrucciones de Instalación (Local)

```bash
# Clonar repositorio
git clone https://github.com/SrEstrada/Proyecto_Final_Angular.git
cd Proyecto_Final_Angular

# BACKEND
cd backend-citas
python -m venv env
source env/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# FRONTEND
cd ../frontend-citas
npm install
ng serve