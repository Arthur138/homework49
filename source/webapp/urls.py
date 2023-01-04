from django.urls import path
from webapp.views import IndexView, DoingView, DoingUpdateView, DoingDeleteView, ProjectView, ProjectDetailView, \
    DoingCreateView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ChangeUserInProject

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('doings/<int:pk>/', DoingView.as_view(), name='doing_view'),
    path('doing/<int:pk>/update/', DoingUpdateView.as_view(), name='doing_update'),
    path('doing/<int:pk>/delete/', DoingDeleteView.as_view(), name='doing_delete'),
    path('projects/', ProjectView.as_view(), name='projects_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_view'),
    path('project/<int:pk>/doing/add', DoingCreateView.as_view(), name='project_doings_add'),
    path('project/create', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/add_users', ChangeUserInProject.as_view(), name='add_users'),

]
