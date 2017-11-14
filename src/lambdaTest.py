"""Test our understanding of the lambda function."""
import random

dinnerOptions = [
    "Chicken",
    "Beef",
    "Pork",
    "Fish",
    "Vegetarian"
]

sides = [
    "Mashed Potatoes",
    "Macaroni and Cheese",
    "Asparagus",
]


def lambda_handler(event, context):
    """Handle the lambda."""
    print("Damnit alexa don't be a bitch")
    if event["request"]["intent"]["name"] == "DinnerBotIntent":
        dinner = random.choice(dinnerOptions)
        response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': dinner,
                }
            }
        }
    else:
        app = random.choice(sides)
        response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': app,
                }
            }
        }

    return response
