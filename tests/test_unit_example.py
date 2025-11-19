def add_item_to_list(lst, item):
    if item:
        lst.append(item)
    return lst

def test_add_item_to_list():
    my_list = []
    assert add_item_to_list(my_list, "TestItem") == ["TestItem"]
    assert add_item_to_list(my_list, None) == ["TestItem"]
    assert add_item_to_list(my_list, "") == ["TestItem"]