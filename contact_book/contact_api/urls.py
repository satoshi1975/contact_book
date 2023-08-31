from django.urls import path
from .views import (ContactListCreateView, ContactRetrieveUpdateDeleteView,
                   ContactSearchByNameView, ContactSearchByLastNameView,)


urlpatterns = [
    path('contacts/', ContactListCreateView.as_view(),
         name='contact-list'),  # вывод всех контактов
    path('contacts/<int:pk>/', ContactRetrieveUpdateDeleteView.as_view(),  # вывод, изменение, удаление контакта по id
         name='contact-detail'),
    path('contacts/search/name/', ContactSearchByNameView.as_view(),  # поиск контактов по имени
         name='contact-search-name'),
    path('contacts/search/last_name/', ContactSearchByLastNameView.as_view(),  # поиск контактов по фамилии
         name='contact-search-last-name'),
]
