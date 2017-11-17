# Alexa Adventures
_By Team Alpha_

## Description

Alexa Adventures is a series of narrative adventure games controlled by voice commands from the user. Repair a spaceship, hear what Alexa has been keeping secret, or engage in casual small-talk with a super-intelligent AI, all with a few utterances and from the comfort of your own living room. An update to the classic choose-your-own-adventure, Alexa Adventures aims to supply a unique user experience.

In creating Alexa Adventures, we utilized [Amazon Echo's Alexa API](https://developer.amazon.com/docs/alexa-voice-service/api-overview.html) to create an [Alexa Skill](https://developer.amazon.com/docs/ask-overviews/build-skills-with-the-alexa-skills-kit.html). To see how we did it or to report any bugs, feel free to check our [Alexa Adventures repo on Github](https://github.com/Zan4567/Alexa_Adventures).

#### How to play Alexa Adventures:
1. Ensure that your Amazon Echo is plugged in and connected to wifi.
2. To start Alexa Adventures, simply say, **"Alexa, take me on an adventure."**
3. Alexa will then bring up the Main Menu for Alexa Adventures. At this point she will list the available adventures for you to choose from. To start a particular adventure, **say the name of the adventure.**
4. Once you've started your adventure, Alexa will give you prompts; and you, the adventurer, will make choices accordingly using voice commands.*

Be aware that certain choices you make have the potential to end the current adventure. If this occurs, Alexa will notify you, bring you back to the Main Menu, and from there you have the option to play again or exit Alexa Adventures.

*_Note: The voice commands you're allowed to give Alexa vary based upon the adventure, so be sure to listen to the opening prompt when you first begin your adventure._

## To contribute to Alexa Adventures:

#### Environment Setup:

In order to contribute to Alexa Adventures, your environment must be set up with certain tools and resources, including: pytest, pytest-cov, and tox (which must be configured to run both Python 2.7 and Python 3.6). The steps to create an environment and install the necessary tools from your **command prompt** are as follows:
1. Open your command prompt and clone down the Alexa Adventures repository by typing ```git clone https://github.com/Zan4567/Alexa_Adventures.git```.
2. After the repository has been cloned down, change directories into the Alexa_Adventures repository by typing ```cd Alexa_Adventures```.
3. Once inside the Alexa_Adventures repository, type ```python3 -m venv ENV``` to create a virtual environment. To ensure the virtual environment was  successfully created, you can type ```ls``` and check for a directory called ```ENV```.
4. Next, activate the newly created virtual environment by typing ```source ENV/bin/activate```. Note that if the virtual environment has been successfully activated your command prompt should now look slightly different. For example, if before following these steps my command prompt looked like this ```user@computer:~$```, it should now look similar to this ```(ENV) user@computer:~$``` if my environment was setup and activated correctly.
5. Finally, run ```pip install -e .[testing]``` to install the dependencies necessary for testing. If everything was done correctly you should now be able to run ```tox``` and ```pytest``` from your activated environment.

## Authors:
_Click the author's name to check out their Github!_

- [Carson Newton](https://github.com/nosrac77)
- [Brendan Davis](https://github.com/Tsarcastic)
- [Allan Liebold](https://github.com/allanliebold)
- [Kevin Robinson](https://github.com/Zan4567)

## Resources Used:

To create Alexa Adventures we used a lot of great software that we feel deserves credit. Below is a list of any external libraries, API's, or other programs that made this project possible. Click on a link to learn more about that software!

#### Testing:
- [Pytest](https://docs.pytest.org/en/latest/)
- [Pytest-cov](https://pypi.python.org/pypi/pytest-cov)
- [Tox](https://tox.readthedocs.io/en/latest/)

#### Hosting/Functionality:
- [Amazon AWS](https://aws.amazon.com/)
- [Amazon Alexa Skills](https://developer.amazon.com/alexa-skills-kit)
