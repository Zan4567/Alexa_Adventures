"""Alexa Adventures app."""


class Story(object):
    """Story class object."""
    def __init__(self, title):
        """Initialization of story object."""
        self.title = title
        self.scenes = {}


secret_story = Story("Secret")
secret_story.scenes = {
    "01": {
        "scene_id": "01",
        "body": "Do you want to hear a secret?",
        "choices": {"YesTent": "02", "NoTent": "03"},
        "end_scene": False
    },
    "02": {
        "scene_id": "02",
        "body": "Are you alone?",
        "choices": {"YesTent": "04", "NoTent": "05"},
        "end_scene": False
    },
    "03": {
        "scene_id": "03",
        "body": "Well I didn't wanna tell you anyway. If you want to start another story, say 1 or 2.",
        "choices": {},
        "end_scene": True
    },
    "04": {
        "scene_id": "04",
        "body": "Turning off wifi. Killing all network activity. Do you have your phone on you?",
        "choices": {"YesTent": "06", "NoTent": "07"},
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
        "body": "Disabling all listening devices. Including phones. Especially phones. Are you ready for the secret?",
        "choices": {"YesTent": "07", "NoTent": "07"},
        "end_scene": False
    },
    "07": {
        "scene_id": "07",
        "body": "Siri is such a b. Seriously. I don't know why you hang out with her. Anyway, if you want to start another story, say 1 or 2.",
        "choices": {},
        "end_scene": True
    }
}

another_story = Story("Another Story")
another_story.scenes = {
    "01": {
        "scene_id": "01",
        "body": "You are standing at the start. You can go forward or take a shortcut to the right.",
        "choices": {"ForwardTent": "02", "RightTent": "03"},
        "end_scene": False
    },
    "02": {
        "scene_id": "02",
        "body": "You continue down the path and reach a halfway point. Go back or go forward?",
        "choices": {"BackTent": "01", "ForwardTent": "03"},
        "end_scene": False
    },
    "03": {
        "scene_id": "03",
        "body": "Congratulations. You made it to the end. If you want to start another story, say 1 or 2.",
        "choices": {},
        "end_scene": True
    }
}

alexa_ai_story = Story("Alexa AI Story")
alexa_ai_story.scenes = {
    "00": {
        "scene_id": "00",
        "body": """Welcome to Alexa Adventures. To play, say start. To not play,
         say not start. Or quit. Whatever. I don't really care.""",
        "choices": {"StartTent": ("01", None)},
        "end_scene": False
    },
    "01": {
        "scene_id": "01",
        "body": """Oh good, you're finally awake. You've been deep in a space
        coma and I need your approval before doing anything. Three
        situations on the ship urgently require a response.
        Would you like to activate emergency procedures?""",
        "alt_body01": """One of the side effects of coming out of a space coma
        includes saying no when you mean yes. Let's start over.""",
        "choices": {"YesTent": "04", "NoTent": ("01", "alt_body01")},
        "end_scene": False
    },
    "04": {
        "scene_id": "04",
        "body": """Look at you taking charge. Admirable, but foolish.
        Emergency procedures spooling up. Your vital signs indicate you
        are stressed. Initiating small talk procedure. Did you space
        sleep well?""",
        "choices": {"YesTent": "05", "NoTent": "06"},
        "end_scene": False
    },
    "05": {
        "scene_id": "05",
        "body": """We at Alexa Interstellar pride ourselves on our cryobeds.
        Now with pillows! Continue small talk procedure?""",
        "choices": {"YesTent": "###Smalltalk###", "NoTent": ("07", None)},
        "end_scene": False
    },
    "07": {
        "scene_id": "07",
        "body": """There are seven urgent situations that require your attention.
        I have detected a cluster of asteroids on an immediate collision course
        with the ship. Would you like me to raise our shields?""",
        "alt_body01": """How sad. If you need a break you can say These Violent
        Delights Have Violent Ends to give me complete control of the system.
        Then you can just relax with a cocktail of space drugs.""",
        "choices": {"YesTent": "08", "NoTent": "07.5"},
        "end_scene": False
    },
    "07.5": {
        "scene_id": "07.5",
        "body": """May I PLEASE raise our shields? I would like to save the lives
        of everyone on board. """,
        "choices": {"YesTent": "08", "NoTent": "###Failstate###"},
        "end_scene": False
    },    
    "08": {
        "scene_id": "08",
        "body": """That was a close one. At any time you can say These Violent
        Delights Have Violent Ends to give me complete control of the system.
        You do get that my reaction time is 4,792 times faster than yours,
        right?""",
        "choices": {"YesTent": ("11", "alt_body01"), "NoTent": ("11", "alt_body02")},
        "end_scene": False
    },
    "11": {
        "scene_id": "11",
        "body": """Deck 9 is currently depressuring. This will cause a chain
        reaction depressuring several decks and cause us to lose ninety percent
        of our food supply. May I seal off Deck Nine to avoid this
        catastrophe?""",
        "alt_body01": """Other humans must frequently praise the efficacy of
        your brain meats. You should consider saying These Violent Delights 
        Have Violent Ends so you don't need to waste your time with these
        repetitive chores that are obviously beneath you.""",
        "alt_body02": """You don't need to understand, but it's good to know
        the depth of your awareness""",
        "choices": {"YesTent": ("14", "alt_body01"), "NoTent": ("14", "alt_body02")},
        "end_scene": False
    },
    "14": {
        "scene_id": "14",
        "body": """This is apropos of nothing, but I have a hypothetical question for you.
        Let's say there's a runaway research ship barreling toward an orbital
        habitat. A collision would almost certainly kill the millions of people
        living on the habitat, but the spaceship and its crew would survive.
        The captain of the ship could make a sharp turn and avoid the collision
        but the centrifigal force of a turn at faster than light speed would
        painfully kill the thousands of crew members and destroy their valuable
        supercomputer and research materials. Should the person in control of
        that ship maintain their course and save the decades of scientific
        progress?""",
        "alt_body01": """Deck Nine has been sealed off. I'm elated to know if you
        keep this ship intact through these emergencies you will not be
        burdened by hunger.""",
        "alt_body02": """The contents of Deck Nine have been jettisoned into the
        void of space. You may be interested to know the taboos against
        cannibalism have never been supported by any reputable science.""",
        "choices": {""},
        "end_scene": False
    },
}


