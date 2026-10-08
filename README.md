# Expense Tracker

A simple CLI expense tracker built with Python.

## Features

* Add expenses
* List expenses
* Delete expenses by ID
* Show total expenses
* Filter summary by month
* Store data in JSON
* Load saved expenses on startup

## Usage

Run the app:

```bash
python expense_tracker.py
```

Available commands:

```bash
add --description "Lunch" --amount 20
list
delete --id 1
summary
summary --month 10
quit
```

## Example

```text
> add --description "Lunch" --amount 20
> add --description "Coffee" --amount 5

> list
id: 1, date: 2026-10-08, description: Lunch, amount: 20
id: 2, date: 2026-10-08, description: Coffee, amount: 5

> summary
Total expenses: 25
```

## Tech Stack

* Python
* argparse
* shlex
* JSON

## Project Goal

This project was created to practice building command-line applications, parsing commands, working with files, and storing persistent data in Python.

Link: https://roadmap.sh/projects/expense-tracker
