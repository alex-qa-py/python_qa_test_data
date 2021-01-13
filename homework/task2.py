import csv
import json


def csv_to_json(file_in, dir_out):
    with open(file_in) as read:
        reader = csv.DictReader(read)
        rows = list(reader)

    with open(dir_out, 'w') as write:
        json.dump(rows, write, indent=4)


def json_to_template(file_in_users, file_in_books, file_out):
    with open(file_in_users, "r") as f1, open(file_in_books, "r") as f2:
        books = json.loads(f1.read())
        users = json.loads(f2.read())

        for i in range(len(users)):
            if i < len(books):
                users[i].update({"books": [books[i]]})
            else:
                users[i].update({"books": []})

    with open(file_out, 'w') as write:
        json.dump(users, write, indent=4)


csv_to_json("../files/books.csv", "../files/books.json")
json_to_template("../files/books.json", "../files/users.json", "../files/result.json")
