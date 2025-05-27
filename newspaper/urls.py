from django.urls import path
from newspaper import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
    path(
        "post-by-category/<int:category_id>/",
        views.PostByCategoryView.as_view(),
        name="post-by-category",
    ),
    path("tag-list/", views.TagListView.as_view(), name="tag-list"),
    path("category-list/", views.CategoryListView.as_view(), name="category-list"),
    path("contact/", views.ContactCreateView.as_view(), name="contact"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("comment/", views.CommentView.as_view(), name="comment"),
    path("newsletter/", views.NewsletterView.as_view(), name="newsletter"),
    path("search/", views.PostSearchView.as_view(), name="search"),
    path("about/", views.AboutView.as_view(), name="about"),
]
