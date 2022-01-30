import pandas as pd
import psycopg2
import csv


conn = psycopg2.connect(host="localhost",
                        database="TabelasFinais",
                        user="postgres",
                        password="password")

cursor = conn.cursor()

query1 = "SELECT * FROM entrada_apps_apps_treino_tratado"
cursor.execute(query1)
lista1=[]
for result in cursor.fetchall():
    lista1.append(result)

query2 = "SELECT * FROM entrada_apps_apps_validacao_tratado"
cursor.execute(query2)
lista2=[]
for result in cursor.fetchall():
    lista2.append(result)
    

conn.commit()
conn.close()




class connector_postgres:
    host = "34.151.204.5"
    database = "apps"
    user = "postgres"
    password = "password"

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




conect = connector_postgres()


for i in lista1:
    query1 = "INSERT INTO entrada_apps_apps_treino_tratado (instituicao, comentario, dataa, classificacao, elogio_quanto_ao_app, reclamacao_quanto_ao_app, elogio_a_instituicao, reclamacao_a_instituicao, nao_classificavel) VALUES('{}','{}','{}',{},'{}','{}','{}','{}','{}')".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])

    conect.inserir(query1)

for i in lista2:
    query2 = "INSERT INTO entrada_apps_apps_validacao_tratado (instituicao, comentario, dataa, classificacao, elogio_quanto_ao_app, reclamacao_quanto_ao_app, elogio_a_instituicao, reclamacao_a_instituicao, nao_classificavel) VALUES('{}','{}','{}',{},'{}','{}','{}','{}','{}')".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])

    conect.inserir(query2)