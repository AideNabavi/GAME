import json
import os


SAVE_DIR = os.path.dirname(os.path.abspath(__file__))

SAVE_FILE = os.path.join(SAVE_DIR, "user_data.json")


def save_player(email, name, avatar, flag):

    try:

        os.makedirs(SAVE_DIR, exist_ok=True)

        data = {
            "email": email,
            "name": name,
            "avatar": avatar,
            "flag": flag
        }

        with open(
            SAVE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        return True

    except Exception as e:

        # print("Save Error:", e)

        return False


def load_player():

    # print("LOAD PATH:", SAVE_FILE)
    # print("EXISTS:", os.path.exists(SAVE_FILE))

    if not os.path.exists(SAVE_FILE):
        return None

    try:

        with open(
            SAVE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        # print("DATA LOADED:", data)

        return data

    except Exception as e:

        # print("Load Error:", e)

        return None