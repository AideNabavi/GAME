const fs = require("fs");
const path = require("path");

// ==========================================
// SETTINGS
// ==========================================

const TIME_FILE =
    path.join(__dirname, "time.json");

const REQUEST_TIMEOUT = 5000;


// ==========================================
// FETCH WITH TIMEOUT
// ==========================================

async function fetchWithTimeout(
    url,
    timeout = REQUEST_TIMEOUT
) {

    const controller =
        new AbortController();

    const timeoutId =
        setTimeout(() => {
            controller.abort();
        }, timeout);

    try {

        const response =
            await fetch(url, {
                signal: controller.signal
            });

        if (!response.ok) {
            throw new Error(
                `HTTP ${response.status}`
            );
        }

        return response;

    } catch (error) {

        if (error.name === "AbortError") {
            throw new Error("TIMEOUT");
        }

        throw error;

    } finally {

        clearTimeout(timeoutId);

    }
}


// ==========================================
// API 1
// TIME.NOW - IP BASED
// ==========================================

async function getTimeFromTimeNow() {

    const API =
        "https://time.now/developer/api/ip";

    const response =
        await fetchWithTimeout(API);

    const data =
        await response.json();

    if (!data.datetime) {
        throw new Error("INVALID_RESPONSE");
    }

    const date =
        new Date(data.datetime);

    if (isNaN(date.getTime())) {
        throw new Error("INVALID_DATE");
    }

    return {

        time:
            `${String(
                date.getHours()
            ).padStart(2, "0")}:${String(
                date.getMinutes()
            ).padStart(2, "0")}:${String(
                date.getSeconds()
            ).padStart(2, "0")}`,

        weekday:
            date.toLocaleDateString(
                "en-US",
                {
                    weekday: "long"
                }
            ),

        day:
            date.getDate(),

        month:
            date.toLocaleDateString(
                "en-US",
                {
                    month: "long"
                }
            ),

        year:
            date.getFullYear(),

        date:
            `${date.getFullYear()}-${String(
                date.getMonth() + 1
            ).padStart(2, "0")}-${String(
                date.getDate()
            ).padStart(2, "0")}`,

        timezone:
            data.timezone || null,

        isDailyWorkout:
            date.getHours() === 7,

        unix:
            data.unixtime ||
            Math.floor(
                date.getTime() / 1000
            ),

        ip:
            data.client_ip || null,

        source:
            "Time.Now IP"

    };
}


// ==========================================
// API 2
// WORLDTIMEAPI - IP BASED
// ==========================================

async function getTimeFromWorldTimeAPI() {

    const API =
        "https://worldtimeapi.org/api/ip";

    const response =
        await fetchWithTimeout(API);

    const data =
        await response.json();

    if (!data.datetime) {
        throw new Error("INVALID_RESPONSE");
    }

    const date =
        new Date(data.datetime);

    if (isNaN(date.getTime())) {
        throw new Error("INVALID_DATE");
    }

    return {

        time:
            `${String(
                date.getHours()
            ).padStart(2, "0")}:${String(
                date.getMinutes()
            ).padStart(2, "0")}:${String(
                date.getSeconds()
            ).padStart(2, "0")}`,

        weekday:
            date.toLocaleDateString(
                "en-US",
                {
                    weekday: "long"
                }
            ),

        day:
            date.getDate(),

        month:
            date.toLocaleDateString(
                "en-US",
                {
                    month: "long"
                }
            ),

        year:
            date.getFullYear(),

        date:
            `${date.getFullYear()}-${String(
                date.getMonth() + 1
            ).padStart(2, "0")}-${String(
                date.getDate()
            ).padStart(2, "0")}`,

        timezone:
            data.timezone || null,

        isDailyWorkout:
            date.getHours() === 7,

        unix:
            data.unixtime ||
            Math.floor(
                date.getTime() / 1000
            ),

        ip:
            null,

        source:
            "WorldTimeAPI IP"

    };
}


// ==========================================
// API 3
// TIMEAPI - TEHRAN
// ==========================================

