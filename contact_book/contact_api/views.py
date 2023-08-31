from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from .models import Contact
from .serializers import ContactSerializer
from .exceptions import ContactNotFound

class CustomPagination(PageNumberPagination):
    '''класс кастомной пагинации'''
    page_size = 10
    page_size_query_param = 'page_size' # количество элементов на странице
    max_page_size = 100
    page_query_param = 'page' #номер страницы
    ordering = 'id' 


class ContactListCreateView(generics.ListCreateAPIView):
    """Вывод всех контактов из базы и создание нового контакта"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        email = request.data.get('email')

        # Проверка на уникальность номера телефона и электронной почты
        if Contact.objects.filter(phone=phone).exists():
            raise ValidationError({"error": ["This phone number is already used."]})
        if Contact.objects.filter(email=email).exists():
            raise ValidationError({"error": ["This email is already used."]})

        return super().create(request, *args, **kwargs)



class ContactRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Получение, изменение и удаление контакта по id"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
     
    def get_object(self):
        contact_id = self.kwargs.get('pk')
        try:
            return Contact.objects.get(pk=contact_id)
        except Contact.DoesNotExist:
            raise ContactNotFound()

    def update(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        email = request.data.get('email')

        # Проверка на уникальность номера телефона и электронной почты
        if Contact.objects.filter(phone=phone).exists():
            raise ValidationError({"error": ["This phone number is already used."]})
        if Contact.objects.filter(email=email).exists():
            raise ValidationError({"error": ["This email is already used."]})

        return super().create(request, *args, **kwargs)

        
class ContactSearchByNameView(generics.ListAPIView):
    """поиск контактов по имени"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    pagination_class = CustomPagination

    def get_queryset(self): # получение списка объектов по введенному имени 
        search_query = self.request.query_params.get('query', None)
        if search_query:
            queryset = Contact.objects.filter(first_name__icontains=search_query)
            if len(queryset)==0: # возвращение исключения при неудачном поиске
                raise ContactNotFound()
        return queryset

    
class ContactSearchByLastNameView(generics.ListAPIView):
    """поиск контактов по фамилии"""
    serializer_class = ContactSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self): # получение списка объектов по введенной фамилии
        search_query = self.request.query_params.get('query', None)
        if search_query:
            queryset = Contact.objects.filter(last_name__icontains=search_query)
            if len(queryset)==0: # возвращение исключения при неудачном поиске
                raise ContactNotFound()
        return queryset
