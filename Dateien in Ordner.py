import os
import shutil

class FileManage:
    def __init__(self, dir_location="/home/sandor/Downloads"):
        self.dir_location = dir_location

    def dir_read(self):
        """
        Das Verzeichnis wird gelesen
        :return:
        """

        try:
            if os.path.exists(self.dir_location):
                return True
            else:
                return False
        except Exception as e:
            return f"Fehler: {e}"

    def file_search(self):
        """
        Sucht die Dateien im ausgewählten Verzeichnis
        :return:
        """
        dir_valid = self.dir_read()
        if dir_valid is False:
            return "Das Verzeichnis existiert nicht"

        try:
            return [f for f in os.listdir(self.dir_location) if os.path.isfile(os.path.join(self.dir_location, f))]
        except Exception as e:
            return f"Es ist ein Fehler aufgetreten: {e}"

    def file_found(self, ext: list):
        """
        Ordnen der Dateien in Ordner:
        :param ext: list - eine Liste von Strings, um die Dateien im Verzeichnis nach Erweiterung zu filtern/suchen
        :return: list - gibt eine Liste der Dateien mit den gesuchten Erweiterungen zurück
        """
        files_valid = self.file_search()
        if isinstance(files_valid, str):
            return files_valid

        filtred_file = []  # Speichere alle Dateien mit den gesuchten Erweiterungen
        try:
            for i in files_valid:
                _, files = os.path.splitext(i)  # _ ignori das, entpacke das Tuple in zwei Variablen
                file_ext = files[1:].lower()  # Normalisierung auf Kleinbuchstaben

                if file_ext in [ext_item.lower() for ext_item in ext]:  # comparare la litere mici
                    filtred_file.append(i)
            return filtred_file if filtred_file else "Es wurden keine Dateien mit den angegebenen Erweiterungen gefunden."

        except Exception as e:
            return f"Es ist ein Fehler aufgetreten: {e}"

    def file_move(self, ext: list):
        """
        Verschiebe Dateien in Ordner basierend auf ihrer Erweiterung.
        :param ext: list - Liste der gesuchten Erweiterungen
        :return: string - Bestätigungsnachricht
        """

        moved_files = []
        for i in ext:
            file_for_move = self.file_found([i])

            if isinstance(file_for_move, str) or not file_for_move:
                print(f"Es wurden keine Dateien mit der Erweiterung {i} gefunden.")
                continue

            for f in file_for_move:
                dir_from = os.path.join(self.dir_location, f)
                dir_to = os.path.join(self.dir_location, i)
                dir_to_file = os.path.join(dir_to, f)

                print(f"Verschiebe {f} nach {dir_to}")

                os.makedirs(dir_to, exist_ok=True)  # Erstelle das Verzeichnis, wenn es nicht existiert
                shutil.move(dir_from, dir_to_file)  # Verschiebe die Datei in das entsprechende Verzeichnis
                moved_files.append(f)  # Fügen wir die verschobene Datei zur Liste hinzu

        if moved_files:
            return f"Verschobene Dateien: {', '.join(moved_files)}"
        else:
            return "Es wurden keine Dateien verschoben."

    def __str__(self):
        """
        Nachricht mit dem Speicherort des Verzeichnisses
        :return:
        """

        return f"Location of director: {self.dir_location}"


# Erstelle ein Objekt mit dem angegebenen Verzeichnispfad
dirs = FileManage("/home/sandor/Downloads")

# Liste der Dateierweiterungen
s = ["jpg", "jpeg", "txt"]

# Zeige das Ergebnis des Verschiebens der Dateien an
print(dirs.file_move(s))