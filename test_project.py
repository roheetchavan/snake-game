import pytest
from project import create_food, move_snake, check_collision, check_eat_food

def test_create_food():
    # Mock snake body and screen dimensions
    snake_body = [[5, 5], [5, 6], [5, 7]]
    sh, sw = 20, 20

    # Create food multiple times and check if it's not on the snake
    for _ in range(100):
        food = create_food(snake_body, sh, sw)
        assert food not in snake_body
        assert 1 <= food[0] < sh
        assert 1 <= food[1] < sw

def test_move_snake():
    # Test moving in different directions
    assert move_snake([[5, 5]], 258) == [6, 5]  # Down
    assert move_snake([[5, 5]], 259) == [4, 5]  # Up
    assert move_snake([[5, 5]], 260) == [5, 4]  # Left
    assert move_snake([[5, 5]], 261) == [5, 6]  # Right

def test_check_collision():
    # Test collision with walls and self
    assert check_collision([[0, 5]], 10, 10)  # Collision with top wall
    assert check_collision([[10, 5]], 10, 10)  # Collision with bottom wall
    assert check_collision([[5, 0]], 10, 10)  # Collision with left wall
    assert check_collision([[5, 10]], 10, 10)  # Collision with right wall
    assert check_collision([[5, 5], [5, 6], [5, 5]], 10, 10)  # Collision with self

def test_check_eat_food():
    # Test eating food
    assert check_eat_food([5, 5], [5, 5])  # Snake head and food in the same position
    assert not check_eat_food([5, 5], [6, 6])  # Snake head and food in different positions

# Add more test cases as needed

if __name__ == '__main__':
    pytest.main()
