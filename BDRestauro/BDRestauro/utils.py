from django.db import connection

def obter_utilizador(user_id, user_id_verificar):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM obter_utilizador_por_id(%s,%s)", [user_id, user_id_verificar])
        result = cursor.fetchone()
    return result


def listar_utilizadores(user_id_verificar):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM listar_utilizadores(%s)", [user_id_verificar])
        columns = [col[0] for col in cursor.description]
        utilizadores = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return utilizadores
        