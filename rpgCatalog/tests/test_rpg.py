from rpgcatalog.character import Character


def test_character_begin_with_1000_point_health():
    steve = Character()

    assert steve.health == 1000


def test_character_begin_with_level_1():
    steve = Character()

    assert steve.level == 1


def test_character_begin_alive():
    steve = Character()

    assert steve.alive
