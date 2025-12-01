# Proyecto: Agencia Inmobiliaria

Aplicación en **Python** para la gestión de una **agencia inmobiliaria**.  
El proyecto está organizado en un modelo de **tres capas**: [dominio](https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/dominio), [persistencia](https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/persistencia) y [ui](https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/ui). Incluye menús por consola y operaciones CRUD para viviendas, propietarios, inquilinos, direcciones y alquileres.

---

## Tabla de contenido
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Base de datos](#base-de-datos)
- [Estructura del codigo](#estructura-del-codigo)
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

> **Importante:** Antes de ejecutar la aplicación, asegúrate de cargar la base de datos desde el archivo `BD.sql` y configurar en `BD.py` la **contraseña** de tu BD, para que todas las operaciones funcionen correctamente.

---

## Base de datos

El sistema utiliza una base de datos relacional gestionada con [MariaDB](https://mariadb.org/)

El siguiente diagrama entidad-relacion muestra cómo se relacionan las tablas de la base de datos, incluyendo llaves primarias y foráneas:  
![Diagrama Relacional](https://github.com/kevinmaar/Inmobiliaria-Xalapa/blob/main/Documentos/Diagrama%20Relacional.jpg)

### Modelo relacional

Para facilitar el manejo de la base de datos se proporciona el siguiente esquema de modelo relacional
```
AGENCIA_INMOBILIARIA      [ID_AGENCIA, RFC, TELÉFONO]
DIRECCION_AGENCIA         [ID_AGENCIA(FK), CALLE, NUM, CP, POBLACION]
VIVIENDA                  [ID_VIVIENDA, DESCR, ID_AGENCIA(FK), DNI_PROPIETARIO(FK)]
DIRECCION_VIVIENDA        [ID_VIVIENDA(FK), CALLE, NUM, CP, POBLACION]
PROPIETARIO               [DNI_PROPIETARIO, TEL, EMAIL, NOMBRE, APELLIDO_P, APELLIDO_M]
DIRECCION_PROPIETARIO     [DNI_PROPIETARIO(FK), CALLE, NUM, CP, POBLACION]
ALQUILER                  [ID_ALQ, FECHA_F, FECHA_I, FECHA_FIN, IMPORTE, FIANZA, RENOV, ID_VIV(FK), DNI_INQ(FK)]
INQUILINO                 [DNI_INQUILINO, TEL, F_NAC, NOMBRE, APELLIDO_P, APELLIDO_M]
```

### Diccionario de datos

Se incluye un diccionario de datos que describe cada tabla, sus campos, tipos de datos y restricciones.
[Ver Diccionario de Datos](https://github.com/kevinmaar/Inmobiliaria-Xalapa/blob/main/Documentos/Diccionario%20de%20datos.pdf)

---

## Estructura del codigo

Este diagrama muestra la estructura de clases en Python y cómo se relacionan dentro de la capa de dominio:  
![Diagrama de Clases](https://github.com/kevinmaar/Inmobiliaria-Xalapa/blob/main/Documentos/Diagrama%20Clases.png)

---

## Autores

- Kevin Marzul Jeronimo Rojano | [kiraaab](https://github.com/kevinmaar) 
- Juan Elias Antonio Ramirez   | [western](https://github.com/western1258)
- Raul Nava Soler              | [hoffman](https://github.com/Hoffman99)

