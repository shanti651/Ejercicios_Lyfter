import random
from bubble_sort1 import bubble_sort1

def test_bubble_sort_with_small_list():
    list_input = [5, 2, 8, 1]

    result = bubble_sort1(list_input)

    assert result == [1, 2, 5, 8]


def test_bubble_sort_with_large_list():
    lista_grande = [random.randint(1, 1000) for _ in range(100)]
    resultado_esperado = sorted(lista_grande) 
    
    resultado = bubble_sort1(lista_grande)
    
    assert resultado == resultado_esperado


def test_bubble_sort_with_empty_list():
    empty_list = []

    result = bubble_sort1(empty_list) 
    
    assert result == []

def test_bubble_sort_with_a_parameter_that_is_not_a_list():
    dictionary = {2,7,4,6}

    result = bubble_sort1(dictionary) 
    
    assert result == {2,4,6,7}
