# Proyecto: Inmobiliaria Xalapa

Aplicación en **Python** para la gestión de una **agencia inmobiliaria**.  
El proyecto está organizado en un modelo de **tres capas**: [dominio](https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/dominio), [persistencia](https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/persistencia) y [ui](https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/ui). Incluye menús por consola y operaciones CRUD para viviendas, propietarios, inquilinos, direcciones y alquileres.

---

## Tabla de contenido
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación y ejecución](#instalación-y-ejecución)
- [Base de datos](#base-de-datos)
- [Autor](#autor)

---

## Estructura del proyecto

```
proyectoBD/
  ├─ dominio/        # Clases del modelo (Agencia, Propietario, Vivienda, etc.)
  ├─ persistencia/   # Conexión a la base de datos y consultas SQL
  └─ ui/Main.py      # Punto de entrada del programa, menús y lógica de interacción con el usuario       
```

---

## Requisitos

Instalar MariaDB Connector para Python:

```bash
pip install mariadb
```

---

## Instalación y ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/kevinmaar/Inmobiliaria-Xalapa.git
```

2. Entrar al proyecto:
```bash
cd proyectoBD
```

3. Ejecutar el programa:
```bash
python Main.py
```

---

## Base de datos

El sistema usa una base de datos relacional inicialmente gestionada con [mariaDB](https://mariadb.org/)

El siguiente diagrama entidad-relacion muestra cómo se relacionan las tablas de la base de datos, incluyendo llaves primarias y foráneas:  
![Diagrama Relacional](https://github.com/kevinmaar/Inmobiliaria-Xalapa/blob/main/Documentos/Diagrama%20Relacional.jpg)

### Modelo relacional
# Modelo Relacional

**AGENCIA_INMOBILIARIA**  
ID_AGENCIA, RFC, TELÉFONO

**DIRECCION_AGENCIA**  
ID_AGENCIA (FK), CALLE, NUMERO, CP, POBLACION

**VIVIENDA**  
ID_VIVIENDA, DESCRIPCIÓN, ID_AGENCIA (FK), DNI_PROPIETARIO (FK)

**DIRECCION_VIVIENDA**  
ID_VIVIENDA (FK), CALLE, NUMERO, CP, POBLACION

**PROPIETARIO**  
DNI_PROPIETARIO, TELÉFONO, EMAIL, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO

**DIRECCION_PROPIETARIO**  
DNI_PROPIETARIO (FK), CALLE, NUMERO, CP, POBLACION

**ALQUILER**  
ID_ALQUILER, FECHA_FIRMA, FECHA_INICIO, FECHA_FIN, IMPORTE_MENSUAL, FIANZA, RENOVACIÓN, ID_VIVIENDA (FK), DNI_INQUILINO (FK)

**INQUILINO**  
DNI_INQUILINO, TELEFONO, FECHA_NACIMIENTO, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO


### Diccionario de datos

Se incluye un diccionario de datos que describe cada tabla, sus campos, tipos de datos y restricciones.
[Ver Diccionario de Datos](https://github.com/kevinmaar/Inmobiliaria-Xalapa/blob/main/Documentos/Diccionario%20de%20Datos.pdf)

---

## Autores

**Kevin Marzul Jeronimo Rojano** 
**Juan Elias Antonio Ramirez**
**Raul Nava Soler**
