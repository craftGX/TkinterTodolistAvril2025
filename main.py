import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestionnaire de Tâches")
        self.tasks = []

        self.task_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.entry_task = tk.Entry(self.master, width=52)
        self.entry_task.pack(pady=10)

        self.btn_add_task = tk.Button(self.master, text="Ajouter Tâche", command=self.add_task)
        self.btn_add_task.pack(pady=5)

        self.btn_remove_task = tk.Button(self.master, text="Supprimer Tâche", command=self.remove_task)
        self.btn_remove_task.pack(pady=5)

        self.btn_mark_complete = tk.Button(self.master, text="Marquer Comme Complète", command=self.mark_complete)
        self.btn_mark_complete.pack(pady=5)

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Avertissement", "Veuillez entrer une tâche.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner une tâche à supprimer.")

    def mark_complete(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index] += " (complète)"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner une tâche à marquer comme complète.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()