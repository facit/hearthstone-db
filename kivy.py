import os
import sys
import sqlite3
import kivy
from optparse import OptionParser

def parseOptions():
    parser = OptionParser()
    parser.add_option("-d", "--database", dest="database",
                      help="write report to FILE", metavar="FILE")
    (options, args) = parser.parse_args()
    if options.database is None:
        databases = []
        for item in os.listdir():
            if item.endswith(".db"):
                databases.append(item)
        if len(databases) == 1:
            options.database = databases[0]
        else:
            sys.exit("What database file should be used? Use -d flag to define this.")
    if not os.path.isfile(options.database):
        sys.exit("No such file \"" + options.database + "\"")

    return (options, args)

def main(options):
    conn = sqlite3.connect(options.database)
    c = conn.cursor()
    c.execute("SELECT * FROM cards")
    print(c.fetchone())

if __name__ == "__main__":
    (options, args) = parseOptions()
    main(options)
