from lib.TaskUnit import TaskUnit
from lib.TaskList import TaskList
from datetime import *
import pytest


# Adding TaskUnits to a TaskList
def test_adding_tasks_to_task_list():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_list.add(task_A)
    assert task_list.all_tasks == [task_A]
    task_list.add(task_B)
    assert task_list.all_tasks == [task_A, task_B]

def test_error_invalid_add():
    task_list = TaskList()
    with pytest.raises(Exception) as e:
        task_list.add("Not a valid task")
    assert str(e.value) == "Invalid task"


# Deleting TaskUnit from TaskList:
def test_delete_task():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    assert task_list.all_tasks == [task_A, task_B, task_C]
    task_list.delete(task_B)
    assert task_list.all_tasks == [task_A, task_C]

def test_invalid_delete():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_list.add(task_A)
    with pytest.raises(Exception) as e:
        task_list.delete("Not a valid task")
    assert str(e.value) == "Invalid task"
    with pytest.raises(Exception) as e:
        task_list.delete(TaskUnit("another task"))
    assert str(e.value) == "Invalid task"


# Marking a TaskUnit as Complete, then updating self.all_tasks, self.completed_tasks, self.incomplete_tasks:
def test_mark_complete():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    task_list.mark_complete_task(task_B)
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == [task_B]
    assert task_list.incomplete_tasks == [task_A, task_C]

def test_error_invalid_mark_complete():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_list.add(task_A)
    task_B = TaskUnit("task B")
    assert task_list.all_tasks == [task_A]
    with pytest.raises(Exception) as e:
        task_list.mark_complete_task(task_B)
    assert str(e.value) == "Invalid task"


# Marking a TaskUnit as Complete, then updating self.all_tasks, self.completed_tasks, self.incomplete_tasks:
def test_mark_incomplete():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    task_list.mark_complete_task(task_B)
    task_list.mark_complete_task(task_A)
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == [task_A, task_B]
    assert task_list.incomplete_tasks == [task_C]
    task_list.mark_incomplete_task(task_A)
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == [task_B]
    assert task_list.incomplete_tasks == [task_A, task_C]

def test_error_invalid_mark_incomplete():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_list.add(task_A)
    task_B = TaskUnit("task B")
    assert task_list.all_tasks == [task_A]
    with pytest.raises(Exception) as e:
        task_list.mark_incomplete_task(task_B)
    assert str(e.value) == "Invalid task"


# Selecting a List:
def test_select_list():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    task_list.mark_complete_task(task_B)
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == [task_B]
    assert task_list.incomplete_tasks == [task_A, task_C]
    assert task_list.select_list("all") == task_list.all_tasks
    assert task_list.select_list("completed") == task_list.completed_tasks
    assert task_list.select_list("incomplete") == task_list.incomplete_tasks

def test_error_invalid_select_list():
    task_list = TaskList()
    with pytest.raises(Exception) as e:
        task_list.select_list("complete")
    assert str(e.value) == "Invalid choice. Please select 'all', 'completed' or 'incomplete'"


# Sorting a list by date:
def test_sort_list_by_date():
    task_list = TaskList()
    task_A = TaskUnit("task A", 2024, 6, 27)
    task_B = TaskUnit("task B")
    task_C = TaskUnit("Task C", 2023, 12, 12)
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    task_list.mark_complete_task(task_C)
    assert task_list.select_list("all") == task_list.all_tasks == [task_A,task_B,task_C]
    assert task_list.sort_by_due_date(task_list.select_list("all")) == [task_C,task_A,task_B]
    assert task_list.select_list("completed") == task_list.completed_tasks == [task_C]
    assert task_list.sort_by_due_date(task_list.select_list("completed")) == [task_C]
    assert task_list.select_list("incomplete") == task_list.incomplete_tasks == [task_A,task_B]
    assert task_list.sort_by_due_date(task_list.select_list("incomplete")) == [task_A,task_B]
def test_error_invalid_sort_list_by_date_param():
    task_list = TaskList()
    with pytest.raises(TypeError) as e:
        task_list.sort_by_due_date("invalid data")
    assert str(e.value) == "Invalid type for lst_to_sort. Please input a list."

# Deleting All:
def test_delete_all_tasks():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    task_list.delete_all()
    assert task_list.all_tasks == []

# Marking All as Done:
def test_complete_all_tasks():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    task_list.mark_all_complete()
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == [task_A, task_B, task_C]
    assert task_list.incomplete_tasks == []

# Marking All as Incomplete:
def test_incomplete_all_tasks():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    task_list.mark_all_complete()
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == [task_A, task_B, task_C]
    assert task_list.incomplete_tasks == []
    task_list.mark_all_incomplete()
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == []
    assert task_list.incomplete_tasks == [task_A, task_B, task_C]


# Change Due Date
def test_change_due_date():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_list.add(task_A)
    assert task_list.display(display_printable=True, display_due_date=True) == '''Task a
- Due: None'''
    task_list.change_due_date(task_A, 2024, 6, 27)
    assert task_list.display(lst_choice="all", display_printable=True, display_due_date=True) == '''Task a
- Due: 27/06/2024'''


# Reset Due Date
def test_error_change_due_date():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_list.add(task_A)
    assert task_list.display(display_printable=True, display_due_date=True) == '''Task a
- Due: None'''
    task_list.change_due_date(task_A, 2024, 6, 27)
    assert task_list.display(display_printable=True, display_due_date=True) == '''Task a
- Due: 27/06/2024'''
    task_list.reset_due_date(task_A)
    assert task_list.display(display_printable=True, display_due_date=True) == '''Task a
- Due: None'''


# Reset All Due Dates


# Displaying Tasks in Terminal - list of TaskUnit.task
def test_display_tasks_as_list_object_of_task_names():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.incomplete_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == []
    assert task_list.display() == ["Task a", "Task b", "Task c"]
    assert task_list.display(lst_choice="completed") == []
    assert task_list.display(lst_choice="incomplete") == ["Task a", "Task b", "Task c"]

# Displaying Tasks in Terminal - formated printable with no dates
def test_display_tasks_as_list_printable_no_dates():
    task_list = TaskList()
    task_A = TaskUnit("task A")
    task_B = TaskUnit("task B")
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.incomplete_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == []
    assert task_list.display(display_printable=True) == "Task a\nTask b\nTask c"

# Displaying Tasks in Terminal - formatted printable with dates
def test_display_tasks_as_list_printable_no_dates():
    task_list = TaskList()
    task_A = TaskUnit("task A", 2024, 6, 27)
    task_B = TaskUnit("task B", 2024, 1, 20)
    task_C = TaskUnit("task C")
    task_list.add(task_A)
    task_list.add(task_B)
    task_list.add(task_C)
    assert task_list.all_tasks == [task_A, task_B, task_C]
    assert task_list.incomplete_tasks == [task_A, task_B, task_C]
    assert task_list.completed_tasks == []
    assert task_list.display(display_printable=True, display_due_date=True) == '''Task a
- Due: 27/06/2024
Task b
- Due: 20/01/2024
Task c
- Due: None'''
    assert task_list.display(display_printable=True, display_due_date=True, sort_by_due = True) == '''Task b
- Due: 20/01/2024
Task a
- Due: 27/06/2024
Task c
- Due: None'''