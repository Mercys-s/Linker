from rest_framework import serializers

from django.utils.text import slugify
from transliterate import translit

from workflow.models import SubjectItem , SubjectCategory
from workflow.extra_functions import file_processing , convert_to_pdf , random_letters



class WorkflowCategorySerializer (serializers.ModelSerializer):

    class Meta:
        model = SubjectCategory
        fields = ('id' , 'title')



class WorkflowSerializer (serializers.ModelSerializer):
    
    author = serializers.CharField (default = serializers.CurrentUserDefault())
    slug = serializers.SlugField (required = False)
    docx_file = serializers.FileField (required = True) 
    pdf_file = serializers.HiddenField (default = '')

    class Meta:
        model = SubjectItem
        fields = ('title' , 'theme' , 'note' , 'author' , 'category' , 'slug' , 'id'  , 'docx_file' , 'pdf_file')


    def create (self , validated_data):
        
        letters = random_letters()

        validated_data ['slug'] = slugify ( translit (validated_data ['title'] , 'ru' , reversed = True))

        # Обработка пришедшего Docx с API
        validated_data ['docx_file'] = file_processing (f = validated_data ['docx_file'] ,\
                                                        filename = letters + str (validated_data ['docx_file']) )

        # Конвертирование в PDF формат
        validated_data ['pdf_file'] = convert_to_pdf (file = validated_data ['docx_file'] ,\
                                                      filename = str (validated_data ['docx_file']) )

        # Переопределение директории файла для БД 
        validated_data ['docx_file'] = 'static/workflow/documents/' + validated_data ['docx_file'] 

        return SubjectItem.objects.create (**validated_data) 


        
    

