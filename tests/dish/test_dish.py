import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 2
def test_dish():
    strogonoff = Dish("Strogonoff de carne", 30.0)
    strogonoff_2 = Dish("Strogonoff de carne", 30.0)
    ravioli = Dish("Ravioli", 20.0)

    assert strogonoff.name == "Strogonoff de carne"
    assert ravioli.name == "Ravioli"

    assert hash(strogonoff) == hash(strogonoff_2)
    assert hash(strogonoff) != hash(ravioli)

    assert strogonoff.__eq__(strogonoff_2) is True
    assert strogonoff.__eq__(ravioli) is False

    assert repr(strogonoff) == "Dish('Strogonoff de carne', R$30.00)"

    with pytest.raises(TypeError):
        Dish(30.0, "Strogonoff de carne")
    with pytest.raises(ValueError):
        Dish("Strogonoff de carne", 0)

    strogonoff.add_ingredient_dependency(Ingredient("carne"), 1)
    strogonoff.add_ingredient_dependency(Ingredient("creme de leite"), 1)
    strogonoff.add_ingredient_dependency(Ingredient("caldo de carne"), 1)

    assert strogonoff.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert strogonoff.get_ingredients() == {
        Ingredient("carne"),
        Ingredient("creme de leite"),
        Ingredient("caldo de carne"),
    }
