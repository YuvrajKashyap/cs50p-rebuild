from bank import value

def test_h():
    assert value("hi") == "$20"
    assert value("hoi") == "$20"
    assert value("heber") == "$20"

def test_hello():
    assert value("hello") == "$0"
    assert value("hellor") == "$0"
    assert value("hellomyguy") == "$0"

def test_else():
    assert value("weewoo") == "$100"
    assert value("nah") == "$100"
    assert value("bruh") == "$100"