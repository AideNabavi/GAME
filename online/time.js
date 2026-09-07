async function fetchWithTimeout(url, timeout = 5000) {

    const controller = new AbortController();

    const timeoutId = setTimeout(() => {
        controller.abort();
    }, timeout);

    try {

        const response = await fetch(url, {
            signal: controller.signal
        });

        clearTimeout(timeoutId);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        return response;

    } catch (error) {

        clearTimeout(timeoutId);

        if (error.name === "AbortError") {
            throw new Error("TIMEOUT");
        }

        throw error;
    }
}


// ==========================================
// GET DAILY TIME
// ==========================================

async function getDailyTime() {

    const timezone =
        Intl.DateTimeFormat().resolvedOptions().timeZone;


    // ==========================================
    // API 1
    // Time.Now - IP Based
    // ==========================================

    try {

        console.log("Trying API 1...");

        const response = await fetchWithTimeout(
            "https://time.now/developer/api/ip",
            5000
        );

        const data = await response.json();

        const date = new Date(data.datetime);

        const hour = date.getHours();
        const minute = date.getMinutes();

        return {

            time:
                `${String(hour).padStart(2, "0")}:${String(minute).padStart(2, "0")}`,

            weekday:
                date.toLocaleDateString("en-US", {
                    weekday: "long"
                }),

            day:
                date.getDate(),

            month:
                date.toLocaleDateString("en-US", {
                    month: "long"
                }),

            year:
                date.getFullYear(),

            date:
                `${date.getFullYear()}-${String(
                    date.getMonth() + 1
                ).padStart(2, "0")}-${String(
                    date.getDate()
                ).padStart(2, "0")}`,

            timezone:
                data.timezone || timezone,

            isDailyWorkout:
                hour === 7,

            unix:
                data.unixtime ||
                Math.floor(date.getTime() / 1000),

            ip:
                data.client_ip || null,

            source:
                "Time.Now API"

        };

    } catch (error) {

        console.log(
            `API 1 failed: ${error.message}`
        );

        console.log(
            "Trying API 2..."
        );
    }


    // ==========================================
    // API 2
    // UTC Time API
    // ==========================================

    try {

        console.log("Trying API 2...");

        const response = await fetchWithTimeout(
            "https://utctime.app/api/now",
            5000
        );

        const data = await response.json();

        const utcDate =
            new Date(data.utc_datetime);


        // ======================================
        // Convert UTC → User Timezone
        // ======================================

        const parts =
            new Intl.DateTimeFormat("en-US", {

                timeZone: timezone,

                year: "numeric",
                month: "2-digit",
                day: "2-digit",

                weekday: "long",

                hour: "2-digit",
                minute: "2-digit",

                hour12: false

            }).formatToParts(utcDate);


        const getPart = (type) => {

            return parts.find(
                part => part.type === type
            )?.value;

        };


        const hour =
            Number(getPart("hour"));

        const minute =
            Number(getPart("minute"));

        const day =
            Number(getPart("day"));

        const monthNumber =
            Number(getPart("month"));

        const year =
            Number(getPart("year"));

        const weekday =
            getPart("weekday");


        // ======================================
        // Month Name
        // ======================================

        const monthName =
            new Date(
                year,
                monthNumber - 1,
                day
            ).toLocaleDateString(
                "en-US",
                {
                    month: "long"
                }
            );


        // ======================================
        // Return
        // ======================================

        return {

            time:
                `${String(hour).padStart(2, "0")}:${String(minute).padStart(2, "0")}`,

            weekday:
                weekday,

            day:
                day,

            month:
                monthName,

            year:
                year,

            date:
                `${year}-${String(monthNumber).padStart(2, "0")}-${String(day).padStart(2, "0")}`,

            timezone:
                timezone,

            isDailyWorkout:
                hour === 7,

            unix:
                Math.floor(utcDate.getTime() / 1000),

            ip:
                null,

            source:
                "UTC Time API"

        };

    } catch (error) {

        console.log(
            `API 2 failed: ${error.message}`
        );

        console.log(
            "All APIs failed."
        );

        return null;
    }
}


// ==========================================
// JSON
// ==========================================

const fs = require("fs");
const path = require("path");
const TIME_FILE = path.join(__dirname, "time.json");

// ==========================================
// RUN
// ==========================================

getDailyTime().then(result => {

    if (result) {

        fs.writeFileSync(
            TIME_FILE,
            JSON.stringify(
                result,
                null,
                4
            )
        );

        console.log(
            "Time saved successfully."
        );

    } else {

        fs.writeFileSync(
            TIME_FILE,
            JSON.stringify(
                {
                    success: false
                },
                null,
                4
            )
        );

        console.log(
            "Could not get online time."
        );
    }

});