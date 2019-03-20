def mejorar_receta(pizza, topping):
    """
    (list of str, str) -> list of str

    Agrega un nuevo ingrediente a la pizza

    >>> mejorar_receta(['queso', "jamon"], "champiñon")
    ['champiñon', 'jamon', 'queso']
    >>> mejorar_receta(['queso', "jamon"], "jamon")
    ['jamon', 'queso']

    :param pizza: list of str La pizza actual
    :param topping: str El topping a agregar
    :return: La pizza con el nuevo topping ordenada
    """
    nueva_pizza = pizza.copy()
    if not (topping in pizza):
        nueva_pizza.append(topping)
    return sorted(nueva_pizza)


def doble_queso(pizza):
    """
    (list of str) -> list of str

    Agrega queso al principio y final de la pizza si no tiene

    >>> doble_queso(['queso', "jamon"])
    ['queso', 'jamon', 'queso']
    >>> doble_queso(["jamon", 'queso'])
    ['queso', 'jamon', 'queso']
    >>> doble_queso(["jamon"])
    ['queso', 'jamon', 'queso']
    >>> doble_queso(['queso', "jamon", 'queso'])
    ['queso', 'jamon', 'queso']

    :param pizza: list of str la pizza a adicionar
    :return: pizza con doble queso
    """
    nueva_pizza = pizza.copy()
    if not ('queso' == nueva_pizza[0]):
        nueva_pizza.insert(0, 'queso')
    if not ('queso' == nueva_pizza[-1]):
        nueva_pizza.append('queso')
    return nueva_pizza