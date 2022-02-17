from model import Author
from model import Document

def show_authors_view(list):
    print('In our db we have %i users. Here they are:' % len(list))
    for item in list:
        print(item.name())


def start_authors_view():
    #print('MVC - the simplest example')
    print('Do you want to see all the authors in my db?[y/n]: ')


def end_view():
    print('Goodbye!')
