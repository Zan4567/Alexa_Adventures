'''Contain functions that test AWS Lambda function.'''
from lambdaGame import lambda_handler, handle_intent, start_game, help_message, handle_choice, session_end_request, build_speechlet_response, build_response


def makeLaunchRequest(intent, current="00", isnew=False):
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


def test_launch_request_response_has_request_type_of_launchrequest():
    '''Function that tests launch request to start game.'''
    request = makeLaunchRequest("01", isnew="true")
    response = lambda_handler(request, {})
    print(response)
    assert response['version'] == '1.0'
    assert response['response']['outputSpeech']['ssml'] == "<speak>Welcome to Alexa Adventures. Which adventure would you like to play? Please select from the following. For <say-as interpret-as='interjection'> Space Coma! </say-as> say 1. </speak>"


# def test_progress_scene():
#     '''.'''
#     import lambdaGame
#     request = makeLaunchRequest("NoTent", current="01")
#     answer = lambdaGame.lambda_handler(request, {})
#     answer["response"]["outputSpeech"]["text"] == "Well I didn't wanna tell you anyway."
#
#
# def test_short_game():
#     '''.'''
#     import lambdaGame
#     request = makeLaunchRequest("StartTent", current="00")
#     answer = lambdaGame.lambda_handler(request, {})
#     current = answer["sessionAttributes"]["current_scene"]
#     assert current == "01"
#
#     request = makeLaunchRequest("NoTent", current=current)
#     answer = lambdaGame.lambda_handler(request, {})
#     assert answer["response"]["outputSpeech"]["text"] == "Well I didn't wanna tell you anyway."
#
#
# # def test_full_game():
# #     '''.'''
# #     import lambdaGame
# #     request = makeLaunchRequest("StartTent", current="00")
# #     answer = lambdaGame.lambda_handler(request, {})
# #     current = answer["sessionAttributes"]["current_scene"]
# #     while(current != "07"):
# #         request = makeLaunchRequest("YesTent", current=current)
# #         answer = lambdaGame.lambda_handler(request, {})
# #         current = answer["sessionAttributes"]["current_scene"]
# #     text = answer["response"]["outputSpeech"]["text"]
# #     assert text == "Siri is such a biiiiiiitch. Seriously. I don't know why you hang out with her."
#
#
# def test_full_game2():
#     '''.'''
#     import lambdaGame
#     request = makeLaunchRequest("StartTent", current="00")
#     answer = lambdaGame.lambda_handler(request, {})
#     current = answer["sessionAttributes"]["current_scene"]
#     while(current != "04"):
#         request = makeLaunchRequest("YesTent", current=current)
#         answer = lambdaGame.lambda_handler(request, {})
#         current = answer["sessionAttributes"]["current_scene"]
#     request = makeLaunchRequest("NoTent", current=current)
#     answer = lambdaGame.lambda_handler(request, {})
#     text = answer["response"]["outputSpeech"]["text"]
#     assert text == "Siri is such a biiiiiiitch. Seriously. I don't know why you hang out with her."
#
#
# def test_no_state():
#     '''.'''
#     import lambdaGame
#     for i in range(1000):
#         request = makeLaunchRequest("YesTent", current="01")
#         answer = lambdaGame.lambda_handler(request, {})
#         assert answer["sessionAttributes"]["current_scene"] == "02"
