import pandas as pd
import psycopg2
import csv


arquivos = []
df_apps_treino = pd.read_csv(
    'entrada_APPS_Apps_Treino.csv',
    sep=";",
    encoding='utf-8')

# print(df_apps_treino)

list_apps_treino = df_apps_treino.values.tolist()

# print(list_apps_teste[:10])

class connector_postgres:
    host = "localhost"
    database = "TabelasFinais"
    user = "postgres"
    password = "deg2205"

    def conectar(self):
        conn = psycopg2.connect(host=self.host,
                                database=self.database,
                                user=self.user,
                                password=self.password)
        cursor = conn.cursor()

        return conn, cursor

    def desconectar(self, conn, cursor):
        cursor.close()
        conn.commit()
        conn.close()

    def inserir(self, query):
        conn, cursor = self.conectar()
        cursor.execute(query)
        self.desconectar(conn, cursor)

    def selecionar(self, query):
        conn, cursor = self.conectar()
        cursor.execute(query)
        lista = []
        for result in cursor.fetchall():
            lista.append(result)
        self.desconectar(conn, cursor)
        return lista

    def update(self, query):
        conn, cursor = self.conectar()
        cursor.execute(query)
        self.desconectar(conn, cursor)

    def delete(self, query):
        conn, cursor = self.conectar()
        cursor.execute(query)
        self.desconectar(conn, cursor)


conect = connector_postgres()

for i in list_apps_treino:
    query = "INSERT INTO entrada_apps_apps_treino (instituicao, comentario, dataa, classificacao, elogio_quanto_ao_app, reclamacao_quanto_ao_app, elogio_a_instituicao, reclamacao_a_instituicao, nao_classificavel) VALUES('{}','{}','{}',{},'{}','{}','{}','{}','{}')".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])

    conect.inserir(query)
