
   
from model import Person
from model import Document
import view

def show_persons():
    #gets list of all Person objects
    people_in_db = Person.get_all()
    #calls view
    return view.show_all_view(people_in_db)


def start():
    view.start_view()
    _input = input()
    if _input == 'y':
        return show_all()
    else:
        return view.end_view()


if __name__ == "__main__":
    start()
      
def show_documents():
    #gets list of all Documents objects
    document_in_db = Document.get_all()
    #calls view
    return view.show_all_view(document_in_db)

