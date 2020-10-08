import config

def test_load():
    assert config.load() == {'categories': ['Lindy', 'Birkin', 'Kelly', 'Bolide 27']}