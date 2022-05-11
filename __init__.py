from mycroft import MycroftSkill, intent_file_handler


class TheLittlePrince(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('prince.little.the.intent')
    def handle_prince_little_the(self, message):
        self.speak_dialog('prince.little.the')


def create_skill():
    return TheLittlePrince()

