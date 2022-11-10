from pymongo import MongoClient 
from pprint import pprint
import pandas as pd

# #CRUD
# #CONEXÃO
cliente = MongoClient('mongodb+srv://vitor:<bol>3105@cluster0.dbhybue.mongodb.net/magalu')
db = cliente['magalu']

# # CONSULTA (READ)
# cursor = db.alunos.find({})
# resultado = list(cursor)
# pprint(resultado)

# # SALVAR CONSULTA (PANDAS)
# df = pd.DataFrame(resultado).set_index('_id')
# print(df)

# # SALVAR CONSULTA EM ARQUIVO 
# df.to_json('mongo.json', orient='records')

#LENDO O JASON EM PANDAS
# df = pd.read_json('mongo.json')
# print(df)

#CONSULTANDO
cursor = db.alunos.find({'Nome': 'José Vitor'})
resultado = list(cursor)
pprint(resultado)

#MODIFICANDO E ATUALIZANDO (SET AND UPDATE)
db.alunos.update_one(
    {'Nome':'José Vitor'},
    {'$set':
        {'Idade':resultado[0]['Idade'] - 6}
    }
)

#CONSULTANDO POS UPDATE
cursor = db.alunos.find({'Nome': 'José Vitor'})
resultado = list(cursor)
pprint(resultado)