from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    chicken = Ingredient("frango")
    chicken_2 = Ingredient("frango")
    egg = Ingredient("ovo")

    assert chicken.name == "frango"
    assert egg.name == "ovo"

    assert chicken.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert egg.restrictions == {
        Restriction.ANIMAL_DERIVED
    }

    assert chicken.__eq__(chicken_2) is True
    assert chicken.__eq__(egg) is False

    assert hash(chicken) == hash(chicken_2)
    assert hash(egg) != hash(chicken_2)
    assert repr(chicken) == "Ingredient('frango')"
