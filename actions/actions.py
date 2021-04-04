# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from .information import CovidInformation as covidInfo
import re
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
