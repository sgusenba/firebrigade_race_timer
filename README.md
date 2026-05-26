# Fire Brigade Race Timer / Feuerwehr Wettkampf-Zeitmessung

---

# English

## Overview

This project is a wireless race timing system built for local fire brigade competitions and training events.

The system consists of:

* 2x ESP32 LoRa V3 boards
* Buzzers connected to the ESP32 devices
* A Raspberry Pi running the timing and web server software
* A WiFi access point connected to the Raspberry Pi for improved wireless reception and easier access

The project was originally developed for the local fire brigade in my hometown.

The Raspberry Pi provides a web interface that displays the timing results live in a browser.

---

## Features

* Wireless start and finish timing
* LoRa communication between ESP32 devices
* Live timing display via web browser
* Automatic race timer updates
* Large and easy-to-read timing display
* Simple setup for competitions and training

---

## System Architecture

### Hardware

#### Starter Unit

* ESP32 LoRa V3
* Connected start button
* Sends start signal wirelessly

#### Finisher Unit

* ESP32 LoRa V3
* Connected finish button
* Sends finish signal and measured time wirelessly

#### Server Unit

* Raspberry Pi
* Runs Python timing software
* Hosts local web server
* Connected to WiFi access point

---

## Project Structure

```text
.
├── timer.py            # Main Raspberry Pi timing and web server application
├── starter.ino         # ESP32 starter unit firmware
├── finisher.ino        # ESP32 finisher unit firmware
└── README.md           # Project documentation
```

---

## Requirements

### Raspberry Pi

* Raspberry Pi OS
* Python 3
* WiFi connection or local access point

### Python Dependencies

Example packages that may be required:

```bash
pip install flask pyserial
```

Additional packages may be required depending on the current implementation.

---

## ESP32 Requirements

### Hardware

* 2x ESP32 LoRa V3 boards
* Buzzers
* USB cables
* Power supply or battery

### Software

* Arduino IDE
* ESP32 board support package
* Required LoRa libraries

---

## Installation

### 1. Flash the ESP32 Devices

Upload:

* `starter.ino` to the starter ESP32
* `finisher.ino` to the finisher ESP32

using the Arduino IDE.

---

### 2. Prepare the Raspberry Pi

Clone the repository:

```bash
git clone https://github.com/sgusenba/firebrigade_race_timer.git
cd firebrigade_race_timer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or install the required packages manually.

---

### 3. Start the Timer Application

Run:

```bash
python3 timer.py
```

The web interface will then be available in the browser.

---

## Usage

1. Power on both ESP32 devices
2. Start the Raspberry Pi application
3. Open the web interface in a browser
4. Trigger the starter unit
5. The timer starts automatically
6. Trigger the finisher unit
7. The final race time is displayed live


---
# Deutsch

## Übersicht

Dieses Projekt ist ein drahtloses Zeitmesssystem für Feuerwehrbewerbe und Trainingsveranstaltungen.

Das System besteht aus:

* 2x ESP32 LoRa V3 Boards
* Buzzern an den ESP32 Geräten
* Einem Raspberry Pi als Zeitmess- und Webserver
* Einem WLAN Access Point am Raspberry Pi für bessere Funkverbindung und einfacheren Zugriff

Das Projekt wurde hauptsächlich für die örtliche Feuerwehr meines Heimatortes entwickelt.

Der Raspberry Pi stellt eine Weboberfläche bereit, auf der die Zeiten live im Browser angezeigt werden.

---

## Funktionen

* Drahtlose Start- und Zielerkennung
* LoRa-Kommunikation zwischen ESP32 Geräten (Start und Ziel)
* Live-Anzeige der Zeit im Webbrowser
* Automatische Aktualisierung der Anzeige
* Große und gut lesbare Zeitanzeige
* Einfache Verwendung bei Bewerben und Trainings


---

## Systemaufbau

### Hardware

#### Start-Einheit

* ESP32 LoRa V3
* Angeschlossener Start-Buzzer
* Sendet das Startsignal drahtlos

#### Ziel-Einheit

* ESP32 LoRa V3
* Angeschlossener Ziel-Buzzer
* ist via serial am Raspberry Pi angeschlosse

#### Server-Einheit

* Raspberry Pi
* Führt die Python-Zeitmesssoftware aus
* Betreibt den lokalen Webserver
* Verbunden mit einem WLAN Access Point

---

## Projektstruktur

```text
.
├── timer.py            # Hauptanwendung für Zeitmessung und Webserver am Raspberry Pi
├── starter.ino         # Firmware für die Start-Einheit
├── finisher.ino        # Firmware für die Ziel-Einheit
└── README.md           # Projektdokumentation
```

---

## Voraussetzungen

### Raspberry Pi

* Raspberry Pi OS
* Python 3
* WLAN-Verbindung oder lokaler Access Point

### Python-Abhängigkeiten

benötigte Pakete:

```bash
pip install flask pyserial
```

Je nach aktueller Implementierung können weitere Pakete notwendig sein.

---

## Anforderungen für die ESP32 Geräte

### Hardware

* 2x ESP32 LoRa V3 Boards
* Buzzer
* USB-Kabel
* Netzteil oder Akkus

### Software

* Arduino IDE
* ESP32 Board Support Package
* Benötigte LoRa-Bibliotheken

---

## Installation

### 1. ESP32 Geräte flashen

Lade folgende Dateien mit der Arduino IDE hoch:

* `starter.ino` auf die Start-Einheit
* `finisher.ino` auf die Ziel-Einheit

---

### 2. Raspberry Pi vorbereiten

Repository clonen:

```bash
git clone https://github.com/sgusenba/firebrigade_race_timer.git
cd firebrigade_race_timer
```

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

oder die benötigten Pakete manuell installieren.

---

### 3. Timer-Anwendung starten

Starten mit:

```bash
python3 timer.py
```

Danach ist die Weboberfläche im Browser erreichbar.

---

## Verwendung

1. Beide ESP32 Geräte einschalten
2. Raspberry Pi Anwendung starten
3. Weboberfläche im Browser öffnen
4. Start-Einheit auslösen
5. Die Zeitmessung startet automatisch
6. Ziel-Einheit auslösen
7. Die Endzeit wird live angezeigt

--
