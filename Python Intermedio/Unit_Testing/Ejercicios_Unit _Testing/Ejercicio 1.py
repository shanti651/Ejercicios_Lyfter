from bubble_sort1 import bubble_sort

def test_bubble_sort_with_small_list():
    list_input = [5, 2, 8, 1]

    result = bubble_sort(list_input)

    assert result == [1, 2, 5, 8]