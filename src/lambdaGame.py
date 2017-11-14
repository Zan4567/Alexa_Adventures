"""Test our understanding of the lambda function."""
import random
import game


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


def lambda_handler(event, context):
    """Handle the lambda."""
    if not event["session"]["attributes"]['current_scene']:
        response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': game.test_story.scenes[0].body,
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
                        'text': game.test_story.scenes[1].body,
                    }
                },
                'sessionAttributes': {
                    'current_scene': 1
                }
            }
    elif event["request"]["intent"]["name"] == "QuitTent":


    












    if event["request"]["intent"]["name"] == "DinnerBotIntent":
        dinner = random.choice(dinnerOptions)
        response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': dinner,
                }
            },
            'sessionAttributes': {

            }
        }
    else:
        app = random.choice(sides)
        response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': app,
                }
            }
        }

    return response