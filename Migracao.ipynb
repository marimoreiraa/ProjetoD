import pandas as pd
import psycopg2
import csv

df1 = pd.read_csv('entrada_BC-Irregularidades_2014_Irregularidades_2Semestre2014.csv',
                  sep=";",encoding='utf-8')
lista1 = df1.values.tolist()

class connector_postgres:
    host = "localhost"
    database = "TabelasFinais"
    user = "postgres"
    password = "12ana20Mari."

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
    query = "INSERT INTO Irreg2021_3 (ano,semestre,categoria,tipo,cnpj,instituicao_financeira, irregularidade,quantidade_reclamacoes_reguladas_procedentes,quantidade_reclamacoes_reguladas_outras,quantidade_reclamacoes_nao_reguladas,quantidade_total_reclamacoes) VALUES({},'{}','{}','{}','{}','{}','{}',{},{},{},{})".format(
        i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
    conect.inserir(query)

print("Migração Completa!")
