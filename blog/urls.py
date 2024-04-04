from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [

    # blog/post_list_view
    path('', views.post_list_view, name='post_list_view'),
    
    # blog/post_detail_view?post_id=<some_id>
    # Requires <int:post_id> having same parameter name in views.post_detail_view()
    path('<int:post_id>/', views.post_detail_view, name='post_detail_view')
]