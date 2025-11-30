# Módulo 5 - Bases de Datos Relacionales (SQL)

## Descripción
Este módulo contiene scripts para trabajar con bases de datos relacionales utilizando SQL.  
Se implementa un modelo simple **Usuarios <-> Tareas**, donde se pueden gestionar usuarios y sus tareas asociadas.  
El objetivo es practicar operaciones básicas de SQL como creación de tablas, inserción, actualización, eliminación y consultas (CRUD).

## Funcionalidades
- **Creación de tablas**: `Usuarios` y `Tareas` con sus relaciones.  
- **CRUD completo**:  
  - Crear usuarios y tareas.  
  - Leer información de usuarios y tareas.  
  - Actualizar datos de usuarios y tareas.  
  - Eliminar registros.  
- Relaciones entre usuarios y sus tareas (uno a muchos).  
- Ejemplos de consultas JOIN y filtros básicos.

## Instrucciones de uso
1. Abrir un gestor de base de datos SQL (MySQL, PostgreSQL, SQLite, etc.).  
2. Ejecutar los scripts en el siguiente orden:  
   1. `01_create_tables.sql` – para crear las tablas.  
   2. `02_insert_data.sql` – para insertar datos de ejemplo.  
   3. `03_queries.sql` – para practicar consultas y operaciones CRUD.  
3. Revisar los resultados de las consultas y verificar que la relación Usuarios <-> Tareas funciona correctamente.

## Mejoras aplicadas
- Código SQL organizado y comentado para facilitar comprensión.  
- Scripts separados por funcionalidad (creación, inserción, consultas).  
- Ejemplos claros de consultas JOIN y filtros.  

## Autor
**Paulina Huentel**
