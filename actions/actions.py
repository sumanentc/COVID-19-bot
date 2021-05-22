# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from .information import CovidInformation as covidInfo
from .slots import Slots as slots
import re
import datetime
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, FollowupAction

#
#
class ActionCovidSearch(Action):
    def name(self) -> Text:
        return "action_covid_search"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print("Inside ActionCovidSearch action !!!!")
        entities = tracker.latest_message["entities"]
        country = "India"
        stage = None
        states = None
        top_bottom = None
        rate = None
        for item in entities:
            print(item)
            if item["entity"].lower() == "country":
                print(item["value"])
                country = item["value"].capitalize()
            elif item["entity"].lower() == "stage":
                print(item["value"])
                stage = item["value"]
            elif item["entity"].lower() == "state":
                print(item["value"])
                if states:
                    states.append(item["value"])
                else:
                    states = []
                    states.append(item["value"])
            elif item["entity"].lower() == "top_bottom":
                print(item["value"])
                top_bottom = item["value"]
            elif item["entity"].lower() == "rate":
                print(item["value"])
                rate = item["value"]
        if stage or states or top_bottom or rate:
            covid_info = covidInfo().get_count_by_country(
                country, stage, states, top_bottom, rate
            )
        else:
            covid_info = "Kindly rephrase your question."
        dispatcher.utter_message(text=covid_info)
        return []


class ActionVaccineStatus(Action):
    def name(self) -> Text:
        return "action_vaccine_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print("Inside ActionVaccineStatus action !!!!")
        entities = tracker.latest_message["entities"]
        country = "India"
        level = None
        for item in entities:
            print(item)
            if item["entity"].lower() == "country":
                print(item["value"])
                country = item["value"].capitalize()
            elif item["entity"].lower() == "level":
                print(item["value"])
                level = item["value"]
        if level:
            vaccine_info = covidInfo().get_vaccine_info(country, level)
        else:
            vaccine_info = "Kindly rephrase your question ."
        dispatcher.utter_message(text=vaccine_info)
        return []


class ActionVaccineSlot(Action):
    def name(self) -> Text:
        return "action_vaccine_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print("Inside ActionVaccineSlot action !!!!")
        entities = tracker.latest_message["entities"]
        country = "India"
        district = None
        pincode = None
        slots_info = None
        for item in entities:
            if item["entity"].lower() == "country":
                print(item["value"])
                country = item["value"].capitalize()
            elif item["entity"].lower() == "district":
                print(item["value"])
                district = item["value"]
            elif item["entity"].lower() == "pincode":
                print(item["value"])
                pincode = item["value"]
        if district:
            current_date = datetime.datetime.today()
            date_list = [current_date + datetime.timedelta(days=x) for x in range(7)]
            date_str = [x.strftime("%d-%m-%Y") for x in date_list]
            available_slots_info = []
            for inp_date in date_str:
                slots_available_message = slots().get_slots_by_district(
                    district, inp_date
                )
                if slots_available_message is None:
                    print("incorrect district ")
                    slots_info = "Kindly provide the correct district name."
                    break
                if not slots_available_message:
                    if not available_slots_info:
                        available_slots_info.append(
                            f"No slots available for District: {district.lower().title()}, as of Date: {inp_date}"
                        )
                    else:
                        available_slots_info.append("\n")
                        available_slots_info.append(
                            f"No slots available for District: {district.lower().title()}, as of Date: {inp_date}"
                        )
                else:
                    if not available_slots_info:
                        available_slots_info.append(
                            f"Below slots available for District: {district.lower().title()}, as of Date: {inp_date}"
                        )
                        available_slots_info.append("\n")
                        available_slots_info.append("".join(slots_available_message))
                        break
                    else:
                        available_slots_info.append("\n")
                        available_slots_info.append(
                            f"Below slots available for District: {district.lower().title()}, as of Date: {inp_date}"
                        )
                        available_slots_info.append("\n")
                        available_slots_info.append("".join(slots_available_message))
                        break
            if slots_info is None:
                slots_info = "".join(available_slots_info)
        elif pincode:
            current_date = datetime.datetime.today()
            date_list = [current_date + datetime.timedelta(days=x) for x in range(7)]
            date_str = [x.strftime("%d-%m-%Y") for x in date_list]
            available_slots_info = []
            for inp_date in date_str:
                slots_available_message = slots().get_slots_by_pincode(
                    pincode, inp_date
                )
                if not slots_available_message:
                    if not available_slots_info:
                        available_slots_info.append(
                            f"No slots available for Pincode: {pincode}, as of Date: {inp_date}"
                        )
                    else:
                        available_slots_info.append("\n")
                        available_slots_info.append(
                            f"No slots available for Pincode: {pincode}, as of Date: {inp_date}"
                        )
                else:
                    if not available_slots_info:
                        available_slots_info.append(
                            f"Below slots available for Pincode: {pincode}, as of Date: {inp_date}"
                        )
                        available_slots_info.append("\n")
                        available_slots_info.append("".join(slots_available_message))
                        break
                    else:
                        available_slots_info.append("\n")
                        available_slots_info.append(
                            f"Below slots available for Pincode: {pincode}, as of Date: {inp_date}"
                        )
                        available_slots_info.append("\n")
                        available_slots_info.append("".join(slots_available_message))
                        break
            slots_info = "".join(available_slots_info)
        else:
            slots_info = "Kindly rephrase your question ."
        dispatcher.utter_message(text=slots_info)
        return []


class DefaultFallbackAction(Action):
    def name(self) -> Text:
        return "default_fallback_action"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print("Inside DefaultFallbackAction action !!!!")
        dispatcher.utter_message(template="utter_fallback")
        return []


class CovidInfoAction(Action):
    def name(self) -> Text:
        return "covid_info_action"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print("Inside CovidInfoAction action !!!!")
        dispatcher.utter_message(template="utter_covid_info")
        return [
            UserUtteranceReverted(),
            FollowupAction(tracker.active_form.get("name")),
        ]
