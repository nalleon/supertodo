<div align="justify">

# supertodo
#### 📜 Autores: Pedro Martín Escula ([@PeterMartEsc](https://github.com/PeterMartEsc)) & Nabil León Álvarez ([@nalleon](https://github.com/nalleon)) 

<br>

Proyecto de una web en Python para la gestión de tareas desarrollado para el módulo de Desarrollo web en entorno servidor (DSW) durante el curso 2025-2026 en IES Puerto de la Cruz.


## Índice

-  [Requisitos](#requisitos)
-  [Estructura y diseño]( #estructura-y-diseño)
-  [Cómo ejecutar el proyecto](#cómo-ejecutar-el-proyecto)

### Requisitos

![Python](https://img.shields.io/badge/Python-%3E%3D3.13-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-%3E%3D5.2.7-0C4B33?logo=django&logoColor=white)
![Browser](https://img.shields.io/badge/Navegador-Web-4285F4?logo=googlechrome&logoColor=white)


### Estructura y diseño

#### Carpetas
```
supertodo/
│── main/
│── shared/
│── tasks/
```

#### Modelos

- Task

```python
name = models.CharField(max_length=70)
description = models.TextField(max_length=256, blank=True)
slug = models.SlugField(unique=True)
completed = models.BooleanField(default=False)
created_at = models.DateTimeField()
updated_at = models.DateTimeField()
```

#### URLS

- Main:
    - `admin/` &rightarrow; Página de administración
    - `tasks/` &rightarrow; Acceso a las urls de segundo nivel de las tareas

- Tasks:
    - `/` &rightarrow; Lista de todas las tareas
    - `completed/` &rightarrow; Lista de tareas completadas
    - `pending/` &rightarrow; Lista de tareas pendientes
    - `add/` &rightarrow; Añadir nueva tarea 
    - `<task_slug>/` &rightarrow; Detalle de una tarea 
    - `<task_slug>/notfound/` &rightarrow; Pantalla alternativa si no existe 
    - `<task_slug>/delete/` &rightarrow; Eliminar tarea
    - `<task_slug>/edit/` &rightarrow; Editar tarea
    - `<task_slug>/toggle/` &rightarrow; Marcar/Desmarcar como completada


<br>

### Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/nalleon/supertodo.git
```

2. Acceder a la carpeta raíz y ejecutar el siguiente comando:

```bash
cd supertodo/supertodo && j setup 
```

3. Accede a `http://127.0.0.1:8000/`

> Se proporciona un usuario con privilegios con credenciales admin:admin para la página de administración.

</div>