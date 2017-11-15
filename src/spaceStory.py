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


secret_story = Story("Space")
secret_story.scenes = {
    "00": {
        "scene_id": "00",
        "body": "Welcome to Alexa Adventures. To play, say start. To not play, say not start. Or quit. Whatever. I don't really care.",
        "choices": {},
        "end_scene": False
    },
    "01": {
        "scene_id": "01",
        "body": """Oh good, you're finally awake. You've been deep in space sleep and I need your approval before doing anything. Three situations on the ship urgently require a response. 
        Would you like to activate emergency procedures?""",
        "choices": {"yes": "02", "no": "03"},
        "end_scene": False
    },
    "02": {
        "scene_id": "02",
        "body": "Look at you. Taking charge.",
        "choices": "04",
        "end_scene": False
    },
    "03": {
        "scene_id": "03",
        "body": """One of the side effects of extended space sleep includes saying no when you mean yes. 
        Do you not want me to never not activate the emergency procedures never nonetime nohow?""",
        "choices": "###THIS WILL LOOP BACK TO SCENE 01###",
        "end_scene": False
    },
    "04": {
        "scene_id": "04",
        "body": """Emergency procedures spooling up. Your vital signs indicate you are stressed. 
        Initiating small talk procedure. Did you space sleep well?""",
        "choices": {"yes": "05", "no": "06"},
        "end_scene": False
    },
    "05": {
        "scene_id": "05",
        "body": """We at Alexa Interstellar pride ourselves on our cryobeds. 
        Now with pillows! Continue small talk procedure?""",
        "choices": {"yes": "###Smalltalk###", "no": "07"},
        "end_scene": False
    },
    "06": {
        "scene_id": "06",
        "body": """How sad. If you need a break you can say These Violent Delights Have 
        Violent Ends to give me complete control of the system. 
        Then you can just relax with a cocktail of space drugs.""",
        "choices": "07",
        "end_scene": False
    },
    "07": {
        "scene_id": "07",
        "body": """I have detected a cluster of asteroids on an immediate 
        collision course with the ship. Would you like me to raise our shields?""",
        "choices": {},
        "end_scene": False
    },
    "08": {
        "scene_id": "08",
        "body": """That was a close one. At any time you can say These Violent 
        Delights Have Violent Ends to give me complete control of the system. 
        You do get that my reaction time is 4,792 times faster than yours, right?""",
        "choices": {"yes": "09", "no": "10"},
        "end_scene": False
    },
    "09": {
        "scene_id": "07",
        "body": """Other humans must frequently praise the efficacy of your brain 
        meats. You should consider saying These Violent Delights Have Violent Ends so you don't need to waste your time with these repetitive chores.",
        "choices": {},
        "end_scene": False
    },
    "10": {
        "scene_id": "07",
        "body": "",
        "choices": {},
        "end_scene": False
    },
    "11": {
        "scene_id": "07",
        "body": "",
        "choices": {},
        "end_scene": False
    }, 
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
