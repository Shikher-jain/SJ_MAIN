#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TASKS 100
#define MAX_TASK_LENGTH 100

typedef struct {
    char tasks[MAX_TASKS][MAX_TASK_LENGTH];
    int num_tasks;
} ToDoList;

void add_task(ToDoList *todo_list) {
    char task[MAX_TASK_LENGTH];
    printf("Enter task: ");
    fgets(task, MAX_TASK_LENGTH, stdin);
    task[strcspn(task, "\n")] = '\0'; // remove newline character
    if (strlen(task) > 0) {
        strcpy(todo_list->tasks[todo_list->num_tasks], task);
        todo_list->num_tasks++;
    }
}

void delete_task(ToDoList *todo_list) {
    int task_index;
    printf("Enter task index to delete: ");
    scanf("%d", &task_index);
    getchar(); // consume newline character
    if (task_index >= 0 && task_index < todo_list->num_tasks) {
        for (int i = task_index; i < todo_list->num_tasks - 1; i++) {
            strcpy(todo_list->tasks[i], todo_list->tasks[i + 1]);
        }
        todo_list->num_tasks--;
    } else {
        printf("Error: Invalid task index\n");
    }
}

void mark_done(ToDoList *todo_list) {
    int task_index;
    printf("Enter task index to mark as done: ");
    scanf("%d", &task_index);
    getchar(); // consume newline character
    if (task_index >= 0 && task_index < todo_list->num_tasks) {
        if (strncmp(todo_list->tasks[task_index], "[Done]", 6) != 0) {
            char done_task[MAX_TASK_LENGTH];
            sprintf(done_task, "[Done] %s", todo_list->tasks[task_index]);
            strcpy(todo_list->tasks[task_index], done_task);
        } else {
            printf("Error: Task is already marked as done\n");
        }
    } else {
        printf("Error: Invalid task index\n");
    }
}

void display_tasks(ToDoList *todo_list) {
    printf("To-Do List:\n");
    for (int i = 0; i < todo_list->num_tasks; i++) {
        printf("%d. %s\n", i + 1, todo_list->tasks[i]);
    }
}

int main() {
    ToDoList todo_list = {0};
    int choice;
    do {
        printf("\nTo-Do List Menu:\n");
        printf("1. Add Task\n");
        printf("2. Delete Task\n");
        printf("3. Mark Task as Done\n");
        printf("4. Display Tasks\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        getchar(); // consume newline character
        switch (choice) {
            case 1:
                add_task(&todo_list);
                break;
            case 2:
                delete_task(&todo_list);
                break;
            case 3:
                mark_done(&todo_list);
                break;
            case 4:
                display_tasks(&todo_list);
                break;
            case 5:
                printf("Exiting...\n");
                break;
            default:
                printf("Error: Invalid choice\n");
                break;
        }
    } while (choice != 5);
    return 0;
}
