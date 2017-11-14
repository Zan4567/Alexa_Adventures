# """Test our understanding of the lambda function."""
import random


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


test_story = Story('Test Story')
test_story.add_scene(0, "MAIN MENU. To start a new game, say start. To quit, say quit.")
test_story.add_scene(1, "This is the first scene. 1) Go left or 2) Go right.")
test_story.add_scene(2, "You went left. There is a ladder leading up into sunlight. 1) Go back or 2) Go up.")
test_story.add_scene(3, "You went right. There are stairs leading down into darkness. 1) Go back or 2) Go down.")
test_story.add_scene(4, "You climb out. This is the end. Congratulations! \n", True)
test_story.add_scene(5, "You go down the stairs and get lost forever. The end. \n", True)


def lambda_handler(event, context):
    """Handle the lambda."""
    if event["session"]["new"]:
        response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': test_story.scenes[0].body,
                }
            },
            'sessionAttributes': {
                'current_scene': 0
            }
        }

    elif event["session"]["attributes"]['current_scene'] == 0:
        if event["request"]["intent"]["name"] == "StartTent":
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': test_story.scenes[1].body,
                    }
                },
                'sessionAttributes': {
                    'current_scene': 1
                }
            }
        elif event["request"]["intent"]["name"] == "QuitTent":
            # This is where someone will quit the game.
            pass

    elif event["session"]["attributes"]['current_scene'] == 1:
        if event["request"]["intent"]["name"] == "LeftTent":
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': test_story.scenes[2].body,
                    }
                },
                'sessionAttributes': {
                    'current_scene': 2
                }
            }
        elif event["request"]["intent"]["name"] == "RightTent":
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': test_story.scenes[3].body,
                    }
                },
                'sessionAttributes': {
                    'current_scene': 3
                }
            }
    else:
        error = 'you made a boo boo'
        response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': error,
                    }
                },
            }

    return response
