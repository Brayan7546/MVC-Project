
   
from model import Author
from model import Document
import view

def show_authors():
    #gets list of all authors objects
    authors_in_db = Author.get_all()
    #calls view
    return view.show_authors_view(authors_in_db)


def start_authors():
    view.start_view()
    _input = input()
    if _input == 'y':
        return show_authors()
    else:
        return view.end_view()


if __name__ == "__main__":
    start()
      
    
      
def show_documents():
    #gets list of all Documents objects
    document_in_db = Document.get_all()
    #calls view
    return view.show_document_view(document_in_db)

def start_documents():
    view.start_documents_view()
    _input = input()
    if _input == 'y':
        return show_documents()
    else:
        return view.end_view()


if __name__ == "__main__":
    start()
