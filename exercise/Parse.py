import csv, sys
import pathlib
import database
import logging
import traceback


def Parse(filename):
    db = database.Database(':memory:')
    row_count = 0
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    row_count += 1
                    db.insert(row)
            except Exception as e:
                logging.error('Row discarded due an error. Row=%s. Exception=%s', row,traceback.format_exc())

        print('{} records inserted, total records are {}'.format(db.count(), row_count))

    finally:
        db.close()


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = '/home/flaviocavallin/projects/1/python-exercise/data/import.csv'
    Parse(filename)
