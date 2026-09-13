#!/bin/bash

GAME_DIR="/opt/mental-math-challenge"

SERVICE_DIR="/etc/systemd/system"

cat > "$SERVICE_DIR/mental-math-daily.service" <<EOF
[Unit]
Description=Mental Math Challenge Daily Workout

[Service]
Type=oneshot
ExecStart=$GAME_DIR/DailyReminder
EOF


cat > "$SERVICE_DIR/mental-math-daily.timer" <<EOF
[Unit]
Description=Mental Math Challenge Daily Workout Timer

[Timer]
OnCalendar=*-*-* 07:00:00
Persistent=true

[Install]
WantedBy=timers.target
EOF


chmod +x "$GAME_DIR/MentalMathChallenge"
chmod +x "$GAME_DIR/DailyReminder"


systemctl daemon-reload

systemctl enable mental-math-daily.timer

systemctl start mental-math-daily.timer


exit 0