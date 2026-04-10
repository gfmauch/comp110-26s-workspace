"""Program to help me host a tea party, and understand everything I will need."""


__author__: str = "730822602"

def main_planner(guests: int) -> None:
    """Overview of all the tea party needs."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(people=guests), treat_count=(treats(people=guests)))))
    
def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed for a tea party."""
    bags_needed: int = people * 2
    return bags_needed

def treats(people: int) -> int:
    """Calculate the number of treats needed for the tea party."""
    treats_needed: float = tea_bags(people=people) * 1.5
    return int(treats_needed)

def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of tea bags and treats for the tea party."""
    tea_cost: float = tea_count * 0.50
    treat_cost: float = treat_count * 0.75
    return tea_cost + treat_cost

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))