    
import subprocess
import os


def check_online():

    result = os.system(
        "ping -c 1 -W 1000 8.8.8.8 > /dev/null 2>&1"
    )

    return result == 0



# import os
# import subprocess


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# TIME_JS = os.path.join(BASE_DIR, "time.js")


# def get_online_status():
#     result = subprocess.run(
#         ["node", TIME_JS],
#         capture_output=True,
#         text=True,
#         check=False
#     )

#     return result.stdout.strip().lower() == "true"










    


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIME_JS = os.path.join(BASE_DIR, "time.js")

def run_online_time():
    if check_online():
        subprocess.run(["node", TIME_JS], check=False)
        return True

    return False


run_online_time()














import subprocess

result = subprocess.run(
    ["node", "online_checker.js"],
    capture_output=True,
    text=True
)

online = result.stdout.strip() == "true"

print("ONLINE:", online)