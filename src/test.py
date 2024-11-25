# test.py

# Definición de funciones que agregarías en main.py
tasks = []

def add_task(task_name):
    tasks.append({"id": len(tasks) + 1, "name": task_name, "status": "pendiente"})
    print(f"Tarea '{task_name}' añadida.")

def view_tasks():
    for task in tasks:
        print(f"Tarea {task['id']}: {task['name']} - {task['status']}")

def update_task_status(task_id, new_status):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            print(f"Tarea {task['id']} actualizada a estado '{new_status}'.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print(f"Tarea {task_id} eliminada.")

# Pruebas
def run_tests():
    print("Iniciando pruebas...")

    # Prueba 1: Agregar tareas
    add_task("Estudiar para examen")
    add_task("Leer libro pendiente")
    print("\nTareas después de agregar:")
    view_tasks()

    # Prueba 2: Actualizar estado
    update_task_status(1, "completa")
    print("\nTareas después de actualizar estado:")
    view_tasks()

    # Prueba 3: Eliminar tarea
    delete_task(2)
    print("\nTareas después de eliminar:")
    view_tasks()

if __name__ == "__main__":
    run_tests()
