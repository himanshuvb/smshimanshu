from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/', views.student_list, name="student_list"),
    path('student/add/', views.add_student, name="add_student"),
    path('student/<int:student_regno>/delete', views.student_delete, name="student_delete"),
    path('leaves/',views.ap_leaves,name="ap_leaves"),
    path('leaves/list/', views.leaves_details, name="leaves_details"),
    path('leaves/<int:leaves_regno>/manage/', views.manage_leaves, name="manage_leaves"),
    path('leaves/<int:leaves_regno>/disapprove/', views.disapprove_leaves, name="disapprove_leaves"),
    path('student/logoutsms', views.logoutsms, name="logoutsms"),

]