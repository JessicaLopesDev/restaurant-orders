# Req 3
from csv import DictReader
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.reader()

    def reader(self):
        all_dishes = {}
        with open(self.source_path, encoding="utf-8") as file:
            for item in DictReader(file):
                name = item['dish']

                if name not in all_dishes:
                    all_dishes[name] = Dish(name, float(item['price']))

                all_dishes[name].add_ingredient_dependency(
                    Ingredient(item['ingredient']), int(item['recipe_amount'])
                )

        return set(all_dishes.values())
