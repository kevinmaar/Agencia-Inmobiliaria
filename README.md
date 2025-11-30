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

#### Modelo relacional

#### AGENCIA_INMOBILIARIA
| Campo       | Tipo / Descripción            |
|------------|-------------------------------|
| ID_AGENCIA | Identificador único de la agencia |
| RFC        | Registro Federal de Contribuyentes |
| TELÉFONO   | Número de teléfono de la agencia |

#### DIRECCION_AGENCIA
| Campo       | Tipo / Descripción         |
|------------|----------------------------|
| ID_AGENCIA | Identificador de la agencia (FK) |
| CALLE      | Calle de la agencia        |
| NUMERO     | Número exterior            |
| CP         | Código postal              |
| POBLACION  | Ciudad / Población         |

#### VIVIENDA
| Campo          | Tipo / Descripción                       |
|----------------|-----------------------------------------|
| ID_VIVIENDA    | Identificador único de la vivienda      |
| DESCRICIÓN     | Descripción de la vivienda               |
| ID_AGENCIA     | Agencia propietaria (FK)                |
| DNI_PROPIETARIO| Propietario de la vivienda (FK)         |

#### DIRECCION_VIVIENDA
| Campo       | Tipo / Descripción              |
|------------|---------------------------------|
| ID_VIVIENDA| Identificador de la vivienda (FK) |
| CALLE      | Calle de la vivienda            |
| NUMERO     | Número exterior                 |
| CP         | Código postal                   |
| POBLACION  | Ciudad / Población              |

#### PROPIETARIO
| Campo            | Tipo / Descripción                      |
|-----------------|----------------------------------------|
| DNI_PROPIETARIO  | Identificador único del propietario    |
| TELÉFONO         | Número de teléfono                     |
| EMAIL            | Correo electrónico                     |
| NOMBRE           | Nombre del propietario                 |
| APELLIDO_PATERNO | Apellido paterno                        |
| APELLIDO_MATERNO | Apellido materno                        |

#### DIRECCION_PROPIETARIO
| Campo           | Tipo / Descripción                |
|----------------|----------------------------------|
| DNI_PROPIETARIO | Propietario (FK)                 |
| CALLE           | Calle                             |
| NUMERO          | Número exterior                   |
| CP              | Código postal                     |
| POBLACION       | Ciudad / Población                |

#### ALQUILER
| Campo          | Tipo / Descripción                          |
|----------------|--------------------------------------------|
| ID_ALQUILER    | Identificador único del alquiler           |
| FECHA_FIRMA    | Fecha de firma del contrato                 |
| FECHA_INICIO   | Fecha de inicio del alquiler                |
| FECHA_FIN      | Fecha de fin del alquiler                   |
| IMPORTE_MENSUAL| Pago mensual                                |
| FIANZA         | Depósito de garantía                        |
| RENOVACIÓN     | Indica si hubo renovación (sí/no)          |
| ID_VIVIENDA    | Vivienda alquilada (FK)                     |
| DNI_INQUILINO  | Inquilino que renta (FK)                    |

#### INQUILINO
| Campo            | Tipo / Descripción                     |
|-----------------|---------------------------------------|
| DNI_INQUILINO    | Identificador único del inquilino     |
| TELEFONO         | Número de teléfono                     |
| FECHA_NACIMIENTO | Fecha de nacimiento                     |
| NOMBRE           | Nombre del inquilino                   |
| APELLIDO_PATERNO | Apellido paterno                       |
| APELLIDO_MATERNO | Apellido materno                       |


### Diccionario de datos

Se incluye un diccionario de datos que describe cada tabla, sus campos, tipos de datos y restricciones.
[Ver Diccionario de Datos](https://github.com/kevinmaar/Inmobiliaria-Xalapa/blob/main/Documentos/Diccionario%20de%20Datos.pdf)

---

## Autores

**Kevin Marzul Jeronimo Rojano** 
**Juan Elias Antonio Ramirez**
**Raul Nava Soler**
