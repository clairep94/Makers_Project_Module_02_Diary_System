# RECIPE


## 1) User Stories:

```
As a user
So that I can record my experiences
I want to keep a regular diary
```

```
As a user
So that I can reflect on my experiences
I want to read my past diary entries
```

* DiaryEntry --> attributes: .date, .title, .contents, .display_format
* DiaryEntry --> add() --> Diary
* Diary --> display_all() --> [DiaryEntrie(s).title] or [DiaryEntrie(s).date]
* Diary --> read() --> DiaryEntry.contents

```
As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed
```

* Reading chunk - entire entries of Diary & portions of DiaryEntry based on time * reading_speed

* DiaryEntry --> method: word_count(), chunk(), read_portion(), read_all()
* Diary --> method: add(), word_counts(), reading_chunk_whole_entry(), reading_chunk_partial_entry(), all_contents()

```
As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
```

* TaskUnit --> add() --> TaskList
* TaskUnit --> attributes: .complete, .task, .due_date
* TaskUnit --> methods: .mark_complete(), .add_due_date()

* TaskList --> attributes: .all_tasks --> [TaskUnit(s)]
* TaskList --> methods: add(), .complete_all(), .completed(), .incomplete(), .delete_all_completed(), .delete_all_incomplete(), .delete_all(), .view_by_due_date(), .view_by_added()

```
As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
```

* Extract phone numbers -- starts with "0", and len is 11 digits

* ContactsList --> attributes: [Contact(s)]
* ContactsList --> methods: add(), extract_all(), display_all()
* ContactsList --> extra_all() --> Diary.all_contents()

* Contact --> attributes: .number, .name
* Contact --> method: .add_name()


## 2) Design the Class System:

* See above.


## 3) Create Example as Integration Test

Between TaskUnit and TaskList:

Adding TasksUnit(s) to TaskList:

```shell
#Adding TaskUnits to a TaskList
TaskList.add(TaskUnitA(due_date = None --> 01/01/2100 as default))
TaskList.add(TaskUnitB(due_date = 20/09/2023))
TaskList.add(TaskUnitC(due_date = 21/09/2023))

#Viewing by Added -- display only incompleted; Add display formatting?
TaskList.view_incomplete_by_added() 
#[TaskUnitA, TaskUnitB, TaskUnitC] 

#Viewing by Completed -- display only incompleted? Add display formatting?
TaskList.view_incomplete_by_due_date() 
#[TaskUnitB, TaskUnitC, TaskUnitA] 

#Deleting a TaskUnit
TaskList.delete(TaskUnitA)
TaskList.view_incomplete_by_added()
#[TaskUnitB, TaskUnitC]

#Deleting a TaskUnit that does not exist
TaskList.delete(TaskUnitD) #Throws Error

#Complete all
TaskList.complete_all()
TaskList.view_incomplete_by_added() #[]
TaskList.view_completed() #[TaskUnitB, TaskUnitC]

#Delete all
TaskList.delete_all_completed()
TaskList.view_completed() #[]

TaskList.delete_all_incomplete()
TaskList.view_incomplete_by_added() #[]
```

```
my_list.sort(key=lambda x: x.my_attribute)
sorted_list = sorted(my_list, key=lambda x: x.my_attribute)
```


## 4) Create Example as Unit Test

For TaskUnit:

``` shell
# For a TaskUnit with default kwargs:
task = TaskUnit(task = "some task")
task.task #"Some task" - .lower().capitalize()
task.complete #False
task.due_date #01/01/2100 -- date.time object
```

``` shell
# For a TaskUnit with set due_date:
task = TaskUnit(task = "some task", due_date = 20/09/2023)
task.task #"some task"
task.complete #False
task.due_date #01/01/2100 -- date.time object
```

``` shell
# Marking a TaskUnit complete
task = TaskUnit(task = "some task")
task.mark_complete()
task.complete #False
```

``` shell
# Adding a due date to a TaskUnit
task = TaskUnit(task = "some task")
task.mark_complete()
task.complete #False
```

``` shell
# 
```