from ejercicio5_funciones import function

def test_ejercico5_funciones_with_a_sentence():
    sentence = "My name is Santiago Torrijos"

    result = function(sentence)

    assert result == (3, 21)