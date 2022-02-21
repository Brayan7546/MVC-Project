
   
from model import Author
from model import Document
import view

def start():
    view.menu_view()
    _input = input()
    #if _input == '1':
    
    if _input == '2':
        return show_documents()
    if _input == '4':
        return show_authors()
    else:
        print('opcion invalida')

def show_authors():
    #gets list of all authors objects
    authors_in_db = Author.get_all()
    #calls view
    return view.show_authors_view(authors_in_db)


def start_authors():
    view.start_authors_view()
    _input = input()
    if _input == 'y':
        return show_authors()
    else:
        return view.end_view()


if __name__ == "__main__":
    view.menu_view()
    
      
    
      
def show_documents():
    #gets list of all Documents objects
    documents_in_db = Document.get_all()
    #calls view
    return view.show_documents_view(documents_in_db)

def start_documents():
    view.start_documents_view()
    _input = input()
    if _input == 'y':
        return show_documents()
    else:
        return view.end_view()


if __name__ == "__main__":
    start()
