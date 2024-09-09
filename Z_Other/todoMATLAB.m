% Import necessary libraries
import matlab.ui.container.Panel
import matlab.ui.control.UIControl
import matlab.ui.control.UIControl.Callback

% Define the ToDoList class
classdef ToDoList < handle
    properties
        root
        tasks
        task_list
        entry
        add_button
        delete_button
        mark_button
    end
    
    methods
        function obj = ToDoList(root)
            obj.root = root;
            obj.root.Title = "To-Do List";
            obj.root.Resizable = [false false];
            obj.root.BackgroundColor = "#05192A";
            obj.tasks = {};
            
            % Create the task list panel
            f = uipanel(obj.root, 'BackgroundColor', '#7CA5B3', 'BorderType', 'groove', 'BorderWidth', 5);
            obj.task_list = uicontrol(f, 'Style', 'listbox', 'BackgroundColor', '#B7C8CE', 'FontName', 'Comic Sans MS', 'FontSize', 8, 'FontWeight', 'bold', 'Position', [5 5 400 200]);
            f.Position = [10 10 430 220];
            
            % Create the task entry field
            obj.entry = uicontrol(obj.root, 'Style', 'edit', 'BackgroundColor', '#B7C8CE', 'FontName', 'Comic Sans MS', 'FontSize', 10, 'FontWeight', 'bold', 'Position', [10 240 400 30]);
            
            % Create the buttons panel
            btnsF = uipanel(obj.root, 'BackgroundColor', '#7CA5B3', 'BorderType', 'groove', 'BorderWidth', 6);
            obj.add_button = uicontrol(btnsF, 'Style', 'pushbutton', 'String', 'Add Task', 'FontSize', 10, 'FontWeight', 'bold', 'Position', [10 10 100 40], 'Callback', @obj.add_task);
            obj.delete_button = uicontrol(btnsF, 'Style', 'pushbutton', 'String', 'Delete Task', 'FontSize', 10, 'FontWeight', 'bold', 'Position', [120 10 100 40], 'Callback', @obj.delete_task);
            obj.mark_button = uicontrol(btnsF, 'Style', 'pushbutton', 'String', 'Mark as Done', 'FontSize', 10, 'FontWeight', 'bold', 'Position', [230 10 100 40], 'Callback', @obj.mark_done);
            btnsF.Position = [10 280 430 60];
        end
        
        function add_task(obj, ~, ~)
            task = obj.entry.String;
            if ~isempty(task)
                obj.tasks{end+1} = task;
                obj.task_list.String{end+1} = task;
                obj.entry.String = '';
            end
        end
        
        function delete_task(obj, ~, ~)
            try
                task_index = obj.task_list.Value;
                obj.tasks(task_index) = [];
                obj.task_list.String(task_index) = [];
            catch
                msgbox('Error: Select a task to delete', 'Error', 'error');
            end
        end
        
        function mark_done(obj, ~, ~)
            try
                task_index = obj.task_list.Value;
                if ~startsWith(obj.tasks{task_index}, '[Done]')
                    obj.tasks{task_index} = ['[Done] ', obj.tasks{task_index}];
                    obj.task_list.String{task_index} = obj.tasks{task_index};
                else
                    msgbox('Error: Task is already marked as done', 'Error', 'error');
                end
            catch
                msgbox('Error: Select a task to mark as done', 'Error', 'error');
            end
        end
    end
end

% Create the main window and run the application
root = figure('Name', 'To-Do List', 'NumberTitle', 'off', 'Resize', 'off');
todo_list = ToDoList(root);
root.Visible = 'on';

