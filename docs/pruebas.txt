# Pruebas del Sistema de Gestión de Tareas

## Prueba 1: Agregar tareas
**Objetivo:** Verificar que las tareas se agreguen correctamente a la lista.  
**Acción:** Agregar las tareas "Estudiar para examen" y "Leer libro pendiente".  
**Resultado esperado:**  
- Las tareas se agregan a la lista de tareas y deben aparecer al ser visualizadas.

### Código:
python
tasks = []

def add_task(task_name):
    tasks.append({"id": len(tasks) + 1, "name": task_name, "status": "pendiente"})
    print(f"Tarea '{task_name}' añadida.")

def view_tasks():
    for task in tasks:
        print(f"Tarea {task['id']}: {task['name']} - {task['status']}")

# Ejecutar prueba
add_task("Estudiar para examen")
add_task("Leer libro pendiente")
view_tasks()

### Resultado esperado: 
Tarea 'Estudiar para examen' añadida.
Tarea 'Leer libro pendiente' añadida.
Tarea 1: Estudiar para examen - pendiente
Tarea 2: Leer libro pendiente - pendiente
