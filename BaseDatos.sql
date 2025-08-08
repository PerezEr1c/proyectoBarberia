-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS ProjectBarber;
USE ProjectBarber;

-- Tabla: Barberias
CREATE TABLE barberias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(100),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Tabla: Barberos
CREATE TABLE barberos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    experiencia_anios INT DEFAULT 0,
    especialidad VARCHAR(100),
    id_barberia INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_barberia) REFERENCES barberias(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Tabla: Comentarios
CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_barbero INT NOT NULL,
    cliente_nombre VARCHAR(100),
    contenido TEXT NOT NULL,
    calificacion INT CHECK (calificacion >= 1 AND calificacion <= 5),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_barbero) REFERENCES barberos(id) ON DELETE CASCADE
) ENGINE=InnoDB;
