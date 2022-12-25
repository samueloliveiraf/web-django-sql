from django.shortcuts import render
from django.db import connection
import pandas as pd
from .models import SqlQuery


def insert_table_sql_query(request):
    query = request.POST.get('query')
    sucesso = 'deu bom!'

    sql = SqlQuery.objects.filter(id='1')

    try:
        df = pd.read_sql_query(query, connection)
        print(df)
    except Exception as e:
        print(e)
    return render(request, 'core/message.html', {'message': sucesso})


def select_table_game(request):
    pass


def update_table_game(request):
    pass


def delete_table_game(request):
    pass
