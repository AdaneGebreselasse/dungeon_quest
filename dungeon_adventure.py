import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        """
        player_name = input("Please enter player name: ").strip()
        health = 10
        inventory = []
        player = {"name": player_name, "health": health, "inventory": inventory}
        return player
        

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.
        """
        treasures = {
            "gold coin": random.randint(3, 12),
            "ruby": random.randint(3, 12),
            "ancient scroll": random.randint(3, 12),
            "emerald": random.randint(3, 12),
            "silver ring": random.randint(3, 12),
        }
        return treasures

    #player = setup_player()
    #treasures = create_treasures()

    def display_options(room_number):
        """
        Displays available options for the player in the current room.
        """
        print(f"\nYou are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")

    
    def search_room(player, treasures):
        """
        Simulates searching the current room.
        """
        outcome = random.choice(["treasure", "trap"])

        if outcome == "treasure":
            item = random.choice(list(treasures.keys()))
            player["inventory"].append(item)
            print(f"You found a {item} worth {treasures[item]} points!")
        else:
            player["health"] -= 2
            print("A trap was triggered! You lost 2 health points.")
        
     
    def check_status(player):
        """
        Displays the player’s current health and inventory.
        """
        print(f"\nHealth: {player['health']}")
        if player["inventory"]:
            items = ", ".join(player["inventory"])
            print(f"Inventory: {items}")
        else:
            print("Inventory: You have no items yet.")

    def end_game(player, treasures):
        """
        Ends the game and displays a summary.
        """
        print("\n Game Over!")
        print(f"Final health: {player['health']}")

        if player["inventory"]:
            print("You collected:")
            total_value = 0
            for item in player["inventory"]:
                value = treasures.get(item, 0)
                total_value += value
                print(f" - {item} (value: {value})")
            print(f"Total treasure value: {total_value}")
            
        else:
            print("You collected no treasures.")

        print("Thanks for playing!")

    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.
        """
        for room_number in range(1, 6):
            if player["health"] < 1:
                print("\nYou have no health left. You collapse...")
                break

            in_room = True
            while in_room and player["health"] > 0:
                display_options(room_number)
                choice = input("Enter your choice (1-4): ").strip()

                if choice == "1":
                    search_room(player, treasures)
                elif choice == "2":
                    print("You move to the next room.")
                    in_room = False
                elif choice == "3":
                    check_status(player)
                elif choice == "4":
                    print("You chose to quit the game.")
                    # USE RETURN TO EXIT ENTIRELY
                    return end_game(player, treasures)
                    #in_room = False
                    # End the loop over rooms early
                    #room_number = 5  # force end after this
                    #break
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.") 

        end_game(player, treasures)

    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()