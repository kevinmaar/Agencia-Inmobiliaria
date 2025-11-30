# Proyecto: Inmobiliaria Xalapa

Aplicación en **Python** para la gestión de una **agencia inmobiliaria**.  
Organizada por un modelo de 3 capas las cuales incluyen [dominio](https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/dominio), [persistencia](https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/persistencia) y [ui](https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/ui). Incluye menús por consola y operaciones CRUD para viviendas, propietarios, inquilinos, direcciones y alquileres.

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

El sistema usa una base de datos relacional con tablas como:

- AGENCIA_INMOBILIARIA  
- DIRECCION_AGENCIA  
- VIVIENDA  
- PROPIETARIO  
- DIRECCION_PROPIETARIO  
- INQUILINO  
- ALQUILER  
- RENOVACION  

Para mayor nocion del funcionamiento, se proporciona el siguiente diagrama relacional:
![img](https://github.com/kevinmaar/Inmobiliaria-Xalapa/blob/main/Documentos/Diagrama%20Relacional.jpg)

---

## Autores

**Kevin Marzul Jeronimo Rojano** 
**Juan Elias Antonio Ramirez**
**Raul Nava Soler**
