# 📘 Requisitos del Sistema

---

## 1. Requisitos Funcionales

### RF01 - Registro de socios 
El sistema debe permitir registrar nuevos socios ingresando nombre, DNI, dirección y teléfono.  

**Prioridad:** Alta  
**Criterio de aceptación:**  
Se valida que los campos obligatorios no estén vacíos y que el socio se guarde correctamente en la base de datos.

---

### RF02 - Registro de libros
El sistema debe permitir registrar nuevos libros con su título, autor y categoría.  

**Prioridad:** Alta  
**Criterio de aceptación:**  
Se confirma que el libro se guarda y aparece disponible en la lista.

---

### RF03 - Registro de préstamos
El sistema debe permitir registrar préstamos de libros a socios registrados.  

**Prioridad:** Alta  
**Criterio de aceptación:**  
El préstamo se registra y el libro cambia su estado a “prestado”.

---

### RF04 - Registro de devoluciones y multas
El sistema debe permitir registrar devoluciones de libros y calcular multas por retraso.  

**Prioridad:** Media  
**Criterio de aceptación:**  
La multa se calcula correctamente según los días de retraso.

---

### RF05 - Autenticación de usuarios
El sistema debe permitir la autenticación de usuarios (bibliotecarios y administradores).  

**Prioridad:** Alta  
**Criterio de aceptación:**  
Solo usuarios con credenciales válidas pueden ingresar.

---

## 2. Requisitos No Funcionales

### RNF01 - Rendimiento
El sistema debe responder en menos de 2 segundos a las consultas de libros.  

**Criterio de aceptación:**  
Durante las pruebas, se mide el tiempo de respuesta promedio y debe ser menor a 2 segundos.

---

### RNF02 - Seguridad 
Las contraseñas de los usuarios deben almacenarse cifradas.  

**Criterio de aceptación:**  
Se verifica que las contraseñas se guarden con un algoritmo de hash seguro.

---

### RNF03 - Disponibilidad 
El sistema debe estar disponible durante el horario de atención (8:00 a 20:00).  

**Criterio de aceptación:**  
El sistema se mantiene operativo durante el horario establecido.

---

### RNF04 - Usabilidad 
La interfaz debe ser intuitiva y fácil de usar para el personal no técnico.  

**Criterio de aceptación:**  
El personal puede realizar tareas sin necesidad de capacitación técnica adicional.

---

### RNF05 - Escalabilidad  
La base de datos debe permitir el acceso concurrente de al menos 10 usuarios.  

**Criterio de aceptación:**  
Se prueba el acceso simultáneo de 10 usuarios sin pérdida de rendimiento.

---
