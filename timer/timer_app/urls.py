from django.urls import path
from .views import views, topic, subtopic

app_name = 'timer'

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('topic/create/', topic.create_and_list_topic, name='create_and_list_topic'),
    path('topic/delete/<int:topic_id>', topic.delete_topic, name='delete_topic'),
    path('topic/edit/<int:topic_id>', topic.edit_topic, name='edit_topic'),
    path('subtopic/create-and-list/', subtopic.create_and_list_subtopic, name='create_and_list_subtopic'),
    path('subtopic/delete/<int:subtopic_id>', subtopic.delete_subtopic, name='delete_subtopic'),
    path('subtopic/edit/<int:subtopic_id>', subtopic.edit_subtopic, name='edit_subtopic'),
    path('session/start/', views.start_session, name='start session'),
]

