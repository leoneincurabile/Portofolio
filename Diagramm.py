import os.path

import matplotlib.pyplot as plt

from Statistiken import CostOfLiving

class Diagrams:
    def __init__(self):
        self.folder_path = "diagramm"
        self.obj = CostOfLiving()  # Es wird nur einmal aufgerufen, weil die Daten sich nicht ändern.
        self.fig, self.ax = None, None

    def diag_cost_of_living(self, cost_of_living):
        """
        Ein Objekt wird aufgerufen, aber mit einer Methode des Objekts können mehrere Diagramme erstellt werden.
        Die Figur wird also nicht für das aufgerufene Objekt erstellt, sondern für die aufgerufene Methode.
        :param cost_of_living: ein Integer, der den Index des Lebenshaltungsindex angibt
        :return: str. Gibt den Untertitel (den Namen) des Diagramms
        """
        self.fig, self.ax = plt.subplots(figsize=(12, 8), dpi=80)
        d = self.obj.top_10_high_cost_country(cost_of_living)
        x = d[0]['Country'].to_numpy()
        y = d[0]['Cost of Living Index'].to_numpy()
        nr_country = len(x)
        # afiseaza datele pe diagrama creata
        self.ax.clear()
        sub_titl = f"Top {nr_country} Länder mit den höchsten Lebenshaltungskosten {cost_of_living}"
        self.fig.suptitle(sub_titl)
        self.ax.barh(x, y, color="lightblue")

        plt.xlabel("Lebenshaltungskostenindex")
        plt.ylabel("Länder")

        plt.gca().invert_yaxis()  # Kehrt die Richtung der y-Achse um.
        plt.xticks(rotation=0)  # Der Text der x-Achse nicht neigt sich

        try:
            plt.show(block=False)  # Diagramm anzeigen
            plt.pause(3)  # Es pausiert für einigen Sekunden, damit das Diagramm sichtbar bleibt.
        finally:
            plt.close(self.fig)  # Das Diagramm wird geschlossen.

        return self.fig.get_suptitle()

    def dir_check(self):
        """
        Überprüfe, ob das Verzeichnis existiert. Falls nicht, erstelle es.
        :return: True oder Fehler - der Status des Verzeichnisses
        """
        try:
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path, mode=0o777)
        except Exception as e:
            return f"Fehler {e}"

        return True

    def save(self, file_name):
        """
        Die Datei speichern.
        :param file_name: str, der Name der Detei
        :return: str, der Status der Speicherung
        """
        file_name = file_name + '.png'
        if self.dir_check() is not True:
            return f"Das Verzeichnis ({self.folder_path}) existiert nicht oder kann nicht erstellt werden."

        file_name = os.path.join("diagramm", file_name)
        while True:
            if not os.path.isfile(file_name):
                self.fig.savefig(file_name, dpi=150, bbox_inches='tight')
                return "Die Datei wurde gespeichert!"

            inp = input("Die Datei existiert, wähle die Optionen aus. \n 1. Datei wieder speichern\n "
                        "2. Datei nicht wieder speichern \n")
            try:
                if int(inp) == 1:
                    self.fig.savefig(file_name, dpi=150, bbox_inches='tight')
                    return "Die Datei wurde erneut gespeichert!"
                elif int(inp) == 2:
                    return "Die Datei wurde nicht erneut gespeichert!"
            except ValueError:
                print("Es wurde keine Option ausgewählt.")

cost_of_living_index = 65  # Benötigen den Lebenshaltungskostenindex
diag = Diagrams()  # Objekt erstellen

diagram_cost_of_living = diag.diag_cost_of_living(cost_of_living_index)  # Zeige das Diagramm für ein paar Sekunden an
# print(diagram_cost_of_living)

mesaj_save = diag.save(diagram_cost_of_living)  # Diagramm speichern
# print(mesaj_save)