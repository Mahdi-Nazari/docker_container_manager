from django.urls import path

from .views import (
    create_container,
    create_multiple_container,
    delete_container,
    get_all_containers,
    get_container_by_name,
    get_container_logs_by_name,
    update_container,
)

urlpatterns = [
    path("all/", get_all_containers),
    path("single/<str:name>/", get_container_by_name),
    path("logs/<str:name>/", get_container_logs_by_name),
    path("create/", create_container),
    path("create/multiple/<str:name>/", create_multiple_container),
    path("update/<str:name>/", update_container),
    path("delete/<str:name>/", delete_container),
]
