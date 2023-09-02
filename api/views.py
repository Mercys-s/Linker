from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .permissions import *

from workflow.models import SubjectItem , SubjectCategory 

from rest_framework.response import Response
from rest_framework.decorators import action


class WorkflowViewSet (viewsets.ModelViewSet):
    queryset = SubjectItem.objects.all()
    serializer_class = WorkflowSerializer

    def get_permissions(self):

        if self.action == 'list'\
        or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]

        else:
            permission_classes = [IsAuthorOrDenied]

        return [permission() for permission in permission_classes]



    @action (methods = ['get'] , detail = False)
    def category_list (self , request):
        queryset = SubjectCategory.objects.all ()
        serializer = WorkflowCategorySerializer (queryset , many = True)
        return Response ({'categories': serializer.data})


