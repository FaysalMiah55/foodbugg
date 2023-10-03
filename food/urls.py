from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # food/
    # path("", views.index, name="index"),
    path('', views.IndexClassViews.as_view(), name="index"),
    # food/id
    # path("<int:item_id>/", views.detail, name="detail"),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path("about/", views.about, name="about"),
    # add item
    path("add/", views.createItem, name="createItem"),
    # update item
    path("update/<int:id>/", views.updateItem, name='updateItem'),
    # delete item
    path("delete/<int:id>/", views.deleteItem, name="deleteItem"),
]
