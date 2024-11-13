# main.py
tasks = []

def add_task(task_name):
    tasks.append({"id": len(tasks) + 1, "name": task_name, "status": "pendiente"})
    print(f"Tarea '{task_name}' añadida.")

def view_tasks():
    for task in tasks:
        print(f"Tarea {task['id']}: {task['name']} - {task['status']}")

add_task("Estudiar para examen")
add_task("Leer libro pendiente")
view_tasks()
