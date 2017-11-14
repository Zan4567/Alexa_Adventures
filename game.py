"""Text adventure tutorial."""
import random
import time
import sys


class Scene(object):
    """Scene class object."""

    def __init__(self, scene_id, body, end_scene=False):
        """Initialization of scene object."""
        self.scene_id = scene_id
        self.body = body
        self.choices = []
        self.end_scene = end_scene

class Story(object):
    """Story class object."""

    def __init__(self, title):
        """Initialization of story object."""
        self.title = 'Title'
        self.scenes = {}

    def add_scene(self, scene_id, body, end_scene=False):
        """Create a scene and add it to scenes list."""
        new_scene = Scene(scene_id, body, end_scene)
        if scene_id in self.scenes:
            raise ValueError('Duplicate scene.')
        self.scenes[scene_id] = new_scene

    def add_path(self, scene1, scene2):
        """Create a path from one scene to another."""
        # if scene1.id not in self.scenes:
        #     self.add_scene(scene1.id, scene1)
        # if scene2.id not in self.scenes:
        #     self.add_scene(scene2.id, scene2)
        # if scene2 in self.scenes[scene1]:
        #     print('Path already exists.')
        self.scenes[scene1].choices.append(self.scenes[scene2])


def display_intro(story):
    """Game introduction text."""
    print("Game introduction.")
    time.sleep(1)
    print("Welcome to the game. Lorem ipsum and stuff.")
    time.sleep(2)
    print("This is where a brief summary of the game goes followed by a prompt.")
    print("Eventually there will be multiple adventures to choose from. For now the options")
    print("are start the game or quit.")
    time.sleep(2)
    main_prompt(story)


def main_prompt(story):
    """Ask for user input."""
    print('\n Main menu \n ---------- \n Choose an option.')
    user_response = input('1 to play. Q to quit. Type info or help for game instructions. \n')
    if user_response == '1':
        print('Starting game.')
        choose_path(story, story.scenes[1])
    elif user_response.lower() in ('q', 'quit', 'exit'):
        print('Are you sure you want to quit?')
        quit = input('Y or N: ')
        if quit.lower() in ('y', 'yes'):
            sys.exit()
    elif user_response.lower() in ('i', 'info', 'information', 'help', 'h', 'instructions'):
        info()
    else:
        print('Invalid response. \n')
    main_prompt(story)


def choose_path(story, scene):
    """User prompt for game."""
    print(scene.body)
    if scene.end_scene:
        time.sleep(1)
        print("Thanks for playing!")
        time.sleep(3)
        main_prompt(story)
    path = ""
    while path != "1" and path != "2":
        path = input("Make a choice: ")
        if path == "1":
            choose_path(story, story.scenes[scene.choices[0].scene_id])
        elif path == "2":
            try:
                choose_path(story, story.scenes[scene.choices[1].scene_id])
            except:
                print('Nope.')
        elif path.lower() in ("info", "information", "help", "h", "instructions"):
            info()
            print(scene.body)
        elif path.lower() in ('q', 'quit', 'exit'):
            print('Are you sure you want to quit to the menu?\n')
            quit = input('Y or N: ')
            if quit.lower() in ('y', 'yes'):
                main_prompt(story)
            else:
                print(scene.body)
        else:
            print('Invalid response. \n')


def info():
    """User asks for help or information."""
    print("\n Game instructions \n")
    print("-----------------------")
    print("This is where game instructions go.")
    print("Alexa will read a description of the current scene.")
    print("Then there will be a prompt asking the player to choose from set options.")
    print("The next scene will be called based on the player's response.")
    print("At any point the player may quit back to the main menu. \n")


if __name__ == '__main__':
    test_story = Story('Test Story')
    test_story.add_scene(0, "Blah blah blah, bitch, this is the beginning MAIN MENU")
    test_story.add_scene(1, "This is the first scene. 1) Go left or 2) Go right.")
    test_story.add_scene(2, "You went left. There is a ladder leading up into sunlight. 1) Go back or 2) Go up.")
    test_story.add_scene(3, "You went right. There are stairs leading down into darkness. 1) Go back or 2) Go down.")
    test_story.add_scene(4, "You climb out. This is the end. Congratulations! \n", True)
    test_story.add_scene(5, "You go down the stairs and get lost forever. The end. \n", True)
    test_story.add_path(1, 2)
    test_story.add_path(1, 3)
    test_story.add_path(2, 1)
    test_story.add_path(2, 4)
    test_story.add_path(3, 1)
    test_story.add_path(3, 5)
    test_story.add_path(4, 4)
    test_story.add_path(5, 5)
    display_intro(test_story)
