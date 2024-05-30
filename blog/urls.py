from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post
from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryPageView, CategoryListView, LikeView, AddCommentView


urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('article/<int:pk>', PostDetailView.as_view(), name='article'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='edit'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:category>/', CategoryPageView, name='category_page'),
    path('category_list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment')
]

