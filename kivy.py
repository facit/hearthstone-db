import sqlite3
import kivy
import optparse

def parseOptions():
    parser.add_option("-d", "--database", dest="database",
                      help="write report to FILE", metavar="FILE")

def main():
    conn = sqlite3.connect('C:\\Users\\Pontus\\Documents\\workspace\\HSDeckBuilder\\hearthstone-db\\all-cards.db')
    c = conn.cursor()

if __name__ == "__main__":
    (args, optione) = parseOptions()
    main()
