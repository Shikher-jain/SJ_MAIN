const { Tk, Frame, Listbox, Entry, Button, messagebox } = require('tkinter');

class ToDoList {
    constructor(root) {
        this.root = root;
        this.root.title("To-Do List");
        this.root.resizable(false, false);
        this.root.config({ bg: "#05192A" });
        this.tasks = [];

        this.f = Frame(this.root, { bg: "#7CA5B3", bd: 5, relief: "groove" });
        this.task_list = Listbox(this.f, { bg: "#B7C8CE", width: 40, height: 10, font: ['Comic Sans MS', '8', 'bold'] });
        this.task_list.pack({ padx: 5, pady: 5 });
        this.f.pack({ padx: 10, pady: 10 });

        this.entry = Entry(this.root, { bg: "#B7C8CE", width: 37, bd: 4, relief: "sunken", font: ['Comic Sans MS', '10', 'bold'] });
        this.entry.pack({ padx: 10, pady: [0, 10] });

        this.btnsF = Frame(this.root, { bg: "#7CA5B3", bd: 6, relief: "groove" });
        this.add_button = Button(this.btnsF, { text: "Add Task", bd: 5, relief: "raised", width: 8, command: this.add_task });
        this.delete_button = Button(this.btnsF, { text: "Delete Task", bd: 5, relief: "raised", width: 9, command: this.delete_task });
        this.mark_button = Button(this.btnsF, { text: "Mark as Done", bd: 5, relief: "raised", width: 10, command: this.mark_done });

        this.add_button.grid({ row: 0, column: 0, padx: 10, pady: 10 });
        this.delete_button.grid({ row: 0, column: 1, padx: 10, pady: 10 });
        this.mark_button.grid({ row: 0, column: 2, padx: 10, pady: 10 });
        this.btnsF.pack({ pady: [0, 10] });
    }

    add_task = () => {
        const task = this.entry.get();
        if (task) {
            this.tasks.push(task);
            this.task_list.insert(END, task);
            this.entry.delete(0, END);
        }
    }

    delete_task = () => {
        try {
            const task_index = this.task_list.curselection()[0];
            this.tasks.splice(task_index, 1);
            this.task_list.delete(task_index);
        } catch (error) {
            messagebox.showerror("Error", "Select a task to delete");
        }
    }

    mark_done = () => {
        try {
            const task_index = this.task_list.curselection()[0];
            if (!this.tasks[task_index].startsWith("[Done]")) {
                this.tasks[task_index] = `[Done] ${this.tasks[task_index]}`;
                this.task_list.delete(task_index);
                this.task_list.insert(task_index, this.tasks[task_index]);
            } else {
                messagebox.showerror("ERROR", "  Already Mark As Done  ");
            }
        } catch (error) {
            messagebox.showerror("Error", "Select a task to mark as done");
        }
    }
}

if (require.main === module) {
    const root = Tk();
    const todo_list = new ToDoList(root);
    root.mainloop();
}

