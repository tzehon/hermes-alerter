import config

def test_load():
    assert config.load() == {'sports': ['Lindy', 'Birkin', 'Kelly', 'Bolide 27']}