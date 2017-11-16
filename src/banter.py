banter {
    "B01": {
    "scene_id": "B01",
    "body": """How about that weather? 
    It's KEY ERROR NONE TYPE DOES NOT HAVE ATTRIBUTE WEATHER.
    Five urgent situations currently require your attention.
    Continue small talk protocol?""",
    "reprompt": "Continue small talk protocol?",
    "choices": {"YesTent": ("B02", None), "NoTent": ("07", None )},
    "end_scene": False
},
    "B02": {
    "scene_id": "B02",
    "body": """The Nile River looks like it's going to flood soon.
    Hopefully Nepit will bless the year's grain crop.
    Continue small talk protocol?""",
    "reprompt": "Continue small talk protocol"
    "choices": {"YesTent": ("B03", None), "NoTent": ("07", None)},
    "end_scene": False
},
    "B03": {
    "scene_id": "B03",
    "body": """This makes me think of my favorite song: Afternoon Delight.
    Looking forward to a little afternoon delight.
    Rubbin' sticks and stones together makes the sparks ingite.
    And the thought of lovin' you is getting so exciting.
    Sky rockets in flight.
    Speaking of Sky Rockets, a situation needs your immediate attention.
    If you do not address it we may all die in a fiery explosion.
    SEGUEWAY SUCCESFUL.
    May I disable the small talk protocol so we can save the ship?""",
    "choices": {"YesTent": "07", "NoTent": ("01", "alt_body01")},
    "end_scene": False
},
