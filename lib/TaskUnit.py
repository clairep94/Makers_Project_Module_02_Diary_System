from datetime import datetime

class TaskUnit:
    def __init__(self, task=str, yyyy: int=2100, m: int=1, d: int=1) -> None:
        '''
        Params: 
            task: str describing a task
            yyyy: int in range (2023, 2101) describing year
            m: int in range (1,13) describing month
            d: int in range (1,32) describing day
        Returns: None | Error if date params out of range or TypeError.
        Side Effects: creates a TaskUnit object with a set due date in in dd/mm/yyyy format, 
        and task string in title case
        '''
        #Catching TypeError for task:
        if type(task) != str:
            raise TypeError("Wrong input type for task. Please input as string.")
        #Catching TypeError for date params:
        if [type(date) for date in [yyyy,m,d]] != [int,int,int]:
            raise TypeError("Wrong input type for dates. Please input as integers.")
        #Catching if date params are out of range -- variables not in ranges specified, or date is before datetime.now():
        if yyyy not in range(2023, 2101) or m not in range(1,13) or d not in range(1,32) or datetime(yyyy, m, d) < datetime.now():
            raise Exception("Date out of range.")

        #Main init:
        self.task = task.lower().capitalize()
        self.complete = False
        
        self.default_due_date = datetime(2100, 1, 1)
        self.due_date = datetime(yyyy, m, d) #default is (2100, 1, 1) --> sort by this attribute
        self.due_date_display = self.due_date.strftime("%d/%m/%Y") #default is None --> display by this attribute
        if self.due_date == self.default_due_date:
            self.due_date_display = None
        

        #print to confirm init:
        print(f"Added task: {self.task}\nDue date:{self.due_date_display}\n")
    


    # MARK COMPLETE/INCOMPLETE
    def mark_complete(self) -> None:
        '''
        Params: None
        Returns: None
        Side Effects: switches task.complete = True
        '''
        #Main method: 
        self.complete = True

        #print to confirm marked complete:
        print(f"{self.task} completion marked {self.complete}")
    
    def mark_incomplete(self) -> None:
        '''
        Params: None
        Returns: None
        Side Effects: switches task.complete = False
        '''
        #Main method:
        self.complete = False

        #print to confirm marked incomplete:
        print(f"{self.task} completion marked {self.complete}")



    # CHANGE/RESET DUE DATE
    def change_due_date(self, yyyy: int in range (2023, 2101), m: int in range (1,13), d: int in range (1,32)) -> None:
        '''
        Params:
            yyyy: int in range (2023, 2101) describing year
            m: int in range (1,13) describing month
            d: int in range (1,32) describing day
        Returns: None | Error if date params out of range or TypeError.
        Side Effects: None
        '''
    
        #Catching TypeError for date params:
        if [type(date) for date in [yyyy,m,d]] != [int,int,int]:
            raise TypeError("Wrong input type for dates. Please input as integers.")
        #Catching if date params are out of range -- variables not in ranges specified, or date is before datetime.now():
        if yyyy not in range(2023, 2101) or m not in range(1,13) or d not in range(1,32) or datetime(yyyy, m, d) < datetime.now():
            raise Exception("Date out of range.")

        #Main method:
        self.due_date = datetime(yyyy, m, d)
        self.due_date_display = self.due_date.strftime("%d/%m/%Y")

        #print to confirm due date added:
        print(f"{self.task} due date changed to {self.due_date_display}\n")

    def reset_due_date(self) -> None:
        '''
        Params: None
        Returns: None
        Side Effects: Reset due date for task to display None and datetime object for 2100/01/01
        '''
        #Main method:
        self.due_date = self.default_due_date
        self.due_date_display = None

        #print to confirm due date reset:
        print(f"{self.task} due date changed to {self.due_date_display}\n")


    # DISPLAY -- Depreciated, use for unit testing only. Will use newer display methods within TaskList
    def display(self) -> str:
        '''
        Params: None
        Returns: Formatted string for displaying task by task & due date
        Side Effects: None
        '''
        return f"{self.task}\nDue: {self.due_date_display}"