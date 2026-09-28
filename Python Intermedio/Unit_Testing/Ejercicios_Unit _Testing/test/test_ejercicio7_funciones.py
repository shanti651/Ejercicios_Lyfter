from ejercicio7_funciones import function

def test_ejercicio7_funciones():
    number = [1, 4, 6, 7, 13, 9, 67]

    result = function(number)

    assert result == [7,13, 67]