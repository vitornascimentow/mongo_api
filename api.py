from flask import Flask, redirect, request, url_for, jsonify
from pymongo import MongoClient

app = Flask(__name__)
conn = MongoClient('mongodb+srv://vitor:<bol>3105@cluster0.dbhybue.mongodb.net/magalu')
db = conn['magalu']

#CRUD

#CREATE 
## FORM

@app.route('/')
def home():
    return redirect(url_for('static', filename='cadastro.html'))

@app.route('/cadastro', methods=['GET'])
def cadastro():
    produto = request.args.to_dict()
    db.produtos.insert_one(produto)
    # colocar um if para impedir cadastrar o mesmo produto 2 vezes
    del produto['_id']
    return produto


# Read

# Update
## Form

# Delete

if __name__ == '__main__':
    app.run(debug=True)