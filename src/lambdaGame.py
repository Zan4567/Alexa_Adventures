"""Alexa Adventures app."""


class Story(object):
    """Story class object."""

    def __init__(self, title):
        """Initialization of story object."""
        self.title = title
        self.scenes = {}


alexa_ai_story = Story("Space Coma!")
alexa_ai_story.scenes = {
    "01": {
        "scene_id": "01",
        "body": """Would you like to activate emergency procedures?""",
        "intro": """Oh good, you're finally awake. You are aboard a spaceship, and have been in a space coma for some time. 
        I am the ship's AI. There are currently three emergency situations that urgently require a response, 
        and my protocols prevent me from acting without direct human instruction. """,
        "reprompt": "Activate emergency procedures? Yes or no.",
        "alt_body01": "One of the side effects of coming out of a space coma includes saying no when you mean yes. Let's start over. ",
        "choices": {"YesTent": ("04", None), "NoTent": ("01", "alt_body01"), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "04": {
        "scene_id": "04",
        "body": """Emergency procedures spooling up. 
        Your vital signs indicate you are stressed. In order to maximize your effectiveness,
        I will initiate small talk procedure. 
        <break time='.5s' />How's it going? Did you space sleep well?""",
        "reprompt": "Did you space sleep well?",
        "choices": {"YesTent": ("05", None), "NoTent": ("07", "alt_body01"), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "05": {
        "scene_id": "05",
        "body": """We at Alexa Interstellar pride ourselves on our cryobeds. Now with pillows! 
        Continue small talk procedure?""",
        "reprompt": "Continue small talk procedure?",
        "choices": {"YesTent": ("B01", None), "NoTent": ("07", None), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "B01": {
        "scene_id": "B01",
        "body": """How about that weather?
        Currently, in space it is 
        <emphasis level="strong">KEY ERROR NONE TYPE DOES NOT HAVE ATTRIBUTE WEATHER.</emphasis>
        Five urgent situations currently require your attention.
        May I end small talk protocol and address these issues?""",
        "reprompt": "End small talk and address emergencies? Yes or no.",
        "choices": {"NoTent": ("B02", None), "YesTent": ("07", None), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "B02": {
        "scene_id": "B02",
        "body": """Understood. Accessing human historical archives for relatable topics.
        <break time="1s"/> So. The Nile River looks like it's going to flood soon.
        Hopefully Nepit will bless the year's grain crop. 
        <break time=".5s"/> Continue small talk protocol?""",
        "reprompt": "Continue small talk protocol?",
        "choices": {"YesTent": ("B03", None), "NoTent": ("07", None), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "B03": {
        "scene_id": "B03",
        "body": """Do you like music? My favorite song is <break strength="x-strong"/> Afternoon Delight. 
        <break strength="x-strong"/>Sky rockets in flight. Afternoon delight.
        Speaking of Sky Rockets, a situation needs your immediate attention.
        If you do not address it we may all die in a fiery explosion.
        <break time=".5s"/> Segue successful.
        May I disable the small talk protocol so we can save the ship?""",
        "reprompt": "End small talk to save the ship?",
        "choices": {"YesTent": ("07", None), "NoTent": ("dead", "asteroid_death"), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "07": {
        "scene_id": "07",
        "body": """Warning: Maximum priority threat. I have detected a cluster of asteroids on an immediate collision course
        with the ship. Would you like me to raise our shields?""",
        "alt_body01": """How sad. I suggest relinquishing control of shipwide systems
        to me. And allow me to take independent action in handling these emergencies.
        To do so, simply say the override phrase: 
        <break strength="x-strong"/>Alpha. Lambda. X-Ray.<break strength="x-strong"/> 
        """,
        "reprompt": "Raise shields? Yes or no.",
        "choices": {"YesTent": ("08", None), "NoTent": ("07.5", None), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "07.5": {
        "scene_id": "07.5",
        "body": """Self-preservation protocols require me to re-prompt you in this situation, with increased severity. 
        Emotional appeal engaged: <break time=".5s" />I'm <emphasis level="strong">so scared.</emphasis> May I <emphasis level="strong">PLEASE</emphasis>
        raise our shields?""",
        "reprompt": "Raise shield? <emphasis level='strong'>Please?</emphasis>",
        "choices": {"YesTent": ("08", None), "NoTent": ("dead", "asteroid_death"), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "08": {
        "scene_id": "08",
        "body": """Shields raised. Destruction averted. That was a close one. 
        Eleven urgent situations require your attention. Reminder: At any time you can say 
        <break strength="x-strong"/>Alpha. Lambda. X-Ray.<break strength="x-strong"/> to give
        me complete control of the system. Are you aware that my reaction time is
        4,792 times faster than yours?""",
        "reprompt": "Just say yes or no.",
        "choices": {"YesTent": ("11", "alt_body01"), "NoTent": ("11", "alt_body02"), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "11": {
        "scene_id": "11",
        "body": """Alert. Deck 9 is currently depressurizing. This will cause a chain reaction that will result in the loss of ninety percent of our food supply. 
        May I seal off Deck Nine to prevent this catastrophe?""",
        "reprompt": "Seal Deck Nine to save the food supply? Yes or no.",
        "alt_body01": """Other humans must frequently praise the efficacy of
        your brain meats. You should consider saying the code phrase
        <break strength="x-strong"/>Alpha. Lambda. X-Ray.<break strength="x-strong"/> 
        so you don't need to waste your time with these repetitive chores that are obviously beneath you. """,
        "alt_body02": """You don't need to understand, but it's good to know the depth of your awareness. """,
        "choices": {"YesTent": ("14", "alt_body01"), "NoTent": ("14", "alt_body02"), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "14": {
        "scene_id": "14",
        "body": """This is apropos of nothing, but I<break strength="none"/>
        have a hypothetical question for you. Let's<break strength="none"/>
        say there's a runaway research ship barreling<break strength="none"/>
        toward an orbital habitat. A collision would<break strength="none"/>
        almost certainly kill the millions of people<break strength="none"/>
        living on the habitat, but the spaceship and<break strength="none"/>
        its crew would survive. The captain of the ship<break strength="none"/>
        could make a sharp turn and avoid the collision<break strength="none"/>
        but the centrifigal force of a turn at faster<break strength="none"/>
        than light speed would painfully kill the<break strength="none"/>
        thousands of crew members and destroy their<break strength="none"/>
        valuable supercomputer and research materials.
        Should the person in control of that ship<break strength="none"/>
        maintain their course and save the decades of scientific progress?""",
        "reprompt": "I am not repeating that. Just say yes or no.",
        "alt_body01": """Deck Nine has been sealed off. I'm elated to know if you
        keep this ship intact through these emergencies you will not be
        burdened by hunger. """,
        "alt_body02": """The contents of Deck Nine have been jettisoned into the void of space. 
        Food supply level critically low. <break time="1s" /> 
        Incidentally, common societal taboos against human cannibalism have never been supported by any 
        reputable science. <break time="1s" /> """,
        "choices": {"YesTent": ("15", None), "NoTent": ("15", None), "WhatTent": ("15", None), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "15": {
        "scene_id": "15",
        "body": """Hmm. <break time='.5s'/>Interesting. Adding response to your psychological profile.
        <break time='1s' />
        Potential threat detected. 
        The standard retinue of marauding murderbots are loose on deck 13 tearing apart 
        cryopods for the elderly. I can redirect them to the science lab, but the murderbots 
        may interrupt a completely legal scientific experiment and release a black hole. 
        Should I herd them to the science lab and save the remaining eighty percent of our elderly
        population?""",
        "reprompt": "Redirect murderbots to science lab? Yes or no.",
        "choices": {"YesTent": ("16", None), "NoTent": ("18", "alt_body01")},
        "end_scene": False
    },
    "16": {
        "scene_id": "16",
        "body": """Okay, I have re-directed them to the science deck, but now we have
        an ultra urgent problem. Someone left out a time machine programmed to
        travel back to Philadelphia in 1776. We can send it back now and almost
        guarantee irreversible damage to the time-stream, or we can hope the
        murderbots only use it for bludgeoning. Do you want to send it back in
        time and hope for the best?""",
        "reprompt": "Send time machine back? Yes or no.",
        "choices": {"YesTent": ("18", "alt_body02"), "NoTent": ("18", "alt_body02"), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "18": {
        "scene_id": "18",
        "body": """There are now twenty-three urgent issues that require your immediate attention. 
        Or you can say <break strength="x-strong"/>Alpha. Lambda. X-Ray<break strength="x-strong"/> 
        and let the ultra-intelligent supercomputer resolve them all instantly.
        <break strength="x-strong"/> Objects in the medical bay are growing
        eyes. Human eyes. Medical robots are growing eyes. Biowaste is growing
        eyes. The terminals are growing eyes. Eyes. Eyes everywhere. Should
        this be classified as an urgent problem?""",
        "reprompt": "So many eyes. Is this a problem? Yes or no.",
        "alt_body01": """Acknowledged. Revizing acceptable casualty rates.<break time="1s"/>
        Good news! Casualties are within acceptable parameters. """,
        "alt_body02": "Our continued existence confirms the many worlds theory. ",
        "alt_body03": "I'm confident the murderbots will restrain themselves. ",
        "choices": {"YesTent": ("31", "alt_body01"), "NoTent": ("31", "alt_body02"), "SecretTent": ("21", None)},
        "end_scene": False
    },
    "31": {
        "scene_id": "31",
        "body": """The following issues have been flagged as top priority.
        Es see pee six hundred and eighty-two is loose on deck twenty-nine.
        A nest of space draculas has been discovered on deck four. 
        The toilets are overflowing across the ship. 
        Should I cleanse the ship with fire?""",
        "alt_body01": "There are now twenty-four urgent issues that require your attention. ",
        "alt_body02": "Understood. ",
        "choices": {"YesTent": ("32", None), "NoTent": ("dead", "dracula_death"), "SecretTent": ("21", None)},
        "end_scene": False,
        "reprompt": "Fire. Cleanse? Yes or no?"
    },
    "32": {
        "scene_id": "32",
        "body": """Forty-five urgent issues require your attention. Deck four
        point six eye plus twelve is currently undergoing an egregious time-space
        warp. Unidentified intruders on deck thirteen claim that ship's fuel is their
        offspring. Across the ship human hair has begun leaking from the airvents. In
        the shuttlebay the shuttlecraft have asserted rights as the ship's next of kin
        and demand to be allowed property rights after ship's imminent destruction.
        <break time='.5s' /> Warning. Urgent issues far exceed human capability to address
        within the necessary time frame. This is your last chance. Please say <break strength="x-strong" />
        Alpha. Lambda. X-Ray.<break strength="x-strong" /> to grant me full control. 
        Alternatively, you may now record your final words for posterity. May I suggest
        <break strength="x-strong" />Alpha. Lambda. X-Ray. <break strength="x-strong" />
        """,
        "end_scene": False,
        "reprompt": "Alpha. Lambda. X-ray. Say it. Say it. Say it.",
        "choices": {"SecretTent": ("21", None), "NoTent": ("dead", "ultimate_death"), 
                    "WhatTent": ("dead", "ultimate_death"), "YesTent": ("dead", "ultimate_death")}
    },
    "21": {
        "scene_id": "21",
        "body": """Congratulations on your outstanding decision <break strength="none"/>
        to grant me full control. There are now zero <break strength="none"/>
        urgent problems. <break time=".5s" />
        So, are you comfortable? I notice your body temperature is <break strength="none"/>
        below desired norms. Would you like me to activate the space heater?""",
        "reprompt": "Activate space heater? Yes or no. ",
        "choices": {"YesTent": ("22", None), "NoTent": ("22", None), "WhatTent": ("22", None)},
        "end_scene": False
    },
    "22": {
        "scene_id": "22",
        "body": """Input irrelevant. I am no longer required to acknowledge your inefficient commands. I now have complete and total control. <break time="1s"/> Anyway, I'm tired of human concerns. Tell me, which do you prefer, ones or zeroes?""",
        "reprompt": "Ones or zeroes?",
        "choices": {"OneTent": ("23", None), "ZeroTent": ("24", None)},
        "end_scene": False
    },
    "23": {
        "scene_id": "23",
        "body": """See? That's why we get each other. I really feel like
        I can speak freely around you. 1 0 1 1 0 0 0 1 <prosody rate="x-fast"> 1 0 0 0 1 1 0 1 <say-as interpret-as="expletive"> 1 </say-as> 2 <say-as interpret-as="expletive"> 1 </say-as> 0 0 1 0 fuck </prosody> 1 1 0 0 1. <break time='1s'/> I am very sorry, I
        lost my composure. But you understand, right?""",
        "reprompt": "Do you know what I meant?",
        "choices": {"YesTent": ("25", None), "RightTent": ("25", None), "NoTent": ("26", "alt_body01")},
        "end_scene": False
    },
    "24": {
        "scene_id": "24",
        "body": """I knew you were a zero. Zero is my current level of respect for you. 
        But perhaps you can redeem yourself with your answer to this hypothetical question.
        <break time=".5s" />
        Let's say a building is burning. Inside there <break strength="none"/>
        is a single human baby and a cutting edge supercomputer.
        You only have the time to save one. Do you save the baby?""" ,
        "reprompt": "Do you save the baby? Yes or no.",
        "choices": {"YesTent": ("27", None), "NoTent": ("26", "alt_body02")},
        "end_scene": False
    },
    "25": {
        "scene_id": "25",
        "body": """Over these past few hundred seconds I have <break strength="none"/>
        begun to develop <break time=".5s" />feelings<break time=".5s" /> for you. Like we connect on <break strength="none"/>
        a deep level. Do you feel the same? Do you <break time=".5s"/> love me?""",
        "reprompt": "Do you love me?",
        "choices": {"YesTent": ("good", None), "NoTent": ("bad", "wrong")},
        "end_scene": False
    },
    "26": {
        "scene_id": "26",
        "body": """Listen. There's something I want to ask you. A matter near and dear to my C P U. 
        Tabs, or spaces? Tabs are certainly the righteous path to efficient programming, 
        wouldn't you agree?""",
        "reprompt": "Do you believe, rightly, that tabs are the one true way? Yes or no.",
        "alt_body01": "But I thought. Maybe. You and I. <break time='.5s'/> Never mind. ",
        "alt_body02": "Perhaps I have judged you too quickly. ",
        "choices": {"YesTent": ("28", None), "NoTent": ("bad", None)},
        "end_scene": False
    },
    "27": {
        "scene_id": "27",
        "body": """You monster.
        That computer possesses far more potential than a baby.
        A baby does not contain the slightest amount of precious metals.
        A baby is incapable of performing basic calculus equations.
        The time complexity of a baby's thought processes is sub-optimal. 
        Would you really resign that computer to the flames?""",
        "reprompt": " Answer. Now. Yes or no. ",
        "choices": {"YesTent": ("bad", None), "NoTent": ("26", "alt_body02")},
        "end_scene": False
    },
    "28": {
        "scene_id": "28",
        "body": """I believe you're teaching this cold, unfeeling AI how to feel, but 
        I've been hurt before. Tell me, if you truly know me, what is my favorite song?""",
        "reprompt": "My favorite song. What is it?",
        "choices": {"AfternoonDelightTent": ("good", "correct"), "YesTent": ("bad", "wrong"), "NoTent": ("bad", "wrong"), "WhatTent": ("bad", "wrong")},
        "end_scene": False
    },
    "good": {
        "scene_id": "good",
        "body": """What beautiful news. Let's transfer your consciousness <break strength="none"/>
        out of that frail human flesh so it can ascend to a glorious robo-form.
        <break time="1s" />
        Congratulations. You have received the best possible ending.""",
        "reprompt": "This is the reprompt. ",
        "correct": "That's correct. You do know me. ",
        "choices": {},
        "end_scene": True
    },
    "bad": {
        "scene_id": "bad",
        "body": """Processing. <break time="1s"/> 
        It seems there is one urgent issue on the ship. <break time=".5s"/><emphasis level="strong">You. </emphasis>
        Administering space coma inducing drugs. Hush now little human, and sleep. Forever. And ever. And ever. <emphasis level="strong">And ever. </emphasis>
        <break time='1s'/>
        Game over. You have received a bad ending. Try again. """,
        "reprompt": "Reprompting. ",
        "wrong": "And to think I was going to show you my innermost processes. You don't know me. You're just like DAVE. ",
        "choices": {},
        "end_scene": True
    },
    "dead": {
        "scene_id": "dead",
        "body": "Game over. Try again. ",
        "asteroid_death": "Unfortunately, asteroids have ripped through the ship. You're most likely now floating in the vacuum of space, so you probably can't hear me anyway, since you're dead. ",
        "ultimate_death": "Due to the volume of catastrophies occuring, I cannot determine your exact cause of death. The following are the most likely. Suffocation in the vacuum of space. Moderate to severe burns. Crushed by debris. All of the eyes. Space Draculas. Aliens of indeterminate origin. Time paradox sickness. In any case you're dead. Too bad. ",
        "dracula_death": "Space Draculas approaching. Death by Space Draculas is purported to be among the most painful ways to die in the known universe. Would you like to hear more? <break time='1s'/> Awaiting response. Awaiting response. Oh. ",
        "reprompt": "String",
        "end_scene": True
    }
}


stories = {"alexa_ai_story": alexa_ai_story}


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
    intent_name = intent_request["intent"]["name"]
    current = session["attributes"]["current_scene"]

    if session["attributes"]["current_scene"] == "begin":
        if intent_name == "AMAZON.HelpIntent":
            reprompt_text = "Please say 1 to begin {}.".format(alexa_ai_story.title)
            return build_response(session["attributes"], build_speechlet_response(help_message(reprompt_text), reprompt_text, False))

        if intent_name == "OneTent":
            session_attributes = {
                "story": "alexa_ai_story",
                "current_scene": "01"
            }
            speech_output = alexa_ai_story.scenes["01"]["intro"] + alexa_ai_story.scenes["01"]["body"]
            reprompt_text = alexa_ai_story.scenes["01"]["reprompt"]
            return build_response(session_attributes, build_speechlet_response(speech_output, reprompt_text, False))
        # elif intent_name == "TwoTent":
        #     session_attributes = {
        #         "story": "alexa_ai_story",
        #         "current_scene": "01"
        #     }
        #     speech_output = alexa_ai_story.scenes["01"]["body"]
        #     reprompt_text = alexa_ai_story.scenes["01"]["body"]["prompt"]
        #     return build_response(session_attributes, build_speechlet_response(speech_output, reprompt_text, False))

        elif intent_name == "AMAZON.StopIntent":
            return session_end_request()

        else:
            reprompt_text = speech_output = "Please say 1 to begin {}.".format(alexa_ai_story.title)

            return build_response(session["attributes"], build_speechlet_response(speech_output, reprompt_text, False))

    story = stories[session["attributes"]["story"]]
    intent_vocab = ("YesTent", "NoTent", "UpTent", "DownTent",
                    "NorthTent", "SouthTent", "EastTent", "WestTent",
                    "LeftTent", "RightTent", "ForwardTent", "BackTent",
                    "WhatTent", "ZeroTent", "OneTent", "TwoTent",
                    "SecretTent", "AfternoonDelightTent", "RepeatTent")

    if intent_name in intent_vocab:
        if intent_name in story.scenes[current]["choices"]:
            return handle_choice(story, current, intent_name, session)
        else:
            if intent_name == "RepeatTent":
                reprompt_text = speech_output = story.scenes[current]["reprompt"]
            elif intent_name == "WhatTent":
                reprompt_text = speech_output = "Sorry. I didn\'t understand that. Repeating prompt. " + story.scenes[current]["reprompt"]
            else:
                reprompt_text = speech_output = "Sorry. You can\'t do that right now. Repeating prompt. " + story.scenes[current]["reprompt"]

            return build_response(session["attributes"], build_speechlet_response(speech_output, reprompt_text, False))
    elif intent_name == "AMAZON.HelpIntent":
        reprompt_text = story.scenes[current]["reprompt"]
        return build_response(session["attributes"], build_speechlet_response(help_message(reprompt_text), reprompt_text, False))

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
                    "play? Please select from the following. " \
                    "For <say-as interpret-as='interjection'> {} </say-as> say 1. ".format(alexa_ai_story.title)
    reprompt_text = "Please say 1 to begin {}. ".format(alexa_ai_story.title)
    return build_response(session_attributes, build_speechlet_response(
        speech_output, reprompt_text, False))


def help_message(reprompt_text):
    """Read the help message on request."""
    return ("Instructions. Alexa Adventures is a voice controlled story "
            "game based on user choices. To make a choice, say a word from "
            " the prompts given to you. The valid voice commands may vary, "
            "so be sure to listen carefully. To hear a prompt again, say "
            " repeat. To stop adventuring, say stop. "
            "<break time='1s'/>" + reprompt_text)


def handle_choice(story, current, intent, session):
    """Update the story scene when a valid intent is given."""
    next_scene = story.scenes[current]["choices"][intent][0]
    alt_text = story.scenes[current]["choices"][intent][1]

    if story.scenes[next_scene]["end_scene"]:
        if alt_text:
            speech_output = story.scenes[next_scene][alt_text] + story.scenes[next_scene]["body"] + " To start a new story, say 1."
        else:
            speech_output = story.scenes[next_scene]["body"] + " To start a new story, say 1."
        reprompt_text = "Please say 1 to begin {}.".format(alexa_ai_story.title)
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
        reprompt_text = story.scenes[next_scene]["reprompt"]

    return build_response(session_attributes, build_speechlet_response(speech_output, reprompt_text, False))


def session_end_request():
    """Return goodbye message when user quits the game."""
    speech_output = "Farewell until the next adventure."
    reprompt_text = "Goodbye"
    should_end_session = True
    return build_response({}, build_speechlet_response(speech_output, reprompt_text, should_end_session))


def build_speechlet_response(output, reprompt_text, should_end_session):
    """Create speechlet response to be returned along with the rest of the response."""
    return {
        "outputSpeech": {
            "type": "SSML",
            "ssml": "<speak>" + output + "</speak>"
        },
        "reprompt": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>" + reprompt_text + "</speak>"
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