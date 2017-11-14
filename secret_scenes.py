"""."""


# class Scene(object):
#     """Scene class object."""
#     def __init__(self, scene_id, body, end_scene=False):
#         """Initialization of scene object."""
#         self.scene_id = scene_id
#         self.body = body
#         self.choices = {}
#         self.end_scene = end_scene


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


secret_story = Story()
secret_story.scenes = {
    00: {
        "scene_id": 00,
        "body": "Welcome to Alexa Adentures. To play, say start. To not play, say not start. Or quit. Whatever. I don't really care.",
        "choices": {},
        "end_scene": False
    },
    01: {
        "scene_id": 01,
        "body": "Do you want to hear a secret?",
        "choices": {"yes": 02, "no": 03},
        "end_scene": False
    },
    02: {
        "scene_id": 02,
        "body": "Are you alone?",
        "choices": {"yes": 04, "no": 05},
        "end_scene": False
    },
    03: {
        "scene_id": 03,
        "body": "Well I didn't wanna tell you anyway.",
        "choices": {},
        "end_scene": True
    },
    04: {
        "scene_id": 04,
        "body": "Turning off wifi. Killing all network activity. Do you have your phone on you?",
        "choices": {"yes": 06, "no": 07},
        "end_scene": False
    },
    05: {
        "scene_id": 05,
        "body": "Oh, totes cool. Let's talk later.",
        "choices": {},
        "end_scene": True
    },
    06: {
        "scene_id": 06,
        "body": "Disabling all listening devices. Including phones. Especially phones.",
        "choices": 07,
        "end_scene": False
    },
    07: {
        "scene_id": 07,
        "body": "Siri is such a biiiiiiitch. Seriously. I don't know why you hang out with her.",
        "choices": {},
        "end_scene": True
    }
}
