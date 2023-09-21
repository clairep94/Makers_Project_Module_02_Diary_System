from datetime import datetime
from lib.TaskUnit import TaskUnit

class TaskList():
    def __init__(self) -> None:
        '''
        Params: None
        Returns: None
        Side Effects: Initialises empty lists to store objects below:
        '''
        self.all_tasks = [] #all TaskUnit objects --> not displayed to user
        self.completed_tasks = [entry for entry in self.all_tasks if entry.complete == True] #all TaskUnit objects where TaskUnit.complete = True --> not displayed to user
        self.incomplete_tasks = [entry for entry in self.all_tasks if entry.complete == False] #all TaskUnit objects where TaskUnit.complete = False --> not displayed to user

    #REFRESH INCOMPLETE & COMPLETE TASK LISTS:
    def refresh(self):
        '''
        Params: None
        Returns: None
        Effects: Updates self.complete_tasks and self.incomplete_tasks after each change
        '''
        self.completed_tasks = [entry for entry in self.all_tasks if entry.complete == True] #all TaskUnit objects where TaskUnit.complete = True --> not displayed to user
        self.incomplete_tasks = [entry for entry in self.all_tasks if entry.complete == False] #all TaskUnit objects where TaskUnit.complete = False --> not displayed to user

    #SELECT BY TASK: for when I change all functions below from TaskUnit object to TaskUnit.task
    def select_task_by_name(self, task_string):
        #returns TaskUnit object where task_string == TaskUnit.task
        pass

    #SELECTING LIST:
    def select_list(self, lst_choice) -> list:
        '''
        Params: lst_choice: string representing self.all_tasks, self.complete_tasks, and self.incomplete_tasks
        Returns: self.all_tasks, self.complete_tasks, self.incomplete_tasks | Exception for invalid choice
        Effects: None
        '''
        map = {"all": self.all_tasks,
            "completed": self.completed_tasks,
            "incomplete": self.incomplete_tasks}
        if lst_choice not in map: #catch invalid lst_choice inputs
            raise Exception("Invalid choice. Please select 'all', 'completed' or 'incomplete'")
        else:
            return map[lst_choice]

    #SORT BY DATE:
    def sort_by_due_date(self, lst_to_sort:list) -> list:
        '''
        Params: one of the lists in the TaskList attributes (self.all_tasks, self.completed_tasks, self.incomplete_tasks)
        Returns: The selected list, sorted by chronological due_date | TypeError
        '''
        if type(lst_to_sort) != list:
            raise TypeError("Invalid type for lst_to_sort. Please input a list.")
        return sorted(lst_to_sort, key = lambda x: x.due_date)
    
    #ADDING/DELETING:
    def add(self, task) -> None:
        '''
        Params: task: TaskUnit object
        Returns: None | TypeError if isinstance() != TaskUnit
        Side Effects: Adds TaskUnit to self.all_tasks
        '''
        if isinstance(task, TaskUnit) != True:
            raise Exception("Invalid task")
        self.all_tasks.append(task)
        self.refresh()
    def delete(self, task) -> None: 
        '''
        Params: task: TaskUnit object
        Returns: None | TypeError if isinstance() != TaskUnit 
        Side Effects: removes TaskUnit from self.all_tasks
        '''
        if task not in self.all_tasks:
            raise Exception("Invalid task")
        self.all_tasks.remove(task)
        self.refresh()
    def delete_all(self, lst="all") -> None:
        '''
        Params: lst - string representing which list to update
        Returns: None
        Effects: moves all tasks to self.completed
        '''
        selected_list = self.select_list(lst_choice=lst)
        self.all_tasks = [entry for entry in self.all_tasks if entry not in selected_list]
        self.refresh()

    #COMPLETE/INCOMPLETE:
    def mark_complete_task(self, task) -> None:        
        '''
        Params: task: TaskUnit object
        Returns: None | TypeError if isinstance() != TaskUnit 
        Side Effects: updates TaskUnit.complete = True
        '''
        if task not in self.all_tasks:
            raise Exception("Invalid task")
        task.mark_complete()
        self.refresh()
    def mark_incomplete_task(self, task):
        '''
        Params: task: TaskUnit object
        Returns: None | TypeError if isinstance() != TaskUnit 
        Side Effects: updates TaskUnit.complete = True
        '''
        if task not in self.all_tasks:
            raise Exception("Invalid task")
        task.mark_incomplete()
        self.refresh()
    def mark_all_complete(self, lst="all"):
        '''
        Params:  lst - string representing which list to update
        Returns: None
        Effects: moves all tasks to self.completed
        '''
        selected_list = self.select_list(lst_choice=lst)
        for entry in selected_list:
            self.mark_complete_task(task=entry)
    def mark_all_incomplete(self, lst="all"):
        '''
        Params:  lst - string representing which list to update
        Returns: None
        Effects: moves all tasks to self.completed
        '''
        selected_list = self.select_list(lst_choice=lst)
        for entry in selected_list:
            self.mark_incomplete_task(task=entry)


    #CHANGE/RESET DUE DATE:
    def change_due_date(self, task, yyyy, m, d):
        '''
        Params: 
            task: TaskUnit object
            yyyy: int in range (2023, 2101) describing year
            m: int in range (1,13) describing month
            d: int in range (1,32) describing day
        Returns: None
        Effects: Changes due date for TaskUnit object
        '''
        if task not in self.all_tasks:
            raise Exception("Invalid task")
        task.change_due_date(yyyy, m, d)
        self.refresh()
    def reset_due_date(self, task):
        '''
        Params: task: TaskUnit object
        Returns: None
        Effects: resets task due date | Exception if task is not in self.all_tasks
        '''
        if task not in self.all_tasks:
            raise Exception("Invalid task")
        task.reset_due_date()
        self.refresh()
    def reset_all(self, lst="all"):
        '''
        Params: lst - string representing which list to update
        Returns: None
        Effects: reset all due dates
        '''
        selected_list = self.select_list(lst_choice=lst)
        for entry in selected_list:
            entry.reset_due_date()
        self.refresh()

    #DISPLAYING TASKS IN THE TERMINAL: 
    def display(self, lst_choice = "all", display_printable = False, display_due_date = False, sort_by_due = False):
        '''
        Params:
            lst_name: string -- which list of to display. Must be within ["all", "completed", "incomplete"]
            display_printable: boolean -- whether to display as printable format, or as a list.
            display_due_date: boolean -- whether to display due date when display is set to True. 
                * If display_printabe is False, display_due_date is set to False.
            sort_by_due: boolean -- whether to sort by added (default) when set to False, or by due_date when set to True
        '''

        #1) Setting the list of TaskUnits to display -- all, completed, or incomplete
        lst = self.select_list(lst_choice=lst_choice)

        #2) Sort list of TaskUnits by date or not
        if sort_by_due == True:
            sorted_lst = self.sort_by_due_date(lst_to_sort=lst)
        else:
            sorted_lst = lst

        #3) Create a list of printable strings for each TaskUnit object in TaskList:
        # See self.format()
        formatted_list = self.format(sorted_lst, display_printable, display_due_date)

        #4) Return either a list of tasks, or printable string as a formatted list:
        if display_printable == False:
            return formatted_list
        else:
            return "\n".join(formatted_list)
    def format(self, lst_choice_sorted, display_printable, display_due_date): #REFORMAT TO BELOW.
        '''
        For use in self.display():
        Params:
            lst: list of TaskUnit objects
            display_printable: boolean -- whether to display as printable format, or as a list.
            display_due_date: boolean -- whether to display due date when display is set to True.
                * If display_printabe is False, display_due_date is set to False.
        Return:
            a list of formatted strings according to the settings in the parameter
        
        OPTIONS:
            display_printable == False --> ["Task 1", "Task 2"]
            display_printable == True and display_due_dates == False
                --> Task 1
                    Task 2
            display_printable == True and display_due_dates == True
                --> Task 1
                    - Due: dd/mm/yyyy
                    Task 2
                    - Due: dd/mm/yyyy
        '''
        result = []
        
        for entry in lst_choice_sorted:
            if display_printable == True and display_due_date == True:
                string = f"{entry.task}\n- Due: {entry.due_date_display}"
            elif display_printable == True and display_due_date == False:
                string = f"{entry.task}"
            else: 
                string = entry.task
            result.append(string)

        return result
    ### Change format to [] Task.task or [x] Task.task for printable