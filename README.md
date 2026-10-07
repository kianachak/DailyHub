# DailyHub

A simple command-line life management application built with Python.

## What is it?

DailyHub is a command-line application built with Python that brings several everyday management tools together in one place. Instead of using separate programs for different tasks, users can manage their to-do list, notes, expenses, and bills through a single application.
The project is designed as a modular application, with each feature organized in a separate Python module and connected through a central main menu. This structure makes the application easier to understand, maintain, and extend.

## Features

- **To-Do List**
  - Add, remove, show, and complete tasks
  - Track the completion status of tasks

- **Notes**
  - Add, show, delete, search, and edit notes
  - Prevent duplicate notes

- **Expenses**
  - Add and track expenses
  - View recorded expenses
  - Calculate total spending

- **Budget Manager**
  - Add and view bills with their amounts and due dates
  - Edit bill amounts and due dates
  - Generate a weekly report of upcoming bills

- **Application**
  - Central main menu for accessing all features
  - Separate modules for each part of the application
  - Number-based and text-based menu options
  - Input validation and error handling

## What I Learned

- Organizing a Python project into multiple modules
- Importing modules and using functions across different Python files
- Designing functions with clear and separate responsibilities
- Working with lists and dictionaries to store and manage data
- Using loops, conditional logic, and `enumerate()` to build interactive menus
- Validating user input and handling `ValueError`
- Using functions with parameters and return values
- Managing program flow between a central application and separate modules
- Refactoring smaller programs and integrating them into a larger application
- Formatting and presenting structured data in the terminal
- Testing different inputs and handling common edge cases

## How to Run

To run DailyHub, make sure Python is installed on your system and run:

```bash
python main.py
```

## Example

```text
============================
  Welcome To DailyHub
============================
0. To Do List
1. Notes
2. Expenses
3. Budgeting
4. Quit

Which place you want to go?: 0

======================
     <To-Do List>
======================
0. Add
1. Remove
2. Show
3. Finish task
4. Quit

What is your option: add
Enter your task: study python

Task added successfully.

What is your option: quit

See you later.

======================
0. To Do List
1. Notes
2. Expenses
3. Budgeting
4. Quit

Which place you want to go?: 2

=======================
       <Expenses>
=======================
0. Add Expense
1. Show Expenses
2. Total Spending
3. Quit

What is your option: add expense
Enter your expense name: book
Enter the spend of book: 25

Your new expense
```
