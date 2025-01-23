"""Excerise one tea party __author__"""

__author__: str = "123456789"


def main_planner(guests: int) -> None:
    """Beginning entry point for tea party"""

    print("A Cozy Tea Party for " + str((guests)) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Tells the number of tea bags needed based on the amount of guests attending"""
    return 2 * people


def treats(people: int) -> int:
    """Gives 1.5 treats for each guest, based on how many people there are"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Put in tea count and treat count and then return cost of them"""
    return (0.50 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
