import serial
import time
import json

SERIAL_PORT = "/dev/ttyUSB0"
BAUDRATE = 115200

HTML_PATH = "/var/www/html/index.html"
JSON_PATH = "/var/www/html/data.json"

last_times = []

race_running = False
start_timestamp = 0
live_time = ""


def format_time(ms):
    try:
        ms = int(ms)

        minutes = ms // 60000
        seconds = (ms % 60000) // 1000
        millis = ms % 1000

        return f"{minutes:02d}:{seconds:02d}:{millis:03d}"

    except:
        return None


def write_html():

    html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Race Timing</title>

<style>

html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;

    background-color: black;
    color: white;

    font-family: Arial, sans-serif;
}

body {
    display: flex;
    flex-direction: column;
    align-items: center;
}

h1 {
    font-size: 4vw;
    margin-top: 1vh;
    margin-bottom: 2vh;
}

#live {

    color: red;

    font-weight: bold;

    font-size: 18vw;

    line-height: 1;

    margin-top: 2vh;
    margin-bottom: 4vh;

    white-space: nowrap;
}

#times {

    width: 100%;

    display: flex;
    flex-direction: column;
    align-items: center;
}

.time {

    font-size: 8vw;

    line-height: 1.1;

    white-space: nowrap;
}

.latest {
    color: red;
}

</style>
</head>

<body>

<h1>Race Timing</h1>

<div id="live"></div>

<div id="times"></div>

<script>

async function updateData() {

    try {

        const response = await fetch("data.json?t=" + Date.now());
        const data = await response.json();

        const liveDiv = document.getElementById("live");
        const timesDiv = document.getElementById("times");

        // show running timer only after start
        if (data.running) {
            liveDiv.innerHTML = data.live_time;
        } else {
            liveDiv.innerHTML = "";
        }

        // rebuild finish list
        timesDiv.innerHTML = "";

        data.last_times.forEach((t, index) => {

            const div = document.createElement("div");

            div.className = "time";

            if (index == 0) {
                div.classList.add("latest");
            }

            div.innerHTML = t;

            timesDiv.appendChild(div);
        });

    } catch (e) {
        console.log(e);
    }
}

setInterval(updateData, 50);

updateData();

</script>

</body>
</html>
"""

    with open(HTML_PATH, "w") as f:
        f.write(html)


def write_json():
    data = {
        "running": race_running,
        "live_time": live_time,
        "last_times": list(reversed(last_times))
    }

    with open(JSON_PATH, "w") as f:
        json.dump(data, f)


def main():

    global race_running
    global start_timestamp
    global live_time
    global last_times

    write_html()

    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)

    time.sleep(2)

    while True:

        # receive serial data
        if ser.in_waiting:

            line = ser.readline().decode("utf-8").strip()

            # START
            if line.lower() == "start":

                race_running = True

                start_timestamp = int(time.time() * 1000)

            # FINISH TIME
            elif line.startswith("Time:"):

                raw_value = line.split("Time:")[1]

                formatted = format_time(raw_value)

                if formatted:

                    race_running = False

                    live_time = formatted

                    last_times.append(formatted)

                    last_times = last_times[-10:]

        # update live timer
        if race_running:

            current_ms = int(time.time() * 1000) - start_timestamp

            live_time = format_time(current_ms)

        # update webpage data
        write_json()

        time.sleep(0.03)


if __name__ == "__main__":
    main()
