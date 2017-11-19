"""Module containing pytest fixtures."""
import pytest

@pytest.fixture
def make_launch_request():
    request = {
      "session": {
        "new": True,
        "sessionId": "SessionId.1559d8c0-5012-43ba-904c-3423c5edfd76",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {},
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "LaunchRequest",
        "requestId": "EdwRequestId.7bd7a02a-be9e-474f-9aa6-36a1e2fbfd3d",
        "locale": "en-US",
        "timestamp": "2017-11-17T20:17:12Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_help_intent_request():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.d673023b-5aeb-404c-80f8-1805154e6f6f",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "begin"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.e8396bd0-9637-43ea-aa81-fe110eb77c8e",
        "intent": {
          "name": "AMAZON.HelpIntent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-18T22:19:17Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_one_intent_request_to_begin_game():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.d673023b-5aeb-404c-80f8-1805154e6f6f",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "begin"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.4c6da60d-96d2-4cb1-8acf-d46c63bde16b",
        "intent": {
          "name": "OneTent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-18T22:32:17Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_what_tent_request():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.47503d1e-0376-4042-95fa-85e11edde24a",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "begin"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.5b61641c-6ab7-48d9-9983-4554796e8d43",
        "intent": {
          "name": "WhatTent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-19T00:04:05Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_stop_tent_request():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.ffad942f-ca45-40bc-9bb6-b14fb37002ec",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "begin"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.43cb4f5d-b841-42ea-aa2a-724cf8394af3",
        "intent": {
          "name": "AMAZON.StopIntent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-19T00:01:44Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_secret_tent():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.acbd0320-95b7-482f-aded-8de0c1cf5d3b",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "01",
          "story": "alexa_ai_story"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.fd4e53a9-2eb3-408e-b690-c7ae68a2902f",
        "intent": {
          "name": "SecretTent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-18T23:19:43Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_end_session():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.2ceeb7d7-06fc-4264-bad7-27b8062ee7e6",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "begin"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "SessionEndedRequest",
        "requestId": "EdwRequestId.f4cbfa60-3fae-4e72-84a3-44a951e803ab",
        "reason": "USER_INITIATED",
        "locale": "en-US",
        "timestamp": "2017-11-18T23:31:23Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_repeat_tent():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.241e5c23-947c-4a21-87c5-a4d098405cdc",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "04",
          "story": "alexa_ai_story"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.19dca777-830f-4928-9d42-ce3bc5a8aa10",
        "intent": {
          "name": "RepeatTent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-18T23:41:37Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_end_scene():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.241e5c23-947c-4a21-87c5-a4d098405cdc",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "25",
          "story": "alexa_ai_story"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.68bbedda-6109-42c4-9525-201deb3f3e63",
        "intent": {
          "name": "YesTent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-18T23:47:18Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_north_tent():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.241e5c23-947c-4a21-87c5-a4d098405cdc",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "01",
          "story": "alexa_ai_story"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.dff70120-8bee-444a-b7df-345fa9f1c030",
        "intent": {
          "name": "NorthTent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-18T23:56:45Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_mid_help_intent():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.47503d1e-0376-4042-95fa-85e11edde24a",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "04",
          "story": "alexa_ai_story"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.eef5cf10-694b-468d-9919-145877e490b0",
        "intent": {
          "name": "AMAZON.HelpIntent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-19T00:06:41Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


@pytest.fixture
def make_mid_stop_intent():
    request = {
      "session": {
        "new": False,
        "sessionId": "SessionId.47503d1e-0376-4042-95fa-85e11edde24a",
        "application": {
          "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
        },
        "attributes": {
          "current_scene": "05",
          "story": "alexa_ai_story"
        },
        "user": {
          "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.398142ae-0b5d-4054-9f0d-c402e01ffa9c",
        "intent": {
          "name": "AMAZON.StopIntent",
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-19T00:09:47Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": "amzn1.ask.skill.f288d8b7-03c0-4f6f-92eb-00a21cdf22f3"
          },
          "user": {
            "userId": "amzn1.ask.account.AFWGKBGUH4OG424PX6EBKYGX6IJ5EJL7IODWVHCKMUQONCB6R7PEBCVBF5MUFMKFQC5WDQEESV4RTLTANI4MTANLADCSWKRAYN3VGW6AZZ745IOLP2D3JG7ZJEYOOTEZGVWZIK7R4UE5AEMSUAEPAMYQSV46MN3CTWPG72JAPGKZARBLSZWUROSCQHCIBZSCHRD22AGBZHRKQ6I"
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request
