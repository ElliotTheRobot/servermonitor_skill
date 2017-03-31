from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'heinzdonnellyschmidt'

LOGGER = getLogger(__name__)


class ServerMonitorSkill(MycroftSkill):
    def __init__(self):
        super(ServerMonitorSkill, self).__init__(name="ServerMonitorSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        # check server X intent
        self.register_regex("server (?P<ServerNum>\w*)")
        checkserver_intent = IntentBuilder("CheckServerIntent").\
            require("VerbKeyword").\
            require("SubjectKeyword").\
            optionally("ServerNum").build()
        self.register_intent(checkserver_intent, self.handle_checkserver_intent)

    def handle_checkserver_intent(self, message):
        singleServer = message.data.get("ServerNum", None)
        if singleServer:
            self.speak(singleServer)
        elif message.data:
                self.speak(message.data)
        else:
            self.speak("No data")

    def stop(self):
        pass


def create_skill():
    return ServerMonitorSkill()