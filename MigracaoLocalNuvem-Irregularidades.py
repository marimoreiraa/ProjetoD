import pandas as pd
import psycopg2
import csv

#Conexão com o Postgers LOCAL

conn = psycopg2.connect(host="localhost",
                        database="TabelasFinais",
                        user="postgres",
                        password="12ana20Mari.")

cursor = conn.cursor()

query1 = "SELECT * FROM irreg_2014_2016"
cursor.execute(query1)
lista1=[]
for result in cursor.fetchall():
    lista1.append(result)

query2 = "SELECT * FROM irreg_2017_2021"
cursor.execute(query2)
lista2=[]
for result in cursor.fetchall():
    lista2.append(result)
    

conn.commit()
conn.close()



#Conecta com o Postgres da NUVEM
class connector_postgres:
    host = "34.151.204.5"
    database = "Irregularidades"
    user = "postgres"
    password = "secret"

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

'''
for i in lista1:
    query = "INSERT INTO irreg_2014_2016(ano,semestre,categoria,tipo,instituicao, irregularidade,qtd_reclamacoes_reguladas_procedentes,qtd_reclamacoes_reguladas_outras,qtd_reclamacoes_nao_reguladas,qtd_total_reclamacoes) VALUES({},'{}','{}','{}','{}','{}',{},{},{},{})".format(
        i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])

    conect.inserir(query)'''

agoraVai = lista2[38184:]

for i in agoraVai:
    query = "INSERT INTO irreg_2017_2021 (ano,trimestre,categoria,tipo,instituicao, irregularidade,qtd_reclamacoes_reguladas_procedentes,qtd_reclamacoes_reguladas_outras,qtd_reclamacoes_nao_reguladas,qtd_total_reclamacoes) VALUES({},'{}','{}','{}','{}','{}',{},{},{},{})".format(
        i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])

    conect.inserir(query)   
