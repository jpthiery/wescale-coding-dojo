from rpgcatalog.character import Character


def test_character_begin_with_1000_point_health():
    steve = Character()

    assert steve.health == 1000
