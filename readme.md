## Exploração de 2 bases de dados diferentes
 ### Esse trabalho consiste em:
1. Restaurar 1 dump do MySql e 1 dump do PostgreSQL
2. Explorar os dados usando Jupyter Notebook com as bibliotecas Python: Pandas, Matplotlib e PLotly
3. Criar um backend usando Flask + Swagger que forneça os dados para visualizações no frontend
4. Criar um frontend usando React + Plotly para a apresentação de um relatório web 

### 1. Restaurando os dumps
* Instalar o PostgreSQL 12.2
* Instalar o MySQL 8.0.18.0
* Criar um banco 'teste' no Postgres
* Criar um banco 'teste' no Mysql
* Executar o seguinte comando na linha de comando para restaurar o banco do Postgres
```console
foo@bar:~$ psql -U postgres teste < dados/PostgreSQL-dump-store-202002051505.sql
foo
```
* Executar o seguinte comando na linha de comando para restaurar o banco do MySQL
```console
foo@bar:~$ mysql -h 127.0.0.1 -u root -p teste < dados.MYSQL_tasks_05-02-20_data.sql
foo
```

### 1. Explorando os dados usando Jupyter Notebook

Essa exploração foi feita através deste notebook: 