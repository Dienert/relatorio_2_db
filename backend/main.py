from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restplus import Resource, Api, fields

import pandas as pd
import numpy as np

from calendar import monthrange
from datetime import date, datetime

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
api = Api(app)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

name_space = api.namespace('/', description='Relatorios')

tudo = pd.read_csv("../dados/tudo.csv")
tudo['updated_at'] = pd.to_datetime(tudo.updated_at, utc=True)
tudo.index = tudo.updated_at

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@name_space.route("/vendasanuais")
class VendasAnuais(Resource):
	def get(self):
		meses = tudo.groupby([tudo.index.year]).price_x.sum()
		return {'x': pd.Series(meses.index).astype(np.int32).to_list(), 
				'y': meses.to_list()}

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@name_space.route("/vendasmensais")
class VendasMensais(Resource):
	def get(self):
		vendas_por_mes = tudo.groupby([tudo.index.year,tudo.index.month]).price_x.sum()
		vendas_por_mes.index = pd.Series(vendas_por_mes.index.values).apply(lambda x:str(x[0])+'-'+str(x[1]))
		return {'x': vendas_por_mes.index.to_list(), 
				'y': vendas_por_mes.to_list()}

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@name_space.route("/vendasporhora")
class VendasPorHora(Resource):
	def get(self):
		compras_por_hora = tudo.groupby([tudo.index.hour]).price_x.sum()
		return {'x': compras_por_hora.index.to_list(), 
				'y': compras_por_hora.to_list()}

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@name_space.route("/vendaspordia")
class VendasPorDia(Resource):
	def get(self):
		receita_por_dia = tudo.groupby([tudo.index.weekday]).price_x.sum()
		dias = {0: 'Segunda', 1: 'Terça', 2: 'Quarta', 3: 'Quinta', 4: 'Sexta', 5: 'Sábado', 6: 'Domingo'}
		return {'x': list(map(lambda x: dias[x], receita_por_dia.index)), 
				'y': receita_por_dia.to_list()}

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@name_space.route("/produtosmaiscomprados")
class ProdutosMaisComprados(Resource):
	def get(self):
		mais_comprados = tudo.groupby(['product']).quantity.sum().sort_values(ascending=False)[:10].sort_values()
		return {'x': mais_comprados.to_list(), 
				'y': mais_comprados.index.to_list()}

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@name_space.route("/produtosmaiorreceita")
class ProdutosMaiorReceita(Resource):
	def get(self):
		mais_comprados = tudo.groupby(['product']).price_x.sum().sort_values(ascending=False)[:10].sort_values()
		return {'x': mais_comprados.to_list(), 
				'y': mais_comprados.index.to_list()}

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@name_space.route("/clientesmaisfrequentes")
class ProdutosMaisFrequentes(Resource):
	def get(self):
		clientes = tudo.groupby(['name']).sale_id.count().sort_values(ascending=False)[:10].sort_values()
		return {'x': clientes.to_list(), 
				'y': clientes.index.to_list()}

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@name_space.route("/clientesmaiscompram")
class ClientesMaisCompram(Resource):
	def get(self):
		clientes = tudo.groupby(['name']).price_x.sum().sort_values(ascending=False)[:10].sort_values()
		return {'x': clientes.to_list(), 
				'y': clientes.index.to_list()}

if __name__ == '__main__':
   app.run()