# Classic Snake Game in Python

import random
import curses
import time

def create_food(snake_body, sh, sw):
    """Create random food on the screen that is not on the snake."""
    food = None
    while food is None:
        nf = [
            random.randint(1, sh - 1),
            random.randint(1, sw - 1)
        ]
        food = nf if nf not in snake_body else None
    return food

def move_snake(snake_body, key):
    """Move the snake's head based on the key input."""
    new_head = [snake_body[0][0], snake_body[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    return new_head

def check_collision(snake_body, sh, sw):
    """Check if the snake collides with the wall or itself."""
    if (
        snake_body[0][0] in [0, sh] or
        snake_body[0][1] in [0, sw] or
        snake_body[0] in snake_body[1:]
    ):
        return True
    return False

def check_eat_food(snake_head, food):
    """Check if the snake's head collides with the food."""
    return snake_head == food

def initialize_screen():
    """Initialize the game screen."""
    stdscr = curses.initscr()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    sh, sw = stdscr.getmaxyx()
    return stdscr, sh, sw

def draw_game(stdscr, snake_body, food, score):
    """Draw the snake and food on the screen."""
    stdscr.clear()
    stdscr.addch(food[0], food[1], curses.ACS_PI)
    for segment in snake_body:
        stdscr.addch(segment[0], segment[1], curses.ACS_CKBOARD)

    # Display the score continuously at the top
    stdscr.addstr(0, 2, f"Score: {score}")
    stdscr.refresh()

def main(stdscr):
    """Main game loop."""
    stdscr, sh, sw = initialize_screen()

    # Snake initial position
    snake_x = sw // 4
    snake_y = sh // 2

    # Snake body
    snake_body = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    # Food position
    food = create_food(snake_body, sh, sw)

    # Initial direction
    key = curses.KEY_RIGHT

    score = 0

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        # Check if the player quit the game
        if snake_body[0] == [0, 0]:
            break

        # Move the snake
        new_head = move_snake(snake_body, key)
        snake_body.insert(0, new_head)

        # Check for collision with the wall or itself
        if check_collision(snake_body, sh, sw):
            break

        # Check if the snake eats the food
        if check_eat_food(snake_body[0], food):
            score += 1
            food = create_food(snake_body, sh, sw)

        else:
            snake_body.pop()

        # Draw the game
        draw_game(stdscr, snake_body, food, score)


    # Display the final score for a brief moment
    stdscr.addstr(sh // 2, sw // 2 - 5, f"Final Score: {score}")
    stdscr.refresh()

    # Sleep for a moment before exiting
    time.sleep(2)  # Adjust the duration as needed
    curses.endwin()


if __name__ == '__main__':
    curses.wrapper(main)
