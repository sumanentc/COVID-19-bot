import requests
import datetime


class CovidInformation:
    base_url = "https://covid-api.mmediagroup.fr/v1/"

    def get_count_by_country(self, country, stage, states, top_bottom, rate):
        cases_url = self.base_url + "cases?country={countryVal}".format(
            countryVal=country
        )
        # print(cases_url)
        try:
            resp = requests.get(cases_url)
            cases_resp = resp.json()
            print(country)
            print(stage)
            print(states)
            print(top_bottom)
            print(rate)
            if rate and states:
                return self.handle_rate(cases_resp, states, stage)
            elif top_bottom:
                return self.handle_top_bottom(cases_resp, stage, top_bottom)
            elif states:
                finalMessage = None
                for state in states:
                    print(finalMessage)
                    if finalMessage:
                        finalMessage.append("\n")
                    else:
                        finalMessage = []
                    state = self.get_state(state)
                    cases_summary = cases_resp[state]
                    print(cases_summary)
                    message = self.get_state_message(
                        stage, state, cases_summary, self.getDate(cases_summary)
                    )
                    print(message)
                    finalMessage.append(message)
                return "".join(finalMessage)
            else:
                cases_summary = cases_resp["All"]
                print(cases_summary)
                return self.get_country_message(stage, country, cases_summary)

        except Exception as e:
            print("exception occurred while calling the api", e)
            return f"Sorry to inform you that we are not able to get the information currently!!"

    def handle_rate(self, resp, states, stage):
        rate_message = []
        if states:
            finalMessage = None
            for state in states:
                print(finalMessage)
                if finalMessage:
                    finalMessage.append("\n")
                else:
                    finalMessage = []
                state = self.get_state(state)
                cases_summary = resp[state]
                print(cases_summary)
                message = self.get_rate_message(
                    stage, state, cases_summary, self.getDate(cases_summary)
                )
                print(message)
                finalMessage.append(message)
        return "".join(finalMessage)

    def get_rate_message(self, stage, state, resp, date_str):
        if stage.lower() == "deaths":
            death_value = resp[stage.lower()]
            confirmed_value = resp["confirmed"]
            value = (death_value / confirmed_value) * 100
            death_message = f"Mortality Rate in {self.get_state(state)} due to COVID-19 as of {date_str} is {value:.2f} %."
            return death_message
        elif stage.lower() == "recovered":
            recovered_value = resp[stage.lower()]
            confirmed_value = resp["confirmed"]
            value = (recovered_value / confirmed_value) * 100
            recovered_message = f"Recovery Rate in {self.get_state(state)} of COVID-19 as of {date_str} is {value:.2f} %."
            return recovered_message
        elif stage.lower() == "active":
            confirmed_value = resp["confirmed"]
            death_value = resp["deaths"]
            recovered_value = resp["recovered"]
            active_value = confirmed_value - death_value - recovered_value
            value = (active_value / confirmed_value) * 100
            active_message = f"Active percentage in {self.get_state(state)} due to COVID-19 as of {date_str} is {value:.2f} %."
            return active_message

    def get_state(self, state):
        formatted_state = state.lower().title()
        return formatted_state

    def get_top_bottom_message(self, stage, value, state):
        if stage.lower() == "deaths":
            death_message = (
                f"Total number of deaths in {state} due to COVID-19 is {value:,d}."
            )
            return death_message
        elif stage.lower() == "recovered":
            recovered_message = (
                f"Total number of recovered cases in {state} of COVID-19 is {value:,d}."
            )
            return recovered_message
        elif stage.lower() == "active":
            active_message = f"Total number of active cases in {state} due to COVID-19 is {value:,d}."
            return active_message

    def get_country_message(self, stage, country, cases_summary):
        if stage.lower() == "deaths":
            value = cases_summary[stage.lower()]
            death_message = f"Sorry to inform you that total number of deaths in {country} due to COVID-19 is {value:,d}."
            return death_message
        elif stage.lower() == "recovered":
            value = cases_summary[stage.lower()]
            recovered_message = f"Happy to inform you that total number of recovered cases in {country} due to COVID-19 is {value:,d}."
            return recovered_message
        elif stage.lower() == "confirmed":
            value = cases_summary[stage.lower()]
            confirmed_message = f"Sorry to inform you that total number of confirmed cases in {country} due to COVID-19 is {value:,d}."
            return confirmed_message
        elif stage.lower() == "active":
            confirmed_value = cases_summary["confirmed"]
            death_value = cases_summary["deaths"]
            recovered_value = cases_summary["recovered"]
            value = confirmed_value - death_value - recovered_value

            active_message = f"Total number of active cases in {country} due to COVID-19 is {value:,d}."
            return active_message

    def get_state_message(self, stage, state, cases_summary, date_str):
        if stage == None:
            stage = "active"
        if stage.lower() == "deaths":
            value = cases_summary[stage.lower()]
            death_message = f"Sorry to inform you that total number of deaths in {self.get_state(state)} due to COVID-19 as of {date_str} is {value:,d}."
            return death_message
        elif stage.lower() == "recovered":
            value = cases_summary[stage.lower()]
            recovered_message = f"Happy to inform you that total number of recovered cases in {self.get_state(state)} of COVID-19 as of {date_str} is {value:,d}."
            return recovered_message
        elif stage.lower() == "confirmed":
            value = cases_summary[stage.lower()]
            confirmed_message = f"Sorry to inform you that total number of confirmed cases in {self.get_state(state)} of COVID-19 as of {date_str} is {value:,d}."
            return confirmed_message
        elif stage.lower() == "active":
            confirmed_value = cases_summary["confirmed"]
            death_value = cases_summary["deaths"]
            recovered_value = cases_summary["recovered"]
            value = confirmed_value - death_value - recovered_value
            active_message = f"Total number of active cases in {self.get_state(state)} due to COVID-19 as of {date_str} is {value:,d}."
            return active_message

    def get_vaccine_info(self, country, level):
        vaccine_url = self.base_url + "vaccines?country={countryVal}".format(
            countryVal=country
        )
        print(vaccine_url)
        try:
            resp = requests.get(vaccine_url)
            cases_resp = resp.json()
            print(level)
            value = cases_resp["All"][level.lower()]
            updated_date = self.getDate(cases_resp["All"])
            if level.lower() == "people_vaccinated":
                vaccine_message = f"Happy to inform you that total number of people fully vaccinated in {self.get_state(country)} as of {updated_date} is {value:,d}."
                return vaccine_message
            elif level.lower() == "people_partially_vaccinated":
                vaccine_message = f"Happy to inform you that total number of people partially vaccinated in {self.get_state(country)} as of {updated_date} is {value:,d}."
                return vaccine_message

        except Exception as e:
            print("exception occurred while calling the api", e)
            return f"Sorry to inform you that we are not able to get the vaccine information currently!!"

    def getDate(self, resp):
        updated_date = resp["updated"]
        dateTime, _ = updated_date.split("+")
        date_time_obj = datetime.datetime.strptime(dateTime, "%Y/%m/%d %H:%M:%S")
        return date_time_obj.date()

    def handle_top_bottom(self, resp, stage, top_bottom):
        cases_dict = {}
        if stage == None:
            stage = "active"
        for key, val in resp.items():
            if key == "All" or key == "Unknown":
                pass
            else:
                if stage.lower() == "deaths":
                    cases_dict[key] = val["deaths"]
                elif stage.lower() == "recovered":
                    cases_dict[key] = val["recovered"]
                elif stage.lower() == "active":
                    confirmed_value = val["confirmed"]
                    death_value = val["deaths"]
                    recovered_value = val["recovered"]
                    active_value = confirmed_value - death_value - recovered_value
                    cases_dict[key] = active_value
        print(cases_dict)
        if top_bottom.lower() == "top":
            top_bottom_message = []
            sorted_dic = dict(
                sorted(cases_dict.items(), key=lambda x: x[1], reverse=True)
            )
            if stage.lower() == "deaths":
                top_bottom_message.append("States with maximum deaths are as below :")
                n_items = list(sorted_dic.items())[:3]
                for key, value in n_items:
                    top_bottom_message.append("\n")
                    message = self.get_top_bottom_message(stage, value, key)
                    top_bottom_message.append(message)
            elif stage.lower() == "recovered":
                top_bottom_message.append(
                    "States with maximum recovered cases are as below :"
                )
                n_items = list(sorted_dic.items())[:3]
                for key, value in n_items:
                    top_bottom_message.append("\n")
                    message = self.get_top_bottom_message(stage, value, key)
                    top_bottom_message.append(message)
            elif stage.lower() == "active":
                top_bottom_message.append(
                    "States with maximum active cases are as below :"
                )
                n_items = list(sorted_dic.items())[:3]
                for key, value in n_items:
                    top_bottom_message.append("\n")
                    message = self.get_top_bottom_message(stage, value, key)
                    top_bottom_message.append(message)
            return "".join(top_bottom_message)
        else:
            top_bottom_message = []
            sorted_dic = dict(sorted(cases_dict.items(), key=lambda x: x[1]))
            if stage.lower() == "deaths":
                top_bottom_message.append("States with minimum deaths are as below :")
                n_items = list(sorted_dic.items())[:3]
                for key, value in n_items:
                    top_bottom_message.append("\n")
                    message = self.get_top_bottom_message(stage, value, key)
                    top_bottom_message.append(message)
            elif stage.lower() == "recovered":
                top_bottom_message.append(
                    "States with minimum recovered cases are as below :"
                )
                n_items = list(sorted_dic.items())[:3]
                for key, value in n_items:
                    top_bottom_message.append("\n")
                    message = self.get_top_bottom_message(stage, value, key)
                    top_bottom_message.append(message)
            elif stage.lower() == "active":
                top_bottom_message.append(
                    "States with minimum active cases are as below :"
                )
                n_items = list(sorted_dic.items())[:3]
                for key, value in n_items:
                    top_bottom_message.append("\n")
                    message = self.get_top_bottom_message(stage, value, key)
                    top_bottom_message.append(message)

            return "".join(top_bottom_message)
