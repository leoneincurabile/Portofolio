import os
import shutil
import time
from pathlib import Path

class ImgSort:
    def __init__(self, path_jpg='jpg'):
        self.path_jpg = path_jpg

    @staticmethod
    def _verify_dir_exists(path):
        """
        Überprüft, ob das angegebene Verzeichnis existiert und zugänglich ist.

        :param path: Der Pfad zum zu überprüfenden Verzeichnis.
        :return: Gibt das Path-Objekt zurück, wenn das Verzeichnis existiert,
                 None, wenn es nicht existiert oder eine Fehlermeldung,
                 wenn es Berechtigungsprobleme oder andere Fehler gibt.
        """
        try:
            p = Path(path)  # Das Objekt für den Dateipfad wird aufgerufen
            if p.is_dir():  # Es wird überprüft, ob das Objekt ein Verzeichnis ist
                return p
            else:
                return None
        except PermissionError:
            return # Fehler: Unzureichende Berechtigungen, um auf das Verzeichnis zuzugreifen.
        except OSError as e:
            return f"Systemfehler: {str(e)}"
        except Exception as e:
            return f"Unerwarteter Fehler: {str(e)}"

    def _creat_path_jpg(self, path):
        """
        Erstellt einen Ordner für JPG-Dateien, wenn der angegebene Pfad gültig ist und das Verzeichnis noch nicht existiert.

        :param path: Der Pfad, der überprüft wird, um sicherzustellen, dass er gültig ist und existiert.
        :return: Eine Nachricht, die den Status der Ordnererstellung beschreibt (Erfolg, Fehler oder Info).
        """
        valid_path = self._verify_dir_exists(path)  # Ruft die Verzeichnisprüfungsfunktion auf

        if valid_path:
            # Fügt den Pfad zur Pfad hinzu, wo die Bilder gespeichert werden
            full_path_jpg = valid_path / self.path_jpg

            # Überprüft, ob der hinzugefügte Verzeichnispfad bereits existiert
            create_dir_check = full_path_jpg.is_dir()
            if not create_dir_check:

                # Erstelle Verzeichnis für JPG-Dateien
                try:
                    full_path_jpg.mkdir(mode=0o777, exist_ok=True)
                    return "Erfolg: Das Verzeichnis wurde erstellt."
                except PermissionError:
                    return "Fehler: Unzureichende Berechtigungen zum Erstellen des Verzeichnisses."
                except FileNotFoundError:
                    return "Fehler: Das übergeordnete Verzeichnis existiert nicht."
                except OSError as e:
                    return f"Systemfehler: {str(e)}"
                except Exception as e:
                    return f"Unerwarteter Fehler: {str(e)}"
            else:
                return "Info: Das Verzeichnis existiert bereits."
        else:
            return "Eroare: Der Pfad ist ungültig."

    def view_path_files(self, path, ext='jpg'):
        """
        Gibt eine Liste von Dateien in einem Verzeichnis zurück, die der angegebenen Erweiterung entsprechen.

        :param path: Der Pfad, in dem nach Dateien gesucht wird.
        :param ext: Die Dateierweiterung, nach der gefiltert wird (Standard: 'jpg').
        :return: Eine Liste der Dateien mit der angegebenen Erweiterung oder eine Fehlermeldung, falls ein Fehler auftritt.
        """
        ext = '.' + ext.lower()  # Concatenation der Erweiterung
        valid_path = self._verify_dir_exists(path)  # Ruft die Verzeichnisprüfungsfunktion auf

        try:
            if not valid_path:
                return []

            # Wenn es ein Verzeichnis ist, wird überprüft, ob sich Dateien mit der entsprechenden
            # Erweiterung im Verzeichnis befinden
            return [f for f in valid_path.iterdir() if f.suffix.lower() == ext and f.is_file()]

        except (PermissionError, FileNotFoundError, OSError) as e:
            return f"Zugriffsfehler: {str(e)}"

    def move_jpg(self, path, ext='jpg', resave=None):
        """
        Bewegt JPG-Dateien von einem Verzeichnis zu einem anderen Verzeichnis und löscht die Originaldateien nach dem Kopieren.

        :param path: Der Pfad, in dem nach JPG-Dateien gesucht wird.
        :param ext: Die Dateierweiterung (Standard: 'jpg').
        :param resave: Wenn gesetzt, werden auch bereits verschobene Dateien erneut gespeichert.
        :return: Eine Nachricht, die den Status des Datei-Verschiebens angibt.
        """
        # Überprüft, ob das Hauptverzeichnis, in dem sich die Bilder befinden, existiert
        valid_path = self._verify_dir_exists(path)

        if not valid_path:
            return "Das Verzeichnis wurde nicht gefunden oder der Pfad ist kein gültiges Verzeichnis."

        # Zum Hauptverzeichnis wird der Name des Verzeichnisses für die Bilder hinzugefügt.
        valid_path_img = valid_path / self.path_jpg
        valid_path_img_dest = self._verify_dir_exists(valid_path_img)  # Es wird im externen Verzeichnis überprüft.

        # Überprüft, ob der Zielpfad für Bilder gültig ist; wenn nicht, wird das Verzeichnis für Bilder erstellt
        if not valid_path_img_dest:
            self._creat_path_jpg(path=valid_path)

        try:
            # Liste der Dateipfade vor dem Kopieren und Löschen
            before_move = self.view_path_files(path, ext=ext)

            # Liste der Dateipfade nach dem Kopieren und Löschen
            after_move = self.view_path_files(valid_path / self.path_jpg, ext=ext)

            moved_file = []  # Liste der Dateinamen, die kopiert werden sollen
            after_names = {f.name for f in after_move}  # Extrahiere die Dateinamen, die kopiert werden sollen

            if not before_move:  # Überprüfe, ob es Daten zum Verschieben gibt
                return f"Es gibt keine Daten zum Verschieben!"

            before_move_sorted = sorted(before_move, key=lambda _:_.name)  # Datei nach Namen sortieren

            # Überprüft, ob die Datei nicht basierend auf dem Namen verschoben wurde
            for file in before_move_sorted:
                save_meth = file.name not in after_names

                # Nur die Dateien werden erneut gespeichert, die noch nicht im Zielverzeichnis existieren und
                # die nicht im jpg-Verzeichnis sind
                if not resave and not save_meth:
                    continue

                file_dest = file.parents[0] / self.path_jpg / file.name  # Zeigt das Zielverzeichnis der Datei an

                shutil.copy2(file, file_dest)  # Kopiert die Dateien mit Metadaten
                os.utime(file_dest,None)  # Aktualisiert die Änderungszeit des Dateis

                moved_file.append(file.name)  # Fügt die Namen der verschobenen Dateien zur Liste hinzu
                try:
                    file.unlink()  # Löschen der Dateien, nachdem sie kopiert wurden
                except Exception as e:
                    print(f"Wir konnten die Datei {file.name} nicht löschen: {e}")

            if moved_file:
                return f"Verschobene Dateien: \n{'\n'.join(moved_file)}"
            else:
                return "Es gibt keine Dateien oder das Verschieben der Dateien wird nicht gewünscht!"

        except (PermissionError, FileNotFoundError, OSError) as e:
            return f"Zugriffsfehler: {str(e)}"


    def file_del(self, path, file_type=None, path_jpg='jpg', resave=True):
        """
        Löscht die Dateien mit einer bestimmten Erweiterung und verschiebt sie bei Bedarf in ein Zielverzeichnis.

        :param path: Der Pfad, in dem die Dateien gesucht werden.
        :param file_type: Die Erweiterung der Dateien, die gelöscht werden sollen.
        :param path_jpg: Das Zielverzeichnis, in das die .jpg-Dateien verschoben werden.
        :param resave: Wenn gesetzt, werden auch bereits verschobene Dateien erneut gespeichert.
        :return: Eine Nachricht, die den Status des Datei-Verschiebens und Löschens angibt.
        """

        # Überprüft, ob das Hauptverzeichnis, in dem die Bilder gespeichert sind, existiert
        valid_path = self._verify_dir_exists(path)

        if not valid_path:
            return "Verzeichnis wurde nicht gefunden oder der Pfad ist kein gültiges Verzeichnis."

        if not file_type:
            return ("Wählen Sie eine Erweiterung, die sich von der bei der Erstellung der Instanz zugewiesenen "
                    "(oder standardmäßigen) unterscheidet!")

        try:
            # Holt die Liste der Dateien mit der angegebenen Erweiterung aus dem gültigen Verzeichnis
            list_del = self.view_path_files(valid_path, ext=file_type)

            # Holt die vollständige Liste aller Dateien im gültigen Verzeichnis, unabhängig von der Erweiterung
            list_view = self.view_path_files(valid_path)

            # Holt die Liste der bereits verschobenen Dateien im angegebenen Verzeichnis für .jpg
            list_view_moved = self.view_path_files(valid_path / path_jpg)

            # Überprüft, ob es Dateien zum Löschen gibt. Wenn nicht, gibt es eine entsprechende Nachricht zurück.
            if not list_del:
                return "Es gibt keine Dateien zum Löschen"

            # Erstellt ein Set mit den Dateinamen aus der vollständigen Liste, um sie später zu überprüfen
            list_check_for_del = {f.stem for f in list_view}

            # Erstellt ein Set mit den Dateinamen der bereits verschobenen Dateien (die .jpg-Dateien),
            # um sie später zu überprüfen
            check_del_jpg = {f.stem for f in list_view_moved}

            # Initialisiert Variablen, um die Anzahl der verschobenen und gelöschten Dateien zu verfolgen
            info_move = 0
            info_del = 0

            # Verschieben, wenn es Dateien zum Verschieben gibt
            for file in list_del:
                # Prüft die Erweiterung der Datei
                file_ext_check = file

                # Wenn die Datei mehrere Erweiterungen hat, wird die Dateierweiterung entfernt
                if len(file.suffixes) > 1:
                    file_ext_check = file.with_suffix('')

                # Überprüft, ob der Dateiname in der Liste der zu löschenden Dateien vorhanden ist
                if file_ext_check.stem in list_check_for_del:
                    # Erhöht den Zähler der verschobenen Dateien
                    info_move += 1

            # Verschiebe alle Dateien mit der angegebenen Erweiterung
            if info_move:
                self.move_jpg(path, ext=file_type, resave=resave)

            # Liste nach dem Verschieben aktualisieren
            list_view_moved = self.view_path_files(valid_path / path_jpg)
            check_del_jpg = {f.stem for f in list_view_moved}

            # Durchlaufe die Dateien, die gelöscht werden müssen
            for file in list_del:
                # Überprüfe die Dateiendung, falls mehrere Endungen vorhanden sind
                file_ext_check = file
                if len(file.suffixes) > 1:
                    file_ext_check = file.with_suffix('')

                # Überprüfe, ob die Datei nicht verschoben wurde (nicht in der Liste der bereits verschobenen Dateien)
                if file_ext_check.stem not in check_del_jpg:
                    try:
                        # Lösche die Datei
                        file.unlink()
                        info_del += 1
                        print(f"Datei gelöscht: {file.name}")
                    except FileNotFoundError:
                        # Falls die Datei nicht gefunden wird, fahre mit der nächsten fort
                        continue
                    except Exception as e:
                        return f"Datei konnte nicht gelöscht werden: {file.name}: {e}"

            msg = []
            if info_move:
                msg.append(f"{info_move} Datei/en erfolgreich verschoben!")
            if info_del:
                msg.append(f"{info_del} Datei/en erfolgreich gelöscht!")
            if not msg:
                msg.append("Es gibt keine Dateien zum Löschen oder Verschieben!")

            return "\n".join(msg)

        except (PermissionError, FileNotFoundError, OSError) as e:
            return f"Zugriffsfehler: {str(e)}"


# path_img = "/home/sandor/Desktop/imagine"  # Der Pfad, in dem sich die Bilder befinden
# obj = ImgSort()  # Instanzaufruf
#
# tt1 = time.perf_counter()  # Starten des Zählers zur Messung der Ausführungszeit
#
# # Anzeigen des Inhalts
# view_img = obj.view_path_files(path_img)
# print(view_img)
#
# # Verschiebe die Dateien des angegebenen Typs oder des Standardtyps (jpg)
# move_jpg = obj.move_jpg(path_img, resave=True)
# move_jpg_1 = obj.move_jpg(path_img, ext='nef', resave=True)
# move_jpg_2 = obj.move_jpg(path_img, ext='pp3', resave=True)
# print(move_jpg)
# print(move_jpg_1)
# print(move_jpg_2)
#
# # Verschiebe automatisch die verarbeiteten Bilder und lösche die nicht verarbeiteten Dateien entsprechend der gewählten
# # Dateierweiterung
# file_del = obj.file_del(path_img, file_type='pp3')
# file_del_1 = obj.file_del(path_img, file_type='nef')
# print(file_del)
# print(file_del_1)
#
# # Stoppen des Zählers zur Messung der Ausführungszeit
# tt2 = time.perf_counter()
#
# # Zeige die Ausführungszeit der Operationen an
# print(f"\n{tt2-tt1:.4f} secunde")
