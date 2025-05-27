from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"tags", views.TagViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"posts", views.PostViewSet)
router.register(r"newsletters", views.NewsletterViewSet)
router.register(r"contacts", views.ContactViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path(
        "post-by-category/<int:category_id>/",
        views.PostListByCategoryView.as_view(),
        name="post-list-by-category-api",
    ),
    path(
        "draft-list/",
        views.DraftListView.as_view(),
        name="draft-list-api",
    ),
    path(
        "draft-detail/<int:pk>/",
        views.DraftDetailView.as_view(),
        name="draft-detail-api",
    ),
    path(
        "post-publish/",
        views.PostPublishViewSet.as_view(),
        name="post-publish-api",
    ),
    path(
        "post/<int:post_id>/comments/",
        views.CommentViewSet.as_view(),
        name="comment-list-api",
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
