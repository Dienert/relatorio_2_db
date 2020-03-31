## Exploração de 2 bases de dados diferentes
 ### Esse trabalho consiste em:
1. Restaurar 1 dump do MySql e 1 dump do PostgreSQL
2. Explorar os dados usando Jupyter Notebook com as bibliotecas Python: Pandas, Matplotlib e Plotly
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
```
* Executar o seguinte comando na linha de comando para restaurar o banco do MySQL
```console
foo@bar:~$ mysql -h 127.0.0.1 -u root -p teste < dados/MYSQL_tasks_05-02-20_data.sql
```

### 2. Explorando os dados usando Jupyter Notebook
* Executar a exploração feita no Jupyter Notebook: [Explocação Inicial.ipynb](https://github.com/Dienert/relatorio_2_db/blob/master/Explora%C3%A7%C3%A3o%20inicial.ipynb)
* **Obs. 1:** Para que os gráficos usando Plotly apareçam é necessário executar o notebook localmente.
* **Obs. 2:** No fim do notebook é gerado o arquivo **dados/tudo.csv** que é usado pelo backend

### 3. Rodando o Backend
* Instalar as dependências do backend com o seguinte comando:
```console
foo@bar:~$ pip install -r backend/requirements.txt
```
* Configurar a variável de ambiente (windows):
```console
C:\>set FLASK_APP=main
```
* Configurar a variável de ambiente (linux):
```console
foo@bar:~$ export FLASK_APP=main
```
* Iniciar o backend com os seguintes comandos:
```console
foo@bar:~$ cd backend
foo@bar:~$ flask run
```
* Verificar os endpoints da API no endenreço: http://localhost:5000/

### 4. Rodando o Frontend
* Instalar o [Node.js](https://nodejs.org/en/)
* Instalar as dependências do Frontend com os seguintes comandos:
```console
foo@bar:~$ cd frontend
foo@bar:~$ npm install
```
* Iniciar o frontend com o seguinte comando:
```console
foo@bar:~$ npm start
```
* Iniciar a aplicação no endereço: http://localhost:3000/
* Um pdf da tela do frontend está disponível [aqui](https://github.com/Dienert/relatorio_2_db/blob/master/relatorio.pdf).
* **Obs.:** Em todos os gráficos é possível selecionar uma faixa específica dos dados clicando com o mouse e arrastando. Essa funcionalidade é bem útil principalmente para o gráfico de Vendas por Mês que possui muitas informações. Sendo possível visualizar meses específicos, dessa forma:

<p align="center"> 
<img src="https://raw.githubusercontent.com/Dienert/relatorio_2_db/master/imagens/venas_por_mes.gif">
</p>
