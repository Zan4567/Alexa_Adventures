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
        self.title = title
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
secret_story = Story('Test Story')
secret_story.add_scene(0, "MAIN MENU. To start a new game, say start. To quit, say quit.")
secret_story.add_scene(1, "This is the first scene. You are at a fork in an underground tunnel. Which way will you go? Left or right?")
secret_story.add_scene(2, "You went left. You find a ladder leading up into sunlight. Say left to go back or right to go up.")
secret_story.add_scene(3, "You went right. There are stairs leading down into darkness. Say left to go back or right to go down.")
secret_story.add_scene(4, "You climb out. This is the end. Congratulations!", True)
secret_story.add_scene(5, "You go down the stairs and get lost forever. The end.", True)
secret_story.add_path(1, 2)
secret_story.add_path(1, 3)
secret_story.add_path(2, 1)
secret_story.add_path(2, 4)
secret_story.add_path(3, 1)
secret_story.add_path(3, 5)


def lambda_handler(event, context):
    """Handle the lambda."""
    if event["session"]["new"]:
        current = 0
        response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': secret_story.scenes[current].body,
                }
            },
            'sessionAttributes': {
                'current_scene': 0
            }
        }
    elif event["session"]["attributes"]['current_scene'] == 0:
        if event["request"]["intent"]["name"] == "StartTent":
            current = 1
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': secret_story.scenes[current].body,
                    }
                },
                'sessionAttributes': {
                    'current_scene': 1
                }
            }
        elif event["request"]["intent"]["name"] == "QuitTent":
            # This is where someone will quit the game.
            pass
    elif event["session"]["attributes"]['current_scene']:
        current = event["session"]["attributes"]['current_scene']
        if event["request"]["intent"]["name"] == "LeftTent":
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': secret_story.scenes[current].choices[0].body,
                    }
                },
                'sessionAttributes': {
                    'current_scene': secret_story.scenes[current].choices[0].scene_id
                }
            }
            current = secret_story.scenes[current].choices[0].scene_id
        elif event["request"]["intent"]["name"] == "RightTent":
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': secret_story.scenes[current].choices[1].body,
                    }
                },
                'sessionAttributes': {
                    'current_scene': secret_story.scenes[current].choices[1].scene_id
                }
            }
            current = secret_story.scenes[current].choices[1].scene_id
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
