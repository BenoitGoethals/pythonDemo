from domain import Item


def test_item():
    assert Item("benoit",10).name == "benoit"