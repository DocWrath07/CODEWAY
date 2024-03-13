import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_frame = tk.Frame(master, width=50)
        self.tasks_frame.pack(pady=10)

        # Drop-down box to display tasks
        self.selected_task = tk.StringVar(master)
        self.task_menu = tk.OptionMenu(master, self.selected_task, "")
        self.task_menu.pack()

        # Buttons for editing and removing tasks
        self.edit_button = tk.Button(master, text="Edit Task", command=self.edit_selected_task)
        self.edit_button.pack()
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_selected_task)
        self.remove_button.pack()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_dropdown()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def update_task_dropdown(self):
        menu = self.task_menu["menu"]
        menu.delete(0, "end")
        for task in self.tasks:
            menu.add_command(label=task, command=tk._setit(self.selected_task, task))
        if self.tasks:
            self.selected_task.set(self.tasks[0])

    def edit_selected_task(self):
        selected_task = self.selected_task.get()
        if selected_task:
            new_text = simpledialog.askstring("Edit Task", "Enter new task:", parent=self.master)
            if new_text:
                idx = self.tasks.index(selected_task)
                self.tasks[idx] = new_text
                self.update_task_dropdown()

    def remove_selected_task(self):
        selected_task = self.selected_task.get()
        if selected_task:
            self.tasks.remove(selected_task)
            self.update_task_dropdown()

def main():
    root = tk.Tk()
    todo_app = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()
