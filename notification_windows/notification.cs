using System;
using System.Diagnostics;
using System.IO;
using CommunityToolkit.WinUI.Notifications;


// ============================================================
// GAME PATH
// ============================================================

string gamePath = Path.Combine(
    AppContext.BaseDirectory,
    "MentalMathChallenge.exe"
);


// ============================================================
// MAIN
// ============================================================

if (args.Length > 0 &&
    args[0].Equals(
        "start",
        StringComparison.OrdinalIgnoreCase
    ))
{
    StartGame();
}
else
{
    ShowNotification();
}


// ============================================================
// SHOW NOTIFICATION
// ============================================================

void ShowNotification()
{
    try
    {
        new ToastContentBuilder()

            .AddText(
                "DAILY WORKOUT"
            )

            .AddText(
                "Today's challenges are ready!"
            )

            .AddText(
                "Complete all 3 games and earn XP."
            )

            .AddText(
                "⭐ +100 XP"
            )

            .AddButton(
                new ToastButton()
                    .SetContent(
                        "START WORKOUT"
                    )
                    .AddArgument(
                        "action",
                        "start"
                    )
            )

            .AddButton(
                new ToastButton()
                    .SetContent(
                        "MAYBE"
                    )
                    .AddArgument(
                        "action",
                        "maybe"
                    )
            )

            .Show();

        Console.WriteLine(
            "Notification sent."
        );
    }
    catch (Exception ex)
    {
        Console.WriteLine(
            "Notification error:"
        );

        Console.WriteLine(
            ex.Message
        );
    }
}


// ============================================================
// START GAME
// ============================================================

void StartGame()
{
    Console.WriteLine(
        "Starting game..."
    );


    // --------------------------------------------------------
    // CHECK GAME
    // --------------------------------------------------------

    if (!File.Exists(gamePath))
    {
        Console.WriteLine(
            "Game executable not found:"
        );

        Console.WriteLine(
            gamePath
        );

        return;
    }


    // --------------------------------------------------------
    // START GAME
    // --------------------------------------------------------

    try
    {
        Process.Start(
            new ProcessStartInfo
            {
                FileName = gamePath,
                WorkingDirectory =
                    AppContext.BaseDirectory,
                UseShellExecute = true
            }
        );

        Console.WriteLine(
            "Game started."
        );
    }
    catch (Exception ex)
    {
        Console.WriteLine(
            "Could not start game:"
        );

        Console.WriteLine(
            ex.Message
        );
    }
}