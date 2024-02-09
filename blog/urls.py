from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name='starting-page'),
    path("posts", views.AllPostsView.as_view(), name='posts'),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name='post-detail-page'),
    path("post/<int:pk>/delete/", views.CommentDeleteView.as_view(), name='post-delete'),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("logoout/", views.exit, name="exit"),
    ]
