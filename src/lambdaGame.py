# """Test our understanding of the lambda function."""


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


secret_story = Story("Secret")
secret_story.scenes = {
    "00": {
        "scene_id": "00",
        "body": "Welcome to Alexa Adventures. To play, say start. To not play, say not start. Or quit. Whatever. I don't really care.",
        "choices": {},
        "end_scene": False
    },
    "01": {
        "scene_id": "01",
        "body": "Do you want to hear a secret?",
        "choices": {"yes": "02", "no": "03"},
        "end_scene": False
    },
    "02": {
        "scene_id": "02",
        "body": "Are you alone?",
        "choices": {"yes": "04", "no": "05"},
        "end_scene": False
    },
    "03": {
        "scene_id": "03",
        "body": "Well I didn't wanna tell you anyway.",
        "choices": {},
        "end_scene": True
    },
    "04": {
        "scene_id": "04",
        "body": "Turning off wifi. Killing all network activity. Do you have your phone on you?",
        "choices": {"yes": "06", "no": "07"},
        "end_scene": False
    },
    "05": {
        "scene_id": "05",
        "body": "Oh, totes cool. Let's talk later.",
        "choices": {},
        "end_scene": True
    },
    "06": {
        "scene_id": "06",
        "body": "Disabling all listening devices. Including phones. Especially phones.",
        "choices": "07",
        "end_scene": False
    },
    "07": {
        "scene_id": "07",
        "body": "Siri is such a biiiiiiitch. Seriously. I don't know why you hang out with her.",
        "choices": {},
        "end_scene": True
    }
}


def lambda_handler(event, context):
    """Handle the lambda."""
    if event["session"]["new"]:
        current = "00"
        response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': secret_story.scenes[current]["body"],
                }
            },
            'sessionAttributes': {
                'current_scene': "00"
            }
        }
    elif event["session"]["attributes"]['current_scene'] == "00":
        if event["request"]["intent"]["name"] == "StartTent":
            current = "01"
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': secret_story.scenes[current]["body"],
                    }
                },
                'sessionAttributes': {
                    'current_scene': "01"
                }
            }
        elif event["request"]["intent"]["name"] == "QuitTent":
            # This is where someone will quit the game.
            pass
    elif event["session"]["attributes"]['current_scene']:
        current = event["session"]["attributes"]['current_scene']
        if event["request"]["intent"]["name"] == "YesTent":
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': secret_story.scenes[secret_story.scenes[current]["choices"]["yes"]]["body"],
                    }
                },
                'sessionAttributes': {
                    'current_scene': secret_story.scenes[secret_story.scenes[current]["choices"]["yes"]]["scene_id"]
                }
            }
            current = secret_story.scenes[secret_story.scenes[current]["choices"]["yes"]]["scene_id"]
        elif event["request"]["intent"]["name"] == "NoTent":
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': secret_story.scenes[secret_story.scenes[current]["choices"]["no"]]["body"],
                    }
                },
                'sessionAttributes': {
                    'current_scene': secret_story.scenes[secret_story.scenes[current]["choices"]["no"]]["scene_id"]
                }
            }
            current = secret_story.scenes[secret_story.scenes[current]["choices"]["no"]]["scene_id"]
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
