import requests
import datetime
import csv
import os


class Slots:
    base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/"
    browser_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
    }
    district = {}

    def __init__(self):
        cwd = os.path.dirname(__file__)  # get current location
        reader = csv.reader(open(os.path.join(cwd, "district.csv"), "r"))
        for row in reader:
            k, v = row
            self.district[k] = v

    def get_slots_by_pincode(self, input_pincode, date):
        slots_by_pincode_url = (
            self.base_url
            + "findByPin?pincode={input_pincode}&date={date}".format(
                input_pincode=input_pincode, date=date
            )
        )
        print(slots_by_pincode_url)
        try:
            resp = requests.get(slots_by_pincode_url, headers=self.browser_header)
            slots_available_message = []
            if resp.ok:
                slots_resp = resp.json()
                sessions = slots_resp["sessions"]
                index = 1
                for session in sessions:
                    present = self.check_capacity(session)
                    if present:
                        message = self.get_message(session)
                        if not slots_available_message:
                            slots_available_message.append(str(index) + ". " + message)
                        else:
                            slots_available_message.append("\n")
                            slots_available_message.append(str(index) + ". " + message)
                        index += 1
            return slots_available_message
        except Exception as e:
            print("exception occurred while calling the slots api", e)
            return f"Sorry to inform you that we are not able to get the vaccine slots currently!!"

    def get_slots_by_district(self, input_district, date):
        district_id = self.district.get(input_district.lower().title(), None)
        if district_id is None:
            return None
        slots_by_dist_url = (
            self.base_url
            + "findByDistrict?district_id={district_id}&date={date}".format(
                district_id=district_id, date=date
            )
        )
        print(slots_by_dist_url)
        try:
            resp = requests.get(slots_by_dist_url, headers=self.browser_header)
            slots_available_message = []
            if resp.ok:
                slots_resp = resp.json()
                sessions = slots_resp["sessions"]
                index = 1
                for session in sessions:
                    present = self.check_capacity(session)
                    if present:
                        message = self.get_message(session)
                        if not slots_available_message:
                            slots_available_message.append(str(index) + ". " + message)
                        else:
                            slots_available_message.append("\n")
                            slots_available_message.append(str(index) + ". " + message)
                        index += 1
            return slots_available_message
        except Exception as e:
            print("exception occurred while calling the slots api", e)
            return f"Sorry to inform you that we are not able to get the vaccine slots currently!!"

    def get_message(self, session):
        name = session["name"]
        address = session["address"]
        district_name = session["district_name"]
        block_name = session["block_name"]
        pincode = session["pincode"]
        available_capacity = session["available_capacity"]
        min_age_limit = session["min_age_limit"]
        vaccine = session["vaccine"]
        return self.get_slot_message(
            name,
            address,
            district_name,
            block_name,
            pincode,
            available_capacity,
            min_age_limit,
            vaccine,
        )

    def check_capacity(self, session):
        available_capacity = session["available_capacity"]
        if int(available_capacity) > 0:
            return True
        return False

    def get_slot_message(
        self,
        name,
        address,
        district_name,
        block_name,
        pincode,
        available_capacity,
        min_age_limit,
        vaccine,
    ):
        return f"Centre: {name} | Address: {address}, District: {district_name}, Block: {block_name}, Pin: {pincode:d} | Doses available: {available_capacity:d} | Age Group: {min_age_limit:d}+ | Vaccine: {vaccine}."
