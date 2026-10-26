import Foundation
import UserNotifications
import AppKit



// این برای کامپایل کردن  این زبان است  
// swiftc DailyReminder.swift -o DailyReminder
/*
killall DailyReminder 
open DailyReminder.app 
 pgrep -fl DailyReminders
killall DailyReminder 2>/dev/null






swiftc DailyReminder.swift -o DailyReminder
cp DailyReminder DailyReminder.app/Contents/MacOS/DailyReminder
codesign --force --deep --sign - DailyReminder.app
open DailyReminder.app
*/
// ==========================================
// GAME PATH
// ==========================================

let gamePath = "/Users/aiden/Desktop/app/app.py"
// let gamePath = "a.app"


// ==========================================
// NOTIFICATION DELEGATE
// ==========================================

class NotificationDelegate: NSObject,
                            NSApplicationDelegate,
                            UNUserNotificationCenterDelegate {

    // ==========================================
    // APP START
    // ==========================================
    func applicationDidFinishLaunching(_ notification: Notification) {

        print("🚀 DailyReminder started")

        let center = UNUserNotificationCenter.current()
        center.delegate = self

        center.getNotificationSettings { settings in

            print("================================")
            print("🔐 Authorization:",
                settings.authorizationStatus.rawValue)

            print("🔔 Alert:",
                settings.alertSetting.rawValue)

            print("🔊 Sound:",
                settings.soundSetting.rawValue)

            print("================================")

            if settings.authorizationStatus == .authorized {

                print("✅ Notification permission is already allowed")

                self.createNotification()

            } else {

                print("⚠️ Notification permission is NOT authorized")

                center.requestAuthorization(
                    options: [.alert, .sound]
                ) { granted, error in

                    if let error = error {
                        print("❌ Permission error:", error)
                        return
                    }

                    print("🔔 Permission result:", granted)

                    if granted {
                        self.createNotification()
                    }
                }
            }
        }
    }


    // ==========================================
    // SHOW NOTIFICATION WHILE APP IS RUNNING
    // ==========================================

    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler:
        @escaping (UNNotificationPresentationOptions) -> Void
    ) {

        completionHandler([.alert, .sound])
    }


    // ==========================================
    // WHEN USER CLICKS NOTIFICATION
    // ==========================================

    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        didReceive response: UNNotificationResponse,
        withCompletionHandler completionHandler:
        @escaping () -> Void
    ) {

        if response.actionIdentifier == "PLAY_NOW" ||
           response.actionIdentifier == UNNotificationDefaultActionIdentifier {

            launchGame()
        }

        completionHandler()
    }


    // ==========================================
    // CREATE NOTIFICATION
    // ==========================================

    func createNotification() {

        let center = UNUserNotificationCenter.current()

        // پاک کردن Notificationهای قبلی
        center.removeAllPendingNotificationRequests()


        // --------------------------------------
        // PLAY NOW BUTTON
        // --------------------------------------

        let playAction = UNNotificationAction(
            identifier: "PLAY_NOW",
            title: "PLAY NOW",
            options: []
        )


        // --------------------------------------
        // NOTIFICATION CATEGORY
        // --------------------------------------

        let category = UNNotificationCategory(
            identifier: "DAILY_GAME",
            actions: [playAction],
            intentIdentifiers: [],
            options: []
        )

        center.setNotificationCategories([category])


        // --------------------------------------
        // NOTIFICATION CONTENT
        // --------------------------------------

        let content = UNMutableNotificationContent()

        content.title = "🎮 Daily Game"
        content.subtitle = "Mental Math Challenge"
        content.body = "Your daily challenge is ready!"
        content.sound = .default
        content.categoryIdentifier = "DAILY_GAME"


        // --------------------------------------
        // TEST: 10 SECONDS
        // --------------------------------------

        let trigger = UNTimeIntervalNotificationTrigger(
            timeInterval: 1,
            repeats: false
        )


        // --------------------------------------
        // REQUEST
        // --------------------------------------

        let request = UNNotificationRequest(
            identifier: "DAILY_GAME_NOTIFICATION",
            content: content,
            trigger: trigger
        )


        // --------------------------------------
        // ADD REQUEST
        // --------------------------------------

        center.add(request) { error in

            if let error = error {

                print("❌ Failed:", error)

            } else {

                print("✅ Notification scheduled!")
                print("⏱️ It should appear in 10 seconds.")

                // بررسی اینکه واقعاً Pending شده
                center.getPendingNotificationRequests { requests in

                    print(
                        "📋 Pending notifications:",
                        requests.count
                    )

                    for request in requests {
                        print(
                            "➡️",
                            request.identifier
                        )
                    }
                }
            }
        }
    }


    // ==========================================
    // LAUNCH GAME
    // ==========================================

// این تابع بع برای اجرا بازی و فایل اگزه است 
//     func launchGame() {

//         let url = URL(fileURLWithPath: gamePath)

//         NSWorkspace.shared.open(url)
//     }
// }


    func launchGame() {

        let process = Process()

        process.executableURL = URL(
            fileURLWithPath: "/usr/local/bin/python3"
        )

        process.arguments = [
            "/Users/mac/Desktop/app/app.py"
        ]

        process.currentDirectoryURL = URL(
            fileURLWithPath: "/Users/mac/Desktop/app"
        )

        do {
            try process.run()
            print("🎮 Game launched!")
            print("PID:", process.processIdentifier)
        } catch {
            print("❌ Failed to launch Python:")
            print(error)
        }
    }
}
// ==========================================
// MAIN
// ==========================================

let app = NSApplication.shared

let delegate = NotificationDelegate()

app.delegate = delegate

app.setActivationPolicy(.accessory)

app.run()
