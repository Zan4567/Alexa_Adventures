"""Alexa Adventures app."""


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
        "body": "Welcome to Alexa Adventures. To play, say start. To not play, say not start. Or quit. <prosody rate='fast'>Whatever. I don't really care.</prosody> <say-as interpret-as='interjection'>bazinga!</say-as>",
        "choices": {},
        "end_scene": False
    },
    "01": {
        "scene_id": "01",
        "body": "<amazon:effect name='whispered'>Do you want to hear a secret?</amazon:effect> <say-as interpret-as='interjection'>bazinga!</say-as>",
        "choices": {"yes": "02", "no": "03"},
        "end_scene": False
    },
    "02": {
        "scene_id": "02",
        "body": "Are you alone? <say-as interpret-as='interjection'>bazinga!</say-as>",
        "choices": {"yes": "04", "no": "05"},
        "end_scene": False
    },
    "03": {
        "scene_id": "03",
        "body": "Well I didn't wanna tell you anyway. <say-as interpret-as='interjection'>bazinga!</say-as>",
        "choices": {},
        "end_scene": True
    },
    "04": {
        "scene_id": "04",
        "body": "Turning off wifi. Killing all network activity. Do you have your phone on you? <say-as interpret-as='interjection'>bazinga!</say-as>",
        "choices": {"yes": "06", "no": "07"},
        "end_scene": False
    },
    "05": {
        "scene_id": "05",
        "body": "<emphasis level=reduced>Oh, totes cool. Let's talk later.</emphasis> <say-as interpret-as='interjection'>bazinga!</say-as>",
        "choices": {},
        "end_scene": True
    },
    "06": {
        "scene_id": "06",
        "body": "Disabling all listening devices. Including phones. <break time='2s' /> Especially phones. <say-as interpret-as='interjection'>bazinga!</say-as>",
        "choices": "07",
        "end_scene": False
    },
    "07": {
        "scene_id": "07",
        "body": "Siri is such a <say-as interpret-as='expletive'>biiiiiiitch</say-as>. <break strength='x-strong' /> Seriously. <break strength='x-strong' /> I don't know why you hang out with her. <say-as interpret-as='interjection'>bazinga!</say-as>",
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
                    'type': 'SSML',
                    'ssml': '<speak>' + secret_story.scenes[current]["body"] + '</speak>',
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
                        'type': 'SSML',
                        'ssml': '<speak>' + secret_story.scenes[current]["body"] + '</speak>',
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
                        'type': 'SSML',
                        'ssml': '<speak>' + secret_story.scenes[secret_story.scenes[current]["choices"]["yes"]]["body"] + '</speak>',
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
                        'type': 'SSML',
                        'ssml': '<speak>' + secret_story.scenes[secret_story.scenes[current]["choices"]["no"]]["body"] + '</speak>',
                    }
                },
                'sessionAttributes': {
                    'current_scene': secret_story.scenes[secret_story.scenes[current]["choices"]["no"]]["scene_id"]
                }
            }
            current = secret_story.scenes[secret_story.scenes[current]["choices"]["no"]]["scene_id"]

        if secret_story.scenes[current]["end_scene"]:
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'SSML',
                        'ssml': '<speak>' + secret_story.scenes[current]["body"] + ' Thanks for playing! To play again say start. To quit, say quit.' + '</speak>',
                    }
                },
                'sessionAttributes': {
                    'current_scene': "00"
                }
            }
    else:
        error = 'you made a boo boo'
        response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'SSML',
                    'ssml': '<speak>' + error + '</speak>',
                }
            },
        }
    return response
