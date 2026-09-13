#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <limits.h>
#include <string.h>
#include <libnotify/notify.h>

/*

اول
sudo apt update
sudo apt install gcc pkg-config libnotify-dev



gcc DailyReminder.c \
    -o DailyReminder \
    $(pkg-config --cflags --libs libnotify)





*/

// ============================================================
// GAME PATH
// ============================================================

void get_game_path(
    char *game_path,
    size_t size
)
{
    char exe_path[PATH_MAX];

    ssize_t length = readlink(
        "/proc/self/exe",
        exe_path,
        sizeof(exe_path) - 1
    );

    if (length == -1)
    {
        snprintf(
            game_path,
            size,
            "./MentalMathChallenge"
        );

        return;
    }

    exe_path[length] = '\0';


    // --------------------------------------------------------
    // FIND LAST /
    // --------------------------------------------------------

    char *last_slash = strrchr(
        exe_path,
        '/'
    );


    // --------------------------------------------------------
    // GET DIRECTORY
    // --------------------------------------------------------

    if (last_slash != NULL)
    {
        *last_slash = '\0';
    }


    // --------------------------------------------------------
    // CREATE GAME PATH
    // --------------------------------------------------------

    snprintf(
        game_path,
        size,
        "%s/MentalMathChallenge",
        exe_path
    );
}


// ============================================================
// START GAME
// ============================================================

void start_game()
{
    char game_path[PATH_MAX];


    get_game_path(
        game_path,
        sizeof(game_path)
    );


    // --------------------------------------------------------
    // CHECK GAME
    // --------------------------------------------------------

    if (access(game_path, X_OK) != 0)
    {
        fprintf(
            stderr,
            "Game executable not found:\n%s\n",
            game_path
        );

        return;
    }


    // --------------------------------------------------------
    // START GAME
    // --------------------------------------------------------

    pid_t pid = fork();


    if (pid == 0)
    {
        execl(
            game_path,
            game_path,
            (char *)NULL
        );


        // If execl fails
        perror(
            "Could not start game"
        );

        exit(1);
    }


    if (pid > 0)
    {
        printf(
            "Game started.\n"
        );

        return;
    }


    perror(
        "fork failed"
    );
}


// ============================================================
// NOTIFICATION CALLBACK
// ============================================================

void notification_action(
    NotifyNotification *notification,
    char *action,
    gpointer user_data
)
{
    (void)notification;
    (void)user_data;


    // --------------------------------------------------------
    // START WORKOUT
    // --------------------------------------------------------

    if (
        strcmp(
            action,
            "start"
        ) == 0
    )
    {
        start_game();
    }


    // --------------------------------------------------------
    // MAYBE
    // --------------------------------------------------------

    else if (
        strcmp(
            action,
            "maybe"
        ) == 0
    )
    {
        printf(
            "Workout postponed.\n"
        );
    }
}


// ============================================================
// SHOW NOTIFICATION
// ============================================================

void show_notification()
{
    NotifyNotification *notification;


    // --------------------------------------------------------
    // INITIALIZE LIBNOTIFY
    // --------------------------------------------------------

    notify_init(
        "Mental Math Challenge"
    );


    // --------------------------------------------------------
    // CREATE NOTIFICATION
    // --------------------------------------------------------

    notification = notify_notification_new(
        "DAILY WORKOUT",
        "Today's challenges are ready!\n"
        "Complete all 3 games and earn XP.\n\n"
        "⭐ +100 XP",
        NULL
    );


    // --------------------------------------------------------
    // ADD BUTTONS
    // --------------------------------------------------------

    notify_notification_add_action(
        notification,
        "start",
        "START WORKOUT",
        notification_action,
        NULL,
        NULL
    );


    notify_notification_add_action(
        notification,
        "maybe",
        "MAYBE",
        notification_action,
        NULL,
        NULL
    );


    // --------------------------------------------------------
    // SHOW
    // --------------------------------------------------------

    GError *error = NULL;


    if (
        !notify_notification_show(
            notification,
            &error
        )
    )
    {
        fprintf(
            stderr,
            "Notification error: %s\n",
            error->message
        );

        g_error_free(error);
    }
    else
    {
        printf(
            "Notification sent.\n"
        );
    }


    // --------------------------------------------------------
    // KEEP PROGRAM ALIVE
    // --------------------------------------------------------

    GMainLoop *loop = g_main_loop_new(
        NULL,
        FALSE
    );


    g_main_loop_run(
        loop
    );


    // --------------------------------------------------------
    // CLEANUP
    // --------------------------------------------------------

    g_main_loop_unref(
        loop
    );

    g_object_unref(
        notification
    );

    notify_uninit();
}


// ============================================================
// MAIN
// ============================================================

int main()
{
    show_notification();

    return 0;
}