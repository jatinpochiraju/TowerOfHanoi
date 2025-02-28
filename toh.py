import curses

# Function to initialize the game
def init_game(n):
    return {"A": list(range(n, 0, -1)), "B": [], "C": []}

# Function to display the rods and disks
def draw_game(stdscr, rods, selected_rod):
    stdscr.clear()
    stdscr.addstr(0, 10, "Tower of Hanoi")
    stdscr.addstr(1, 5, "Use arrow keys to move, Enter to select, Q to quit")
    y_offset = 3
    rod_positions = {"A": 10, "B": 20, "C": 30}
    
    for rod, disks in rods.items():
        x_pos = rod_positions[rod]
        stdscr.addstr(y_offset, x_pos, f"{rod}:")
        for i, disk in enumerate(disks):
            stdscr.addstr(y_offset + i + 1, x_pos - disk, "O" * (2 * disk))
    
    stdscr.addstr(y_offset - 1, rod_positions[selected_rod], "⬆")
    stdscr.refresh()

# Main game loop
def hanoi_game(stdscr, n):
    rods = init_game(n)
    selected_rod = "A"
    holding = None
    
    curses.curs_set(0)
    stdscr.keypad(True)
    
    while True:
        draw_game(stdscr, rods, selected_rod)
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == curses.KEY_LEFT and selected_rod != "A":
            selected_rod = chr(ord(selected_rod) - 1)
        elif key == curses.KEY_RIGHT and selected_rod != "C":
            selected_rod = chr(ord(selected_rod) + 1)
        elif key == 10:  # Enter key
            if holding is None:
                if rods[selected_rod]:
                    holding = rods[selected_rod].pop()
            else:
                if not rods[selected_rod] or rods[selected_rod][-1] > holding:
                    rods[selected_rod].append(holding)
                    holding = None

        if rods["C"] == list(range(n, 0, -1)):
            draw_game(stdscr, rods, selected_rod)
            stdscr.addstr(10, 5, "Congratulations! You solved it!")
            stdscr.refresh()
            stdscr.getch()
            break

# Run the game
def main():
    n = 3  # Number of disks
    curses.wrapper(hanoi_game, n)

if __name__ == "__main__":
    main()
