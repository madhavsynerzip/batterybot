from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action

from rasa_core.events import AllSlotsReset


class ActionProvideBatteryOption(Action):
    def name(self):
        return 'action_provide_battery_options'

    def run(self, dispatcher, tracker, domain):
        car_type = tracker.get_slot("car_type")
        if car_type == "diesel":
            dispatcher.utter_message("Following options are available in Diesel Variant: Exide 4500, Amaron 4200")
        else:
            dispatcher.utter_message("Following options are available in Petrol Variant: Exide 4250, Amaron 3900")
        return [AllSlotsReset()]