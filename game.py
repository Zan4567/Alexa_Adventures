"""Text adventure tutorial."""
import random
import time


class Scene(object):
    """Scene class object."""

    def __init__(self, scene_id, body):
        """Initialization of scene object."""
        self.scene_id = scene_id
        self.body = body
        self.choices = []


class Story(object):
    """Story class object."""

    def __init__(self, title):
        """Initialization of story object."""
        self.title = 'Title'
        self.scenes = {}

    def add_scene(self, scene_id, body):
        """Create a scene and add it to scenes list."""
        new_scene = Scene(scene_id, body)
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
    print('Choose an option.')
    user_response = input('1 to play. Q to quit. \n')
    if user_response == '1':
        print('Starting game.')
        choose_path(story, story.scenes[1])
    elif user_response.lower() == 'q':
        print('Selected quit.')
    else:
        print('Invalid response. \n')
    main_prompt()


def choose_path(story, scene):
    """User prompt for game."""
    print(scene.body)
    path = ""
    while path != "1" and path != "2":
        path = input("Choose 1 or 2. Q to quit. \n")
        if path == "1":
            choose_path(story, story.scenes[scene.choices[0].scene_id])
        elif path == "2":
            choose_path(story, story.scenes[scene.choices[1].scene_id])
        elif path.lower() == 'q':
            print('Selected quit. \n')
        else:
            print('Invalid response. \n')


def info():
    """User asks for help or information."""
    pass


if __name__ == '__main__':
    test_story = Story('Test Story')
    test_story.add_scene(1, "This is the first scene. 1) Go right or 2) Go left.")
    test_story.add_scene(2, "You went right. 1) Go back or 2) Go left.")
    test_story.add_scene(3, "You went left. 1) Go back or 2) Go right.")
    test_story.add_path(1, 2)
    test_story.add_path(1, 3)
    test_story.add_path(2, 1)
    test_story.add_path(2, 3)
    test_story.add_path(3, 1)
    test_story.add_path(3, 2)
    display_intro(test_story)
