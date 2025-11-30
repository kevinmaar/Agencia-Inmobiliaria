-- 1) crear DB y usarla (cambia el nombre si ya usas otra)
CREATE DATABASE IF NOT EXISTS inmobiliaria CHARACTER SET = utf8mb4 COLLATE = utf8mb4_uca1400_ai_ci;
USE inmobiliaria;

DROP TABLE IF EXISTS direccion_agencia;
DROP TABLE IF EXISTS propietario;
DROP TABLE IF EXISTS agencia_inmobiliaria;

CREATE TABLE agencia_inmobiliaria (
  ID_AGENCIA INT PRIMARY KEY,
  RFC VARCHAR(13) NOT NULL UNIQUE,
  TELEFONO VARCHAR(15)
) ENGINE=InnoDB;

CREATE TABLE direccion_agencia (
    ID_AGENCIA INT NOT NULL,
    CALLE VARCHAR(50) NOT NULL,
    NUMERO VARCHAR(10) NOT NULL,
    CP CHAR(5) NOT NULL,
    POBLACION VARCHAR(50) NOT NULL,
    PRIMARY KEY (CALLE, NUMERO, CP, POBLACION)
) ENGINE=InnoDB;

CREATE TABLE propietario (
    DNI_PROPIETARIO VARCHAR(20) PRIMARY KEY,
    TELEFONO VARCHAR(15),
    EMAIL VARCHAR(50) UNIQUE,
    NOMBRE VARCHAR(40) NOT NULL,
    APELLIDO_PATERNO VARCHAR(40) NOT NULL,
    APELLIDO_MATERNO VARCHAR(40) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE direccion_propietario (
    DNI_PROPIETARIO VARCHAR(20) NOT NULL,
    CALLE VARCHAR(50) NOT NULL,
    NUMERO VARCHAR(10) NOT NULL,
    CP CHAR(5) NOT NULL,
    POBLACION VARCHAR(50) NOT NULL,
    PRIMARY KEY (CALLE, NUMERO, CP, POBLACION)
) ENGINE=InnoDB;

CREATE TABLE inquilino (
    DNI_INQUILINO VARCHAR(20) PRIMARY KEY,
    TELEFONO VARCHAR(15),
    FECHA_NACIMIENTO DATE NOT NULL,
    NOMBRE VARCHAR(40) NOT NULL,
    APELLIDO_PATERNO VARCHAR(40) NOT NULL,
    APELLIDO_MATERNO VARCHAR(40) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE vivienda (
    ID_VIVIENDA INT PRIMARY KEY,
    DESCRIPCION VARCHAR(200),
    ID_AGENCIA INT,
    DNI_PROPIETARIO VARCHAR(20) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE direccion_vivienda (
    ID_VIVIENDA INT NOT NULL,
    CALLE VARCHAR(50) NOT NULL,
    NUMERO VARCHAR(10) NOT NULL,
    CP CHAR(5) NOT NULL,
    POBLACION VARCHAR(50) NOT NULL,
    PRIMARY KEY (CALLE, NUMERO, CP, POBLACION)
) ENGINE=InnoDB;

CREATE TABLE alquiler (
    ID_ALQUILER INT PRIMARY KEY,
    FECHA_FIRMA DATE NOT NULL,
    FECHA_INICIO DATE NOT NULL,
    FECHA_FIN DATE NOT NULL,
    IMPORTE_MENSUAL DECIMAL(10,2) NOT NULL,
    FIANZA DECIMAL(10,2),
    ID_VIVIENDA INT NOT NULL,
    DNI_INQUILINO VARCHAR(20) NOT NULL,
    ID_ALQUILER_PADRE INT NULL,
    CONSTRAINT chk_importe CHECK (IMPORTE_MENSUAL > 0),
    CONSTRAINT chk_fianza CHECK (FIANZA >= 0)
) ENGINE=InnoDB;


ALTER TABLE direccion_agencia
ADD CONSTRAINT fk_dir_agencia
FOREIGN KEY (ID_AGENCIA)
REFERENCES agencia_inmobiliaria(ID_AGENCIA)
ON DELETE CASCADE;

ALTER TABLE direccion_propietario
ADD CONSTRAINT fk_dir_propietario
FOREIGN KEY (DNI_PROPIETARIO)
REFERENCES propietario(DNI_PROPIETARIO)
ON DELETE CASCADE;

ALTER TABLE vivienda
ADD CONSTRAINT fk_viv_agencia
FOREIGN KEY (ID_AGENCIA)
REFERENCES agencia_inmobiliaria(ID_AGENCIA)
ON DELETE SET NULL;

ALTER TABLE vivienda
ADD CONSTRAINT fk_viv_propietario
FOREIGN KEY (DNI_PROPIETARIO)
REFERENCES propietario(DNI_PROPIETARIO);

ALTER TABLE direccion_vivienda
ADD CONSTRAINT fk_dir_vivienda
FOREIGN KEY (ID_VIVIENDA)
REFERENCES vivienda(ID_VIVIENDA)
ON DELETE CASCADE;

ALTER TABLE alquiler
ADD CONSTRAINT fk_alq_vivienda
FOREIGN KEY (ID_VIVIENDA)
REFERENCES vivienda (ID_VIVIENDA)
ON DELETE RESTRICT;

ALTER TABLE alquiler
ADD CONSTRAINT fk_alq_inquilino
FOREIGN KEY (DNI_INQUILINO)
REFERENCES inquilino (DNI_INQUILINO)
ON DELETE RESTRICT;

ALTER TABLE alquiler
ADD CONSTRAINT fk_alq_renovacion
FOREIGN KEY (ID_ALQUILER_PADRE)
REFERENCES alquiler (ID_ALQUILER)
ON DELETE SET NULL;


ALTER TABLE agencia_inmobiliaria 
MODIFY ID_AGENCIA INT AUTO_INCREMENT;

ALTER TABLE vivienda 
MODIFY ID_VIVIENDA INT AUTO_INCREMENT;

ALTER TABLE alquiler 
MODIFY ID_ALQUILER INT AUTO_INCREMENT;



CREATE OR REPLACE VIEW v_alquiler_duracion AS
SELECT
    alquiler.ID_ALQUILER,
    alquiler.FECHA_INICIO,
    alquiler.FECHA_FIN,
    alquiler.ID_ALQUILER_PADRE,

    (
        WITH RECURSIVE cadena AS (
            SELECT 
                ID_ALQUILER,
                FECHA_INICIO,
                ID_ALQUILER_PADRE
            FROM alquiler
            WHERE ID_ALQUILER = alquiler.ID_ALQUILER

            UNION ALL

            SELECT 
                alquiler.ID_ALQUILER,
                alquiler.FECHA_INICIO,
                alquiler.ID_ALQUILER_PADRE
            FROM alquiler
            JOIN cadena ON alquiler.ID_ALQUILER = cadena.ID_ALQUILER_PADRE
        )
        SELECT MIN(FECHA_INICIO) FROM cadena
    ) AS FECHA_INICIO_ORIGINAL,

    DATEDIFF(
        alquiler.FECHA_FIN,
        (
            WITH RECURSIVE cadena AS (
                SELECT 
                    ID_ALQUILER,
                    FECHA_INICIO,
                    ID_ALQUILER_PADRE
                FROM alquiler
                WHERE ID_ALQUILER = alquiler.ID_ALQUILER

                UNION ALL

                SELECT 
                    alquiler.ID_ALQUILER,
                    alquiler.FECHA_INICIO,
                    alquiler.ID_ALQUILER_PADRE
                FROM alquiler
                JOIN cadena ON alquiler.ID_ALQUILER = cadena.ID_ALQUILER_PADRE
            )
            SELECT MIN(FECHA_INICIO) FROM cadena
        )
    ) AS DURACION_TOTAL

FROM alquiler;



/* DATOS DE PRUEBA: */

/*Agencia*/
INSERT INTO agencia_inmobiliaria (ID_AGENCIA, RFC, TELEFONO) VALUES
(1, 'AIX230101ABC', '2288123456'),
(2, 'BRM210506XYZ', '2281654321'),
(3, 'CJV190923KLM', '2288421098'),
(4, 'DLT200731PRS', '2288997744'),
(5, 'EMS180215QWE', '2281203040');

/*Direccion de agencia*/ 
INSERT INTO direccion_agencia (ID_AGENCIA, CALLE, NUMERO, CP, POBLACION) VALUES
(1, 'Av. Araucarias', '120', '91190', 'Xalapa'),
(2, 'Av. Ruiz Cortines', '301', '91020', 'Xalapa'),
(3, 'Av. Américas', '455', '91110', 'Xalapa'),
(4, 'Calle Enríquez', '18', '91000', 'Xalapa'),
(5, 'Av. 20 de Noviembre', '240', '91064', 'Xalapa');

/*Propietario*/
INSERT INTO propietario (DNI_PROPIETARIO, TELEFONO, EMAIL, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO) VALUES
('PROPXA01', '2289001122', 'jmendez@gmail.com', 'Juan', 'Méndez', 'Ortega'),
('PROPXA02', '2288776655', 'laura.rivas@yahoo.com', 'Laura', 'Rivas', 'Torres'),
('PROPXA03', '2288124500', 'carlos.soto@outlook.com', 'Carlos', 'Soto', 'Ramírez'),
('PROPXA04', '2288452211', 'paola.martinez@gmail.com', 'Paola', 'Martínez', 'Luna'),
('PROPXA05', '2289988776', 'andres.giron@hotmail.com', 'Andrés', 'Girón', 'Hernández');

/*Direccion Propietario*/
INSERT INTO direccion_propietario (DNI_PROPIETARIO, CALLE, NUMERO, CP, POBLACION) VALUES
('PROPXA01', 'Calle Lázaro Cárdenas', '45', '91180', 'Xalapa'),
('PROPXA02', 'Paseo de los Lagos', '12', '91060', 'Xalapa'),
('PROPXA03', 'Calle Ignacio Zaragoza', '210', '91030', 'Xalapa'),
('PROPXA04', 'Av. Rebsamen', '701', '91130', 'Xalapa'),
('PROPXA05', 'Calle Sayago', '88', '91040', 'Xalapa');

/*Inquilino*/
INSERT INTO inquilino (DNI_INQUILINO, TELEFONO, FECHA_NACIMIENTO, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO) VALUES
('INQXA01', '2288801122', '1995-03-12', 'Miguel', 'Pérez', 'Ruiz'),
('INQXA02', '2288507788', '1999-08-21', 'Diana', 'Lopez', 'Cruz'),
('INQXA03', '2288223300', '1988-11-05', 'Roberto', 'Aguilar', 'Santos'),
('INQXA04', '2288445566', '2000-01-30', 'Sara', 'Jiménez', 'Marín'),
('INQXA05', '2288991100', '1993-06-14', 'Fernanda', 'Torres', 'Paredes');

/*Vivienda*/
INSERT INTO vivienda (ID_VIVIENDA, DESCRIPCION, ID_AGENCIA, DNI_PROPIETARIO) VALUES
(101, 'Departamento cerca de Plaza Américas', 1, 'PROPXA01'),
(102, 'Casa de 2 pisos en Zona Centro', 2, 'PROPXA02'),
(103, 'Departamento en Rebsamen, 3 habitaciones', 3, 'PROPXA03'),
(104, 'Casa amplia en colonia Obrero Campesina', 4, 'PROPXA04'),
(105, 'Loft moderno cerca de la USBI', 5, 'PROPXA05');

/*Direccion vivienda*/
INSERT INTO direccion_vivienda (ID_VIVIENDA, CALLE, NUMERO, CP, POBLACION) VALUES
(101, 'Av. Américas', '350', '91110', 'Xalapa'),
(102, 'Calle Revolución', '102', '91000', 'Xalapa'),
(103, 'Av. Rebsamen', '650', '91130', 'Xalapa'),
(104, 'Calle Ávila Camacho', '55', '91050', 'Xalapa'),
(105, 'Calle Camino a la USBI', '20', '91090', 'Xalapa');

/*Alquiler*/
INSERT INTO alquiler (ID_ALQUILER, FECHA_FIRMA, FECHA_INICIO, FECHA_FIN, IMPORTE_MENSUAL, FIANZA, ID_VIVIENDA, DNI_INQUILINO, ID_ALQUILER_PADRE) VALUES
(1, '2023-01-10', '2023-02-01', '2024-02-01', 8500.00, 8500.00, 101, 'INQXA01', NULL),
(2, '2023-05-15', '2023-06-01', '2024-06-01', 9500.00, 9000.00, 102, 'INQXA02', NULL),
(3, '2024-03-01', '2024-03-15', '2025-03-15', 7800.00, 7800.00, 103, 'INQXA03', NULL),
(4, '2022-02-20', '2022-03-01', '2023-03-01', 7000.00, 7000.00, 104, 'INQXA04', NULL),
(5, '2023-02-15', '2023-03-01', '2024-03-01', 7200.00, 7000.00, 104, 'INQXA04', 4);

/*Borrar todo
DELETE FROM alquiler;
DELETE FROM direccion_vivienda;
DELETE FROM vivienda;
DELETE FROM inquilino;
DELETE FROM direccion_propietario;
DELETE FROM propietario;
DELETE FROM direccion_agencia;
DELETE FROM agencia_inmobiliaria;
*/


/*Crear trigger*/
DELIMITER //
CREATE TRIGGER trg_validar_fechas_alquiler
BEFORE INSERT ON alquiler
FOR EACH ROW
BEGIN
    IF NEW.FECHA_FIN <= NEW.FECHA_INICIO THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La fecha de fin debe ser mayor que la fecha de inicio.';
    END IF;
END //
DELIMITER ;

