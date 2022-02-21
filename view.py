from model import Author
from model import Document

def menu_view():
    print('1. Agregar un Documento')
    print('2. Mostrar documentos')
    print('3. Agregar autores')
    print('4. Mostrar Autores')
    

def show_authors_view(list):
    print('In our db we have %i users. Here they are:' % len(list))
    for item in list:
        print(item.name())

def show_documents_view(list):
    print('In our db we have %i documents. Here they are:' % len(list))
    for item in list:
        print(item.title())

def start_authors_view():
    #print('MVC - the simplest example')
    print('Do you want to see all the authors in my db?[y/n]: ')


def end_view():
    print('Goodbye!')
