from django.urls import path
from blog.views import PostView, CommentView, PostDetail


app_name = "blogs"

urlpatterns = [
    path("", PostView.as_view(), name="posts"),
    path("<int:pk>/post/", PostDetail.as_view(), name="detail"),
    path("<int:pk>/comment/", CommentView.as_view(), name="comment")
]