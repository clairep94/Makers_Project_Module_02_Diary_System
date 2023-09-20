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
        
        self.task = task.lower().capitalize()
        self.complete = False
        
        self.default_due_date = datetime(2100, 1, 1)
        self.due_date = datetime(yyyy, m, d) #default is (2100, 1, 1) --> sort by this attribute
        self.due_date_display = self.due_date.strftime("%d/%m/%Y") #default is None --> display by this attribute
        if self.due_date == self.default_due_date:
            self.due_date_display = None

        #print to confirm init:
        print(f"Added task: {self.task}\nDue date:{self.due_date_display}\n")
    



    def mark_complete(self):
        '''
        Params: None
        Returns: None | Error if already complete
        Side Effects: switches task.complete = True
        '''
            
        self.complete = True

        #print to confirm marked complete:
        print(f"{self.task} completion marked {self.complete}")



    
    def mark_incomplete(self):
        '''
        Params: None
        Returns: None | Error if already incomplete
        Side Effects: switches task.complete = False
        '''

        self.complete = False

        #print to confirm marked incomplete:
        print(f"{self.task} completion marked {self.complete}")




    def add_due_date(self, yyyy: int in range (2023, 2101), m: int in range (1,13), d: int in range (1,32)):
        '''
        Params:
            yyyy: int in range (2023, 2101) describing year
            m: int in range (1,13) describing month
            d: int in range (1,32) describing day
        Returns: None | Error if date params out of range or TypeError.
        Side Effects: None
        '''
    
        self.due_date = datetime(yyyy, m, d)
        self.due_date_display = self.due_date.strftime("%d/%m/%Y")

        #print to confirm due date added:
        print(f"{self.task} due date changed to {self.due_date_display}\n")




    def reset_due_date(self):
        '''
        Params:
            yyyy: int in range (2023, 2101) describing year
            m: int in range (1,13) describing month
            d: int in range (1,32) describing day
        Returns: None
        Side Effects: None
        '''
        
        self.due_date = self.default_due_date
        self.due_date_display = None

        #print to confirm due date reset:
        print(f"{self.task} due date changed to {self.due_date_display}\n")
