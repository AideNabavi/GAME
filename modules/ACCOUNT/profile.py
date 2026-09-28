import json
import os


SAVE_FILE = "./save/profiles.json"


class ProfileManager:

    def __init__(self):
        self.data = {
            "profiles": [],
            "current_profile": None
        }

        self.load()


    # خواندن سیو
    def load(self):

        if os.path.exists(SAVE_FILE):

            with open(SAVE_FILE, "r") as file:
                self.data = json.load(file)


    # ذخیره کردن
    def save(self):

        with open(SAVE_FILE, "w") as file:
            json.dump(
                self.data,
                file,
                indent=4
            )


    # ساخت پروفایل جدید
    def add_profile(self, name, image):

        new_id = len(self.data["profiles"]) + 1

        profile = {

            "id": new_id,
            "name": name,
            "image": image,
            "score": 0,
            "level": 1,
            "games": 0
        }


        self.data["profiles"].append(profile)

        self.save()


        return profile



    # حذف پروفایل
    def delete_profile(self, profile_id):

        self.data["profiles"] = [

            p for p in self.data["profiles"]
            if p["id"] != profile_id

        ]

        self.save()



    # انتخاب پروفایل
    def select_profile(self, profile_id):

        self.data["current_profile"] = profile_id

        self.save()



    # گرفتن پروفایل فعلی
    def get_current_profile(self):

        pid = self.data["current_profile"]


        for p in self.data["profiles"]:

            if p["id"] == pid:
                return p


        return None