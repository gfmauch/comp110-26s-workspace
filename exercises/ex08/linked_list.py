from __future__ import annotations


class Node:
    """Node in a singly-linked list recursive structure."""
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialization self.value to value and self.next to next."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """String returning to create linked list."""
        if self.next is None:
            return f"{self.value} -> None"
        return f"{self.value} -> {self.next}"


def sum(head: Node | None) -> int:
    """Sum of value and next."""
    if head is None:
        return 0 
    return head.value + sum(head.next)


def value_at(head: Node | None, index: int) -> int:
    """Find value at head and determine if error or point in index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum value in the linked list."""
    if head is None:  # Base Case: Empty list.
        raise ValueError("Cannot call max with None")
    if head.next is None:  # Base Case: Last node in the list
        return head.value
        
    sub_max: int = max(head.next)  # Recursive Case: Find the max of the rest of the list
    return head.value if head.value > sub_max else sub_max


def linkify(items: list[int]) -> Node | None:
    """Converts a list of int into a linked list of Nodes."""
    if not items: 
        return None
    return Node(items[0], linkify(items[1:]))  # Create node with 1st item and link to rest



node_c: Node = Node(4, None)
node_b: Node = Node(0, node_c)
print(sum(node_b))
courses: Node = Node(110, Node(210, None))
print(courses)