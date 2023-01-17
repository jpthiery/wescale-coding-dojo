from rpgcatalog.character import Character, hit
import pytest


def test_character_begin_with_1000_point_health():
    steve = Character()

    assert steve.health == 1000


def test_character_begin_with_level_1():
    steve = Character()

    assert steve.level == 1


def test_character_begin_alive():
    steve = Character()

    assert steve.alive


def test_character_receive_damage():
    steve = Character()
    hit(steve, damage=20)

    assert steve.health == 980


def test_character_receive_more_damage():
    steve = Character()
    hit(steve, damage=100)

    assert steve.health == 900


@pytest.mark.parametrize("damage", [1000, 1001, 1100])
def test_character_receive_more_damage_than_my_life(damage):
    steve = Character()
    hit(steve, damage=damage)

    assert not steve.alive


def test_character_hurts_receive_more_damage_than_his_life():
    steve = Character(health=100)
    hit(steve, damage=300)

    assert not steve.alive
