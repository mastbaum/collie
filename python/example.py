import sys
import uuid
import random

import db

# views
def all_by_num1(doc):
    if doc['type'] == 'test':
        return [doc['num1']], doc

# filters
def small(row):
    if row[1][1]['num1'] < 5:
        return True
    return False

# main
def main():
    collie = db.CollieDB()

    collie.views['all_by_num1'] = {'map': all_by_num1}
    collie.filters['small'] = small

    for i in range(10):
        doc = {'id': uuid.uuid4().hex, 'num1': random.randint(0,10), 'num2': random.randint(0,5), 'type': 'test'}
        collie.append(doc)

    print 'Documents'
    for doc in collie:
        print doc

    view_rows = collie.view('all_by_num1')

    print
    print 'View rows'
    for row in view_rows:
        print row

    view_rows = collie.view('all_by_num1', filt='small')

    print
    print 'Filtered view rows'
    for row in view_rows:
        print row

if __name__ == '__main__':
    main()

