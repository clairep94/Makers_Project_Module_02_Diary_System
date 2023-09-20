from lib.TaskUnit import TaskUnit
from datetime import *
import pytest


# Make a TaskUnit with no due_date:
def test_creating_task_with_no_due_date():
    task = TaskUnit(task="somE task")
    assert task.task == "Some task"
    assert task.complete == False
    assert task.due_date_display == "01/01/2100"

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
    task.add_due_date(2024, 6, 27)
    assert task.due_date_display == "27/06/2024"    

# Resetting a due date to default:
def test_reset_due_date():
    task = TaskUnit(task="somE task", d=2, m=10, yyyy=2024)
    assert task.due_date_display == "02/10/2024"
    task.reset_due_date()
    assert task.due_date_display == "01/01/2100"

