import argparse
import shlex
import datetime



cur_index = 1

expenses = []


def delete_expense(args):
    global expenses
    expenses = list(filter(lambda x:x[0]!= args.id[0], expenses))


def summary_expense(args):
    global expenses
    if not args:
        s= 0
        for (cur_index, date, description, amount) in expenses:
            s+=amount
        print(f"Total expenses: {s}")
    else:
        s = 0
        for (cur_index, date, description, amount) in expenses:
            if(date.month == args.month[0]):
                s+=amount
        print(f"Total expenses: {s}")
def add_expense(args):

    global cur_index
    expenses.append((cur_index, datetime.date.today(), args.description[0], args.amount[0]))
    cur_index+=1


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



while True:
    command = input("> ")

    if command.strip() == "quit":
        break

    args = parser.parse_args(shlex.split(command))

    args.func(args)



