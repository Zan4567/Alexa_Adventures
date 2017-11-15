'''.'''
import pytest


def makeRequest(intent, current="00", isnew=False):
    request = {
      "session": {
        "new": isnew,
        "sessionId": "SessionId.b12d2d10-739a-483d-a570-afe8fad93a19",
        "application": {
          "applicationId": "amzn1.ask.skill.479ec097-e63c-4755-aab3-38d32b1cd151"
        },
        "attributes": {
            "current_scene": current
        },
        "user": {
          "userId": ""
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.acc52612-ce33-4321-b303-6103698eebdf",
        "intent": {
          "name": intent,
          "slots": {}
        },
        "locale": "en-US",
        "timestamp": "2017-11-13T21:50:12Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": ""
          },
          "user": {
            "userId": ""
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }
    return request


def test_get_response():
    '''.'''
    import lambdaGame
    request = makeRequest("new", isnew="true")
    response = lambdaGame.lambda_handler(request, {})
    assert response['version'] == '1.0'


def test_progress_scene():
    '''.'''
    import lambdaGame
    request = makeRequest("NoTent", current="01")
    answer = lambdaGame.lambda_handler(request, {})
    answer["response"]["outputSpeech"]["text"] == "Well I didn't wanna tell you anyway."


def test_short_game():
    '''.'''
    import lambdaGame
    request = makeRequest("StartTent", current="00")
    answer = lambdaGame.lambda_handler(request, {})
    current = answer["sessionAttributes"]["current_scene"]
    assert current == "01"

    request = makeRequest("NoTent", current=current)
    answer = lambdaGame.lambda_handler(request, {})
    assert answer["response"]["outputSpeech"]["text"] == "Well I didn't wanna tell you anyway."


# def test_full_game():
#     '''.'''
#     import lambdaGame
#     request = makeRequest("StartTent", current="00")
#     answer = lambdaGame.lambda_handler(request, {})
#     current = answer["sessionAttributes"]["current_scene"]
#     while(current != "07"):
#         request = makeRequest("YesTent", current=current)
#         answer = lambdaGame.lambda_handler(request, {})
#         current = answer["sessionAttributes"]["current_scene"]
#     text = answer["response"]["outputSpeech"]["text"]
#     assert text == "Siri is such a biiiiiiitch. Seriously. I don't know why you hang out with her."


def test_full_game2():
    '''.'''
    import lambdaGame
    request = makeRequest("StartTent", current="00")
    answer = lambdaGame.lambda_handler(request, {})
    current = answer["sessionAttributes"]["current_scene"]
    while(current != "04"):
        request = makeRequest("YesTent", current=current)
        answer = lambdaGame.lambda_handler(request, {})
        current = answer["sessionAttributes"]["current_scene"]
    request = makeRequest("NoTent", current=current)
    answer = lambdaGame.lambda_handler(request, {})
    text = answer["response"]["outputSpeech"]["text"]
    assert text == "Siri is such a biiiiiiitch. Seriously. I don't know why you hang out with her."


def test_no_state():
    '''.'''
    import lambdaGame
    for i in range(1000):
        request = makeRequest("YesTent", current="01")
        answer = lambdaGame.lambda_handler(request, {})
        assert answer["sessionAttributes"]["current_scene"] == "02"
