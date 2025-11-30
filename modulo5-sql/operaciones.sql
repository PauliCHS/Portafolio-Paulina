-- operaciones.sql
INSERT INTO usuarios (nombre, correo) VALUES ('Paulina Huentel','paulina@example.com');
INSERT INTO usuarios (nombre, correo) VALUES ('Juan Perez','juan@example.com');

INSERT INTO tareas (titulo, descripcion, fecha, estado, id_usuario)
VALUES ('Comprar material', 'Comprar cuadernos', '2025-11-30', 'pendiente', 1);

INSERT INTO tareas (titulo, descripcion, fecha, estado, id_usuario)
VALUES ('Revisar proyecto', 'Revisar entregable', '2025-12-01', 'en progreso', 2);

SELECT * FROM usuarios;
SELECT * FROM tareas;
SELECT t.titulo, u.nombre FROM tareas t JOIN usuarios u ON t.id_usuario = u.id_usuario;

UPDATE tareas SET estado = 'completado' WHERE id_tarea = 1;
DELETE FROM tareas WHERE id_tarea = 2;
