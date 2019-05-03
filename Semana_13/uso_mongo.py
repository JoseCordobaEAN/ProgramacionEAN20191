from pymongo import MongoClient




cliente = MongoClient()

# print(cliente)

base = cliente.matrices

# print(base)

coleccion = base.matrices

# print(coleccion)

a_insertar = {
    'algo': 'una cosa',
    'otra': 'otra cosa'
}

coleccion.insert({
    'algo': 'una cosa',
    'otra': 'otra cosa'
})
#
# print(coleccion.find_one({'A'}))