import logging
import os

def dir_check():
    """
    Überprüfe, ob das Verzeichnis existiert, und estelle es, wenn nicht.
    :return: True sau Fehler - der Status des Verzeichnisses
    """
    dir_log = 'Cost_of_Living/Log'
    try:
        if not os.path.exists(dir_log):  # Überprüfen, ob das Verzeichnis existiert.
            os.makedirs(dir_log, mode=0o777)  # Erstelle ein Verzeichnis mit den Rechten 777
    except Exception as e:
        return f"Fehler {e}"

    return dir_log

def setup_logger(name: str):
    """
    Erstellt und konfiguriert einen Logger mit einem bestimmten Namen.

    Der Logger protokolliert Meldungen sowohl in die Konsole als auch
    in eine `.log`-Datei mit dem gleichen Namen wie das Argument `name`.
    Das Format der Log-Nachrichten enthält einen Zeitstempel, den
    Log-Level und die Nachricht. Falls der Logger bereits Handler hat,
    werden keine weiteren hinzugefügt, um doppelte Ausgaben zu vermeiden.

    Parameter:
        name (str): Der Name des Loggers und der Logdatei.

    Rückgabe:
        logging.Logger: Die konfigurierte Logger-Instanz.
    """

    dir_log = dir_check()
    if not dir_log:
        return "Fehler bei der Überprüfung/Erstellung des Verzeichnisses"

    logger = logging.getLogger(name)  # Holt einen Logger mit dem angegebenen Namen
    logger.setLevel(logging.INFO)  # Setzt das Log-Level auf INFO (und schwerwiegender)

    # Prüft, ob der Logger bereits Handler hat, um Duplikate zu vermeiden
    if not logger.hasHandlers():
        consol_handler = logging.StreamHandler()  # Handler für die Konsolenausgabe
        file_handler = logging.FileHandler(f"{dir_log}/{name}.log") # Handler für das Schreiben in eine Datei

        # Definiert das Format der Log-Nachrichten
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        consol_handler.setFormatter(formatter)  # Setzt das Format für die Konsole
        file_handler.setFormatter(formatter)  # Setzt das Format für die Datei

        # Fügt die Handler dem Logger hinzu
        logger.addHandler(file_handler)
        logger.addHandler(consol_handler)

    logger.propagate = False  # Verhindert das Weitergeben von Logs an übergeordnete Logger
    return logger  # Gibt den konfigurierten Logger zurück
