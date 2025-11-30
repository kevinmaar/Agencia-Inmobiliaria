# Proyecto: Inmobiliaria Xalapa

Aplicación en **Python** para la gestión de una **agencia inmobiliaria**.  
Organizada por capas (`(dominio)[https://github.com/kevinmaar/Inmobiliaria-Xalapa/tree/main/Proyecto/proyectoBD/dominio]', `datos`, `ui`). Incluye menús por consola y operaciones CRUD para viviendas, propietarios, inquilinos, direcciones y alquileres.

---

## Tabla de contenido
- [Descripción](#descripción)
- [Características](#características)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación y ejecución](#instalación-y-ejecución)
- [Base de datos](#base-de-datos)
- [Autor](#autor)

---

## Descripción

Este proyecto gestiona información relacionada con una agencia inmobiliaria:  
- Agencias  
- Propietarios  
- Inquilinos  
- Viviendas  
- Direcciones  
- Contratos de alquiler  
- Renovaciones de alquiler  

Toda la interacción se realiza mediante un menú en consola y cada módulo tiene operaciones CRUD.

---

## Características

- Menú interactivo por consola  
- CRUD para propietarios, inquilinos, viviendas, direcciones y alquileres  
- Consultas SQL organizadas dentro de clases  
- Arquitectura modular por capas  
- Fácil mantenimiento y ampliación  

---

## Estructura del proyecto

```
proyectoBD/
├─ dominio/        # Clases del modelo (Agencia, Propietario, Vivienda, etc.)
├─ datos/          # Conexión a la base de datos y consultas SQL
├─ ui/             # Menús y lógica de interacción con el usuario
└─ Main.py         # Punto de entrada del programa
```

> Nota: Las carpetas `__pycache__/` y archivos `.pyc` no deben subirse a GitHub.

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
git clone <URL-del-repositorio>
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

La capa `datos/` contiene todas las funciones de conexión y consulta.

---

## Autor

**Kevin Marzul Jeronimo Rojano**  
Universidad Veracruzana  
Ingeniería de Ciberseguridad e Infraestructura de Cómputo