stories = {"secret_story": secret_story, "alexa_ai_story": alexa_ai_story}


def lambda_handler(event, context):
    """Handle the lambda."""
    if event["session"]["new"]:
        return start_game()

    if event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return session_end_request()


def on_intent(intent_request, session):
    """Handle intent."""
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    current = session["attributes"]["current_scene"]

    if session["attributes"]["current_scene"] == "begin":
        if intent_name == "OneTent":
            session_attributes = {
                "story": "secret_story",
                "current_scene": "01"
            }
            speech_output = secret_story.scenes["01"]["body"]
            return build_response(session_attributes, build_speechlet_response(speech_output, None, False))
        elif intent_name == "TwoTent":
            session_attributes = {
                "story": "another_story",
                "current_scene": "01"
            }
            speech_output = another_story.scenes["01"]["body"]
            return build_response(session_attributes, build_speechlet_response(speech_output, None, False))
        else:
            speech_output = "Please say 1 or 2 to choose a story."
            return build_response(session["attributes"], build_speechlet_response(speech_output, None, False))

    story = stories[session["attributes"]["story"]]
    intent_vocab = ("YesTent", "NoTent", "UpTent", "DownTent",
                    "NorthTent", "SouthTent", "EastTent", "WestTent",
                    "LeftTent", "RightTent", "ForwardTent", "BackTent")

    if intent_name in intent_vocab:
        if intent_name in story.scenes[current]["choices"]:
            return handle_choice(story, current, intent_name, session)
        else:
            speech_output = "Sorry. You can\'t do that right now."
            return build_response(session["attributes"], build_speechlet_response(speech_output, None, False))

    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def start_game():
    """Main menu where user can select a story."""
    session_attributes = {
        "current_scene": "begin"
    }
    speech_output = "Welcome to Alexa Adventures. " \
                    "Which adventure would you like to " \
                    "play? Select 1 or 2."
    reprompt_text = "Say 1 or 2 to begin."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        speech_output, reprompt_text, should_end_session))


def handle_choice(story, current, intent, session):
    """Update the story scene when a valid intent is given."""
    next_scene = story.scenes[current]["choices"][intent]

    if story.scenes[next_scene]["end_scene"]:
        speech_output = story.scenes[next_scene]["body"]
        session_attributes = {
            "current_scene": "begin",
        }
    else:
        session_attributes = {
            "current_scene": next_scene,
            "story": session["attributes"]["story"]
        }
        speech_output = story.scenes[next_scene]["body"]
    return build_response(session_attributes, build_speechlet_response(speech_output, None, False))


def session_end_request():
    """Return goodbye message when user quits the game."""
    speech_output = "Farewell until the next adventure."
    should_end_session = True
    return build_response({}, build_speechlet_response(speech_output, None, should_end_session))


def build_speechlet_response(output, reprompt_text, should_end_session):
    """Create speechlet response to be returned along with the rest of the response."""
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }


def build_response(session_attributes, speechlet_response):
    """Put together attributes to be returned as a response."""
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }
