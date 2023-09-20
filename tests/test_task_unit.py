from lib.TaskUnit import TaskUnit
from datetime import *
import pytest


# Make a TaskUnit with no due_date:
def test_creating_task_with_no_due_date():
    task = TaskUnit(task="somE task")
    assert task.task == "Some task"
    assert task.complete == False
    assert task.due_date_display == None

# Make a TaskUnit with set due_date:
def test_creating_task_with_due_date():
    task = TaskUnit(task="somE task", d=2, m=10, yyyy=2024)
    assert task.task == "Some task"
    assert task.complete == False
    assert task.due_date_display == "02/10/2024"

# Marking a TaskUnit as complete
def test_mark_test_as_complete():
    task = TaskUnit(task="somE task")
    task.mark_complete()
    assert task.complete == True

# Marking a TaskUnit as incomplete
def test_mark_test_as_incomplete():
    task = TaskUnit(task="somE task")
    task.mark_complete()
    assert task.complete == True
    task.mark_incomplete()
    assert task.complete == False

# Adding a due date to an existing TaskUnit:
def test_add_due_date():
    task = TaskUnit(task="somE task")
    task.change_due_date(2024, 6, 27)
    assert task.due_date_display == "27/06/2024"    

# Resetting a due date to default:
def test_reset_due_date():
    task = TaskUnit(task="somE task", d=2, m=10, yyyy=2024)
    assert task.due_date_display == "02/10/2024"
    task.reset_due_date()
    assert task.due_date_display == None



#### EDGE CASES:


### TYPEERRORS:
# Initiating a Task Unit with TypeError for task
def test_init_task_type_error():
    with pytest.raises(TypeError) as e:
        task = TaskUnit(task=9)
    error = str(e.value)
    assert error == "Wrong input type for task. Please input as string."

# Initiating a Task Unit with TypeError for date params
def test_init_date_params_type_error():
    with pytest.raises(TypeError) as e:
        task = TaskUnit(task="some task", yyyy="abc")
    error = str(e.value)
    assert error == "Wrong input type for dates. Please input as integers."

# Changing a Task due date with TypeError for date params
def test_change_date_params_type_error():
    task = TaskUnit(task="some task")
    with pytest.raises(TypeError) as e:
        task.change_due_date(yyyy="abc", m=1, d=27)
    error = str(e.value)
    assert error == "Wrong input type for dates. Please input as integers."


### OTHER:
# Initiation a Task Unit with date params out of range
def test_init_date_params_out_of_range():
    with pytest.raises(Exception) as e:
        task = TaskUnit(task="some task", yyyy=99999)
    error = str(e.value) 
    assert error == "Date out of range."

# Initiation a Task Unit with before today.
def test_init_date_out_of_range():
    with pytest.raises(Exception) as e:
        task = TaskUnit(task="some task", yyyy=2010)
    error = str(e.value) 
    assert error == "Date out of range."

# Changing a Task Unit due date with date params out of range
def test_change_date_params_out_of_range():
    task = TaskUnit(task="some task")
    with pytest.raises(Exception) as e:
        task.change_due_date(9999,1,1)
    error = str(e.value) 
    assert error == "Date out of range."

# Changing a Task Unit due date before today.
def test_change_date_out_of_range():
    task = TaskUnit(task="some task")
    with pytest.raises(Exception) as e:
        task.change_due_date(2010,1,1)
    error = str(e.value) 
    assert error == "Date out of range."

