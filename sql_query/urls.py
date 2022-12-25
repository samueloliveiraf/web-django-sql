from django.urls import path
from .views import insert_table_sql_query


urlpatterns = [
    path('insert/', insert_table_sql_query, name='insert_table_game'),
]
