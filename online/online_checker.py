import subprocess
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIME_JS = os.path.join(BASE_DIR, "time.js")


def check_online_and_run():

    result = os.system(
        "ping -c 1 -W 1000 8.8.8.8 > /dev/null 2>&1"
    )

    if result == 0:

        print("🌐 Online")

        subprocess.run(
            ["node", TIME_JS],
            check=False
        )

        return True

    return False