async function getTimeFromTehran() {

    const API =
        "https://timeapi.io/api/time/current/zone?timeZone=Asia/Tehran";

    const response =
        await fetchWithTimeout(API);

    const data =
        await response.json();

    if (!data.dateTime) {
        throw new Error("INVALID_RESPONSE");
    }

    const date =
        new Date(data.dateTime);

    if (isNaN(date.getTime())) {
        throw new Error("INVALID_DATE");
    }

    const hour =
        Number(data.hour);

    const minute =
        Number(data.minute);

    const second =
        Number(data.seconds);

    const day =
        Number(data.day);

    const monthNumber =
        Number(data.month);

    const year =
        Number(data.year);

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

    return {

        time:
            `${String(hour).padStart(2, "0")}:${String(
                minute
            ).padStart(2, "0")}:${String(
                second
            ).padStart(2, "0")}`,

        weekday:
            data.dayOfWeek,

        day:
            day,

        month:
            monthName,

        year:
            year,

        date:
            `${year}-${String(
                monthNumber
            ).padStart(2, "0")}-${String(
                day
            ).padStart(2, "0")}`,

        timezone:
            "Asia/Tehran",

        isDailyWorkout:
            hour === 7,

        unix:
            Math.floor(
                date.getTime() / 1000
            ),

        ip:
            null,

        source:
            "TimeAPI Tehran"

    };
}


// ==========================================
// LAST SAVED TIME
// ==========================================

function getLastSavedTime() {

    try {

        if (!fs.existsSync(TIME_FILE)) {
            return null;
        }

        const raw =
            fs.readFileSync(
                TIME_FILE,
                "utf8"
            );

        const data =
            JSON.parse(raw);

        if (
            data &&
            data.success === true &&
            data.unix
        ) {

            return data;

        }

    } catch (error) {

        console.error(
            "Could not read previous time."
        );

    }

    return null;
}


// ==========================================
// GET DAILY TIME
// ==========================================

async function getDailyTime() {

    // ======================================
    // API 1
    // ======================================

    try {

        return {
            success: true,
            online: true,
            data:
                await getTimeFromTimeNow()
        };

    } catch (error) {

        console.error(
            "API 1 failed:",
            error.message
        );

    }


    // ======================================
    // API 2
    // ======================================

    try {

        return {
            success: true,
            online: true,
            data:
                await getTimeFromWorldTimeAPI()
        };

    } catch (error) {

        console.error(
            "API 2 failed:",
            error.message
        );

    }


    // ======================================
    // API 3
    // ======================================

    try {

        return {
            success: true,
            online: true,
            data:
                await getTimeFromTehran()
        };

    } catch (error) {

        console.error(
            "API 3 failed:",
            error.message
        );

    }


    // ======================================
    // ALL APIs FAILED
    // ======================================

    const lastTime =
        getLastSavedTime();

    return {

        success:
            lastTime !== null,

        online:
            false,

        data:
            lastTime

    };
}


// ==========================================
// RUN
// ==========================================

getDailyTime().then(result => {

    // ======================================
    // PRINT FULL INFORMATION
    // ======================================

    console.error(
        "================================"
    );

    console.error(
        "ONLINE TIME:",
        result.online
    );

    if (result.data) {

        console.error(
            "Time:",
            result.data.time
        );

        console.error(
            "Date:",
            result.data.date
        );

        console.error(
            "Timezone:",
            result.data.timezone
        );

        console.error(
            "Unix:",
            result.data.unix
        );

        console.error(
            "Source:",
            result.data.source
        );

        console.error(
            "IP:",
            result.data.ip
        );

        console.error(
            "Weekday:",
            result.data.weekday
        );

        console.error(
            "Day:",
            result.data.day
        );

        console.error(
            "Month:",
            result.data.month
        );

        console.error(
            "Year:",
            result.data.year
        );

        console.error(
            "Daily Workout:",
            result.data.isDailyWorkout
        );



    }

    console.error(
        "================================"
    );


    // ======================================
    // SAVE TIME.JSON
    // ======================================

    if (
        result.data &&
        result.data.unix
    ) {

        fs.writeFileSync(

            TIME_FILE,

            JSON.stringify(
                {
                    success: true,
                    ...result.data
                },
                null,
                4
            )

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

    }


    // ======================================
    // IMPORTANT:
    // STDOUT = ONLY TRUE / FALSE
    // ======================================

    console.log(
        result.online
    );

});















