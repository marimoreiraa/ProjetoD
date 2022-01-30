# ProjetoD

O projeto teve como objetivo:
* Carregar os datasets em um DB Postgres Local e em um DataLake em Nuvem
* Utilize triggers e procedures para realizar uma pré-normalização
* Criar um código em python que conectassee o Postgres Local a um Postgres instanciado na nuvem, para a migração das tabelas
* Migrar as tabelas do Banco Relacional da Nuvem para os notebooks jupyter, e tratar os dados com Pandas
* Criar uma instancia na nuvem com o Banco Não-Relacional Cassandra, e utiliza-lo como DataWarehouse
* Migrar as tabelas normalizadas para o Cassandra
* Utilizar Spark para ler a DB Cassandra e gerar os insights iniciais 
* Salvar as tabelas normalizadas em formato parquet e salvar no DataLake Cloud Storage da GCP
* Utilizar o BigQuery também como DataWarehouse e para gerar as analises finais
* Conectar o BigQuery com o DataStudio, e trazer as analises finais em um DashBoard

## WorkFlow - ETL
> ![WorkFlow-ETL](https://user-images.githubusercontent.com/82787741/151703685-7175ad92-1811-47ef-b455-723c139408c5.jpg)

## Notebook MigraçãoLocal
Lê as tabelas locais em formato de dataframe, conecta com o Postgres Local e insere nas tabelas, ativando o Trigger e Procedure

## Notebook MigraçãoLocalNuvem
Conecta com o Postgres Local, armazena os dados retornados da query em uma lista, Conecta com o Postgres da Nuvem, e migra os dados da lista nas tabelas da nuvem.

## Notebook Pandas
Conecta com o Postgres da Nuvem, armazena os dados retornados da query em uma lista, e em seguida em um DataFrame. Logo após, os dataframes são analisados e tratados. E por fim, conecta com a intancia onde o Cassandra esta instalado, e migra os dados normalizados para as tabelas do Banco Não-Relacional.

## Notebook Pyspark
Conecta com a intancia onde o Cassandra esta instalado, armazena os dados retornados da query em uma lista, e em seguida em um DataFrame. Logo após, os dataframes são analisados para gerar pré-insights. E por fim, a tabela normalizada é salva no Cloud Storage em formato Parquet.


