import argparse
import shlex
import datetime
import json


cur_index = 1

expenses = []
def load_expenses():
    global expenses, cur_index

    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        expenses = []

        for item in data:
            expenses.append((
                item["id"],
                datetime.date.fromisoformat(item["date"]),
                item["description"],
                item["amount"]
            ))

        if expenses:
            cur_index = max(expense[0] for expense in expenses) + 1
        else:
            cur_index = 1

    except FileNotFoundError:
        expenses = []
        cur_index = 1

def save_expenses():
    data = []

    for expense_id, date, description, amount in expenses:
        data.append({
            "id": expense_id,
            "date": date.isoformat(),
            "description": description,
            "amount": amount
        })

    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def delete_expense(args):
    global expenses
    expenses = list(filter(lambda x:x[0]!= args.id[0], expenses))
    save_expenses()


def summary_expense(args):
    if args.month is None:
        total = sum(expense[3] for expense in expenses)
    else:
        month = args.month[0]
        total = sum(
            expense[3]
            for expense in expenses
            if expense[1].month == month
        )

    print(f"Total expenses: {total}")
def add_expense(args):

    global cur_index
    expenses.append((cur_index, datetime.date.today(), args.description[0], args.amount[0]))
    cur_index+=1
    save_expenses()


def list_expense(args):
    global expenses
    for expense in expenses:
        print(f"id: {expense[0]}, date:{expense[1]} description: {expense[2]}, amount: {expense[3]}")

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add",help="add new item")
list_parser = subparsers.add_parser("list", help="list of all expenses")
delete_parser = subparsers.add_parser("delete", help="delete by id")
summary_parser = subparsers.add_parser("summary", help="total expense")
add_parser.add_argument("--description", nargs=1, type=str)
add_parser.add_argument("--amount", nargs = 1, type=int)
summary_parser.add_argument("--month", nargs=1, type=int)
delete_parser.set_defaults(func = delete_expense)
add_parser.set_defaults(func = add_expense)
list_parser.set_defaults(func = list_expense)
summary_parser.set_defaults(func = summary_expense)

delete_parser.add_argument("--id", nargs=1, type=int)


load_expenses()
while True:
    command = input("> ")

    if command.strip() == "quit":
        break

    args = parser.parse_args(shlex.split(command))

    args.func(args)



