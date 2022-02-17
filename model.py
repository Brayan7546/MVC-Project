import csv
import json


class Author(object):

    def __init__(self, id_person=None, first_name=None, last_name=None):
        self.__id_person = id_person
        self.__first_name = first_name
        self.__last_name = last_name

    def name(self):
        return "%s %s" % (self.__first_name, self.__last_name)

    @classmethod
    def get_all(self):
        result = list()
        with open('db.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                person = Author(row['id_person'], row['first_name'], row['last_name'])
                result.append(person)
                line_count += 1
        return result

    class Document(object):

    def __init__(self, title=None, authors=None, pub_udate=None, id_book=None, edition=None, no_pag=None):
        self.__title = title
        self.__id_book = id_book
        self.__authors = authors
        self.__pub_udate = pub_udate
        self.__edition= edition
        self.__no_pag= no_pag
        

    @classmethod
    def get_all(self):
        result = list()
        with open('db.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                document = Document(row['title'], row['id_book'], row['authors'], row['pub_udate'], row['edition'],row['no_pag'])
                result.append(person)
                line_count += 1
        return result
