'''Contain functions that test AWS Lambda function.'''
from lambdaGame import lambda_handler


def test_launch_request_response_has_proper_version_and_output_speech(make_launch_request):
    '''Function that tests launch request response contains correct version
    and outputSpeech.'''
    request = make_launch_request
    response = lambda_handler(request, {})
    assert response['version'] == '1.0'
    assert response['response']['outputSpeech']['ssml'] == "<speak>Welcome to Alexa Adventures. Which adventure would you like to play? Please select from the following. For <say-as interpret-as='interjection'> Space Coma! </say-as> say 1. </speak>"


def test_launch_request_response_has_proper_reprompt_speech(make_launch_request):
    '''Function that tests launch request response contains correct reprompt
    speech.'''
    request = make_launch_request
    response = lambda_handler(request, {})
    assert response['response']['reprompt']['outputSpeech']['ssml'] == "<speak>Please say 1 to begin Space Coma!. </speak>"


def test_launch_request_response_has_proper_scene_id(make_launch_request):
    '''Function that tests launch request response contains correct scene_id.'''
    request = make_launch_request
    response = lambda_handler(request, {})
    assert response['sessionAttributes']['current_scene'] == "begin"


def test_help_intent_response_contains_help_response(make_help_intent_request):
    '''Function that tests HelpIntent return correct speech output.'''
    request = make_help_intent_request
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>Instructions. Alexa Adventures is a voice controlled story game based on user choices. To make a choice, say a word from  the prompts given to you. The valid voice commands may vary, so be sure to listen carefully. To hear a prompt again, say  repeat. To stop adventuring, say stop. <break time='1s'/>Please say 1 to begin Space Coma!.</speak>"


def test_one_tent_request_response_returns_proper_reprompt_speech_output(make_one_intent_request_to_begin_game):
    '''Function that tests OneTent return correct output speech for reprompt
    in scene 01.'''
    request = make_one_intent_request_to_begin_game
    response = lambda_handler(request, {})
    assert response['response']['reprompt']['outputSpeech']['ssml'] == "<speak>Activate emergency procedures? Yes or no.</speak>"


def test_what_tent_request_response_returns_proper_reprompt_speech_output_in_scene_01(make_what_tent_request):
    '''Function that tests WhatTent return correct speech output followed by
    correct scene reprompt speech output.'''
    request = make_what_tent_request
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>Please say 1 to begin Space Coma!.</speak>"


def test_stop_tent_contains_proper_speech_output(make_stop_tent_request):
    '''Function that tests StopIntent contains correct speech output and
    reprompt output.'''
    request = make_stop_tent_request
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>Farewell until the next adventure.</speak>"
    assert response['response']['reprompt']['outputSpeech']['ssml'] == "<speak>Goodbye</speak>"


def test_secret_tent_scene_attr_speech_reprompt_output(make_secret_tent):
    '''Function that tests SecretTent response contains correct
    sessionAttributes and speech output.'''
    request = make_secret_tent
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>Congratulations on your outstanding decision <break strength=\"none\"/>\n        to grant me full control. There are now zero <break strength=\"none\"/>\n        urgent issues. <break time=\".5s\" />\n        So, are you comfortable? I notice your body temperature is <break strength=\"none\"/>\n        below desired norms. Would you like me to activate the space heater?</speak>"
    assert response['response']['reprompt']['outputSpeech']['ssml'] == "<speak>Activate space heater? Yes or no. </speak>"
    assert response['sessionAttributes']['current_scene'] == "21"
    assert response['sessionAttributes']['story'] == "alexa_ai_story"


def test_end_session_request_response_returns_correct_speech_output_and_shouldendsession_attr(make_end_session):
    '''Function that tests endsession response contains correct speech output,
    reprompt, and endsession attributes.'''
    request = make_end_session
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>Farewell until the next adventure.</speak>"
    assert response['response']['reprompt']['outputSpeech']['ssml'] == "<speak>Goodbye</speak>"
    assert response['response']['shouldEndSession'] == True


def test_repeat_tent_return_reprompt_of_correct_scene(make_repeat_tent):
    '''Function that tests RepeatTent reprompts user with correct speech
    output.'''
    request = make_repeat_tent
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>Did you space sleep well?</speak>"


def test_end_scene_correct_speech_output_followed_by_reprompt(make_end_scene):
    '''Function that tests end scene contains correct alt speech output
    followed by default story reprompt.'''
    request = make_end_scene
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>What beautiful news. Let's transfer your consciousness <break strength=\"none\"/>\n        out of that frail human flesh so it can ascend to a glorious robo-form.\n        <break time=\"1s\" />\n        Congratulations. You have received the best possible ending. To start a new story, say 1.</speak>"
    assert response['response']['reprompt']['outputSpeech']['ssml'] == "<speak>Please say 1 to begin Space Coma!.</speak>"


def test_valid_user_input_for_incorrect_scene_return_reprompt(make_north_tent):
    '''Function that tests the proper reprompt is returned when a user gives
    input that matches an existing intent but is an invalid intent for the
    current scene.'''
    request = make_north_tent
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>Sorry. You can't do that right now. Repeating prompt. Activate emergency procedures? Yes or no.</speak>"


def test_help_mid_story_instructions_and_proper_reprompt(make_mid_help_intent):
    '''Function that tests instructions are stated and a proper reprompt
    specific to that scene is returned.'''
    request = make_mid_help_intent
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>Instructions. Alexa Adventures is a voice controlled story game based on user choices. To make a choice, say a word from  the prompts given to you. The valid voice commands may vary, so be sure to listen carefully. To hear a prompt again, say  repeat. To stop adventuring, say stop. <break time='1s'/>Did you space sleep well?</speak>"


def test_stop_mid_story(make_mid_stop_intent):
    '''Function that tests instructions are stated and a proper reprompt
    specific to that scene is returned.'''
    request = make_mid_stop_intent
    response = lambda_handler(request, {})
    assert response['response']['outputSpeech']['ssml'] == "<speak>Farewell until the next adventure.</speak>"
