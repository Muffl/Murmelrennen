Damit du .mp4 speichern kannst, brauchst du FFmpeg auf deinem System.

🔧 Installation unter Windows:
Lade FFmpeg herunter:
https://ffmpeg.org/download.html → Windows → „Windows builds by Gyan.dev“

Entpacke den Ordner (z. B. ffmpeg-...) nach C:\ffmpeg

Füge C:\ffmpeg\bin zu deiner System-PATH-Umgebungsvariable hinzu:

Systemsteuerung → System → Erweiterte Systemeinstellungen → Umgebungsvariablen

„Path“ bearbeiten → C:\ffmpeg\bin hinzufügen

Starte dein Terminal neu und überprüfe mit:


ffmpeg -version

Danach kannst du dein Python-Skript wieder mit folgendem Befehl speichern:




