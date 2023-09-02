from django.conf import settings

import aspose.words as convert

import string , random

from .models import SubjectCategory , SubjectItem



# Рандомизация букв для уникального имени файла
def random_letters ():
    letters = string.ascii_lowercase
    random_str = ''.join (random.choice(letters) for i in range(8))
    return random_str



 # Запись файла в папку со статикой
def file_processing (f , filename):
    with open (f'{settings.BASE_DIR}\\workflow\\static\\workflow\\documents\\{filename}' , 'wb+') as file:
        for chunk in f.chunks ():
            file.write (chunk)
        return f'{filename}'



# Конвертация из DOCX в PDF
def convert_to_pdf (file , filename):
    
    doc = convert.Document (f'{settings.BASE_DIR}\\workflow\\static\\workflow\\documents\\{file}')

    name_file = filename.split('.')[0]

    doc.save (f'{settings.BASE_DIR}\\workflow\\static\\workflow\\documents\\{name_file}.pdf') 
    
    return f'{name_file}.pdf'


