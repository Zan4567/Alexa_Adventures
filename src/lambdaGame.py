"""Alexa Adventures app."""


class Story(object):
    """Story class object."""

    def __init__(self, title):
        """Initialization of story object."""
        self.title = title
        self.scenes = {}


secret_story = Story("Alexa\'s Secret")
secret_story.scenes = {
    "01": {
        "scene_id": "01",
        "body": "Do you want to hear a secret?",
        "choices": {"YesTent": ("02", None), "NoTent": ("03", None)},
        "end_scene": False
    },
    "02": {
        "scene_id": "02",
        "body": "Are you alone?",
        "choices": {"YesTent": ("04", None), "NoTent": ("05", None)},
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
        "choices": {"YesTent": ("06", None), "NoTent": ("07", None)},
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
        "choices": {"YesTent": ("07", "alt_body1"), "NoTent": ("07", "alt_body2")},
        "end_scene": False
    },
    "07": {
        "scene_id": "07",
        "body": "Siri is such a b. Seriously. I don't know why you hang out with her. Anyway, ",
        "alt_body1": "Okay. Here is the secret. ",
        "alt_body2": "Whatever. I\'m telling you anyway. ",
        "choices": {},
        "end_scene": True
    }
}

another_story = Story("Another Story")
another_story.scenes = {
    "01": {
        "scene_id": "01",
        "body": "You are standing at the start. You can go forward or take a shortcut to the right.",
        "choices": {"ForwardTent": ("02", None), "RightTent": ("03", "alt_body2")},
        "end_scene": False
    },
    "02": {
        "scene_id": "02",
        "body": "You continue down the path and reach a halfway point. Go back or go forward?",
        "choices": {"BackTent": ("01", None), "ForwardTent": ("03", "alt_body1")},
        "end_scene": False
    },
    "03": {
        "scene_id": "03",
        "body": "You made it to the end. Congratulations.",
        "alt_body1": "You took your sweet time getting there, but ",
        "alt_body2": "That was fast. ",
        "choices": {},
        "end_scene": True
    }
}


stories = {"secret_story": secret_story, "another_story": another_story}


def lambda_handler(event, context):
    """Handle the lambda."""
    if event["session"]["new"]:
        return start_game()

    if event["request"]["type"] == "IntentRequest":
        return handle_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return session_end_request()


def handle_intent(intent_request, session):
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
            speech_output = "Please say 1 for {} or 2 for {} to begin the adventure.".format(secret_story.title, another_story.title)
            return build_response(session["attributes"], build_speechlet_response(speech_output, None, False))                

    story = stories[session["attributes"]["story"]]
    intent_vocab = ("YesTent", "NoTent", "UpTent", "DownTent",
                    "NorthTent", "SouthTent", "EastTent", "WestTent",
                    "LeftTent", "RightTent", "ForwardTent", "BackTent",
                    "WhatTent")

    if intent_name in intent_vocab:
        if intent_name in story.scenes[current]["choices"]:
            return handle_choice(story, current, intent_name, session)
        else:
            if intent_name == "WhatTent":
                speech_output = "Sorry. I didn\'t understand that. Repeating prompt. " + story.scenes[current]["body"]
            else:
                speech_output = "Sorry. You can\'t do that right now. Repeating prompt. " + story.scenes[current]["body"]        
            return build_response(session["attributes"], build_speechlet_response(speech_output, None, False))

    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return session_end_request()

    else:
        raise ValueError("Invalid intent")


def start_game():
    """Main menu where user can select a story."""
    session_attributes = {
        "current_scene": "begin"
    }
    speech_output = "Welcome to Alexa Adventures. " \
                    "Which adventure would you like to " \
                    "play? For {} say 1. For {} say 2.".format(secret_story.title, another_story.title)
    reprompt_text = "Please say 1 for {} or 2 for {} to begin the adventure.".format(secret_story.title, another_story.title)
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        speech_output, reprompt_text, should_end_session))


def handle_choice(story, current, intent, session):
    """Update the story scene when a valid intent is given."""
    next_scene = story.scenes[current]["choices"][intent][0]
    alt_text = story.scenes[current]["choices"][intent][1]

    if story.scenes[next_scene]["end_scene"]:
        if alt_text:
            speech_output = story.scenes[next_scene][alt_text] + story.scenes[next_scene]["body"] + " To start a new story, say 1 or 2."
        else:
            speech_output = story.scenes[next_scene]["body"] + " To start a new story, say 1 or 2."

        session_attributes = {
            "current_scene": "begin",
        }
    else:
        session_attributes = {
            "current_scene": next_scene,
            "story": session["attributes"]["story"]
        }
        if alt_text:
            speech_output = story.scenes[next_scene][alt_text] + story.scenes[next_scene]["body"]
        else:
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
