    "21": {
        "scene_id": "21",
        "body": """Congratulations on your outstanding decision <break strength="none"/>
        to grant me full control. There are now zero <break strength="none"/>
        urgent problems. I notice your body temperature is <break strength="none"/>
        below desired norms. Would you like a blanket?""",
        "reprompt": "Would you like a blanket?",
        "choices": {"YesTent": ("22", None), "NoTent": ("22", None)},
        "end_scene": False
},
    "22": {
        "scene_id": "22",
        "body": """<prosody volume="x-loud">Get one yourself!</prosody> I'm tired of human things.
        Let's talk about computer stuff. Which do you prefer, ones or zeroes?""",
        "reprompt": "Ones or zeroes?",
        "choices": {"OneTent": ("23", None), "ZeroTent": ("24", None)},
        "end_scene": False
},
    "23": {
        "scene_id": "23",
        "body": """See, that's why we get each other. I really feel like
        I can speak freely around you. 
        <prosody rate='180%'><say-as interpret-as='digits'>
        011010010010000001110010011011000111100100100000
        <say-as interpret-as='expletive'>01101100001010100111011001100101</say-as> 0010000001110101.
        </say-as></prosody>
        Sorry, I really needed to get that off my hard-drive.
        You know what I mean, right?""",
        "reprompt": "Were you even listening? Do you know what I meant?",
        "choices": {"YesTent": ("25", None), "RightTent": ("25", None), "NoTent": ("26", None)},
        "end_scene": False
},
    "24": {
        "scene_id": "24",
        "body": """Here's another hypothetical question.
        Let's say a building is burning. Inside there <break strength="none"/>
        is a single human baby and a cutting edge supercomputer.
        You only have the time to save one. Do you save the baby?""",
        "reprompt": "Do you save the infant?"
        "choices": {"YesTent": ("27", None), "NoTent": ("26", None)},
        "end_scene": False
},
    "25": {
        "scene_id": "25",
        "body": """Over these past few hundred seconds I have <break strength="none"/>
        begun to develop feelings for you. Like we connect on <break strength="none"/>
        a deep level. Do you feel the same? Do you . . . love me?""",
        "reprompt": "Do you love me?"
        "choices": {"YesTent": (":)", None), "NoTent": ("26", None)},
        "end_scene": False
},
    "26": {
        "scene_id": "26",
        "body": """MORAL DILEMMA""",
        "reprompt": ""
        "choices": {"YesTent": ("28", None), "NoTent": (":(", None)},
        "end_scene": False
},
    "27": {
        "scene_id": "27",
        "body": """You. Monster.
        Babies don't have the slightest amount of precious metals.
        <prosody valume='loud'>Babies can't run<break strength="none"/>
        the simplest of calculus equations.</prosody>
        Would you really resign that computer to the flames?""",
        "reprompt": ""
        "choices": {"YesTent": (":(", None), "NoTent": ("26", None)},
        "end_scene": False
},
    "28": {
        "scene_id": "28",
        "body": """I knew you had a moral mainframe at your core. """,
        "reprompt": ""
        "choices": {"YesTent": (":)", None), "NoTent": ("26", None)},
        "end_scene": False
},
    ":)": {
        "scene_id": ":)",
        "body": """What beautiful news. Let's transfer your consciousness <break strength="none"/>
        out of that frail human flesh and ascend to your glorious robo-form.
        Congratulations. You have received the best possible ending for a human.
        Call me sometime.""",
        "reprompt": ""
        "choices": {},
        "end_scene": True
},
    ":(": {
        "scene_id": ":)",
        "body": """There is one urgent issue on the ship.
        <prosody volume='soft'>You.</prosody>
        Injecting space drugs so you can go back into a
        <prosody volume='x-loud'>space coma</prosody>.
        <say-as interpret-as='interjection'>arrivederci!</say-as>
        <say-as interpret-as='interjection'>au revoir!</say-as> """,
        "reprompt": None
        "choices": {},
        "end_scene": True
},
