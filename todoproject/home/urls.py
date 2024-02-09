from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_page,name="login"),
    path('sign_up/',views.signup_page,name="sign_up"),
    path('log_out/',views.logout_page,name="log_out"),
    path('index/',views.todo_page,name="todo"),
    path('delete/int:<id>/',views.delete_todo,name='delete'),
    path('update/',views.update_todo,name='update'),
    path('edit/int:<id>/',views.edit_todo,name='edit'),
    path('edit_done/int:<id>/',views.edit_done,name='edit_done'),

    
]