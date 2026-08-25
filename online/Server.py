import socket
import threading
import json


HOST = "0.0.0.0"
PORT = 5555


# بازیکن های آنلاین (موقت)
online_players = []


def handle_client(conn, address):

    print("Connected:", address)


    try:

        # دریافت اطلاعات بازیکن
        data = conn.recv(4096).decode()

        player = json.loads(data)


        online_players.append({
            "name": player["name"],
            "country": player["country"],
            "profile": player["profile"],
            "connection": conn
        })


        print("\n--- New Player ---")
        print("Name:", player["name"])
        print("Country:", player["country"])
        print("Profile:", player["profile"])
        print("------------------")


        conn.send(
            "CONNECTED".encode()
        )


        # نگه داشتن اتصال
        while True:

            message = conn.recv(1024)


            if not message:
                break


    except Exception as e:

        print("Error:", e)



    finally:

        # حذف بازیکن هنگام خروج

        for p in online_players:

            if p["connection"] == conn:
                online_players.remove(p)
                break


        print(
            "Disconnected:",
            address
        )


        conn.close()



server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


server.bind(
    (HOST, PORT)
)


server.listen()


print("Server started...")


while True:

    conn, address = server.accept()


    thread = threading.Thread(
        target=handle_client,
        args=(conn,address)
    )


    thread.start()