from django.urls import path
from . views import *

urlpatterns = [
    path('home/',home),
    path('home/',home),
    path('add_student/',student_add),
    path('delete-student/<int:roll>',delete_student),
    path('update-student/<int:roll>',update_student),
    
]