# Systembibliothek importieren
import os.path

# Externe Bibliothek importieren
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# lokal importieren
from Statistiken import CostOfLiving


class Diagrams:
    def __init__(self):
        self.folder_path = "diagramm"  # Die Dateipfade
        self.obj = CostOfLiving()  # Es wird nur einmal aufgerufen, weil die Daten sich nicht ändern.
        self.fig, self.ax = None, None  # Platzhalter für die Matplotlib-Figur und Achsen

    def diag_cost_of_living(self, cost_of_living:int):
        """
        Ein Objekt wird aufgerufen, aber mit einer Methode des Objekts können mehrere Diagramme erstellt werden.
        Die Figur wird also nicht für das aufgerufene Objekt erstellt, sondern für die aufgerufene Methode.
        :param cost_of_living: ein Integer, der den Index des Lebenshaltungsindex angibt
        :return: None | str - Gibt den Untertitel (den Namen) des Diagramms
        """
        self.fig, self.ax = plt.subplots(figsize=(14, 6))  # Ein Subplot erstellen

        # Ein Tupel, das ein DataFrame und eine Zeichenkette mit dem Dateinamen enthält.
        d = self.obj.top_10_high_cost_country(cost_of_living)

        # Es wird überprüft, ob die Daten vom Typ DataFrame sind.
        if not isinstance(d[0], pd.DataFrame):
            return f"Fehler. Die Daten müssen vom Typ DataFrame sein."

        x = d[0]['Country'].to_numpy()  # Umwandlung einer Serie in ein Array
        y = d[0]['Cost of Living Index'].to_numpy() # Umwandlung einer Serie in ein Array
        nr_country = len(x)  # Totale Anzahl der Einträge

        # Zeige die Daten auf dem erstellten Diagramm an.
        sub_titl = f"Top {nr_country} Länder mit den höchsten Lebenshaltungskosten {cost_of_living}" # Die Titel
        self.fig.suptitle(sub_titl)  # Erstelle den Titel
        self.ax.barh(x, y, color="lightblue")  # Balkendiagramm

        plt.xlabel("Lebenshaltungskostenindex")  # Beschriftungen die x-Achse
        plt.ylabel("Länder")  # Beschriftungen die y-Achse

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
        :return: True | str - der Status des Verzeichnisses
        """
        try:
            if not os.path.exists(self.folder_path):  # Überprüfen, ob das Verzeichnis existiert.
                os.makedirs(self.folder_path, mode=0o777)  # Erstelle ein Verzeichnis mit den Rechten 777
        except Exception as e:
            return f"Fehler {e}"

        return True

    def corr_cost_rent(self, continent= None):
        """
        Die Anzeige des Diagramms zur Korrelation zwischen dem Lebenshaltungskostenindex und dem Rent Index,
        mit der Möglichkeit, den Kontinent zu filtern.
        :param continent: str | None - nützlich, um die Daten nach dem gewählten Kontinent zu filtern.
        :return: str - die Titel
        """
        # Analysierte Daten
        correlation_data = self.obj.correlation_cost_living_rent(continent)

        # Etikett der gewünschten anzuzeigenden Daten
        x1, x2 = ('Cost of Living Index','Lebenshaltungskostenindex')
        y1, y2 = ('Rent Index','Mietindex')

        # Streudiagramm mit einer Regressionslinie
        sns.regplot(x=x1, y=y1, data=correlation_data, ci=None)

        # Für jede Zeile im DataFrame werden die Ländernamen basierend auf der Position abgerufen,
        # die jeder Wert in x bzw. y einnimmt.
        for i in range(correlation_data.shape[0]):
            plt.text(correlation_data[x1].iloc[i], correlation_data[y1].iloc[i],
                     correlation_data['Country'].iloc[i], fontsize=9, ha='right', color='green')

        # Informationen zum Diagramm
        plt.title(f"Korrelation zwischen {x2} und {y2}")  # Die Titel
        plt.xlabel(f'{x2}')  # Beschriftungen die x-Achse
        plt.ylabel(f'{y2}') # Beschriftungen die y-Achse

        # Es ist wichtig, die aktuelle Figur zum Speichern abzurufen.
        self.fig = plt.gcf()  # Aktuelle Figur abrufen
        self.fig.set_size_inches(14,6)  # Diagrammgröße
        ax = plt.gca()  # Aktuelle Achsen abrufen
        diagramm_title = ax.get_title() # Titel abrufen
        plt.grid() # Gitter

        try:
            plt.show(block=False)  # Diagramm anzeigen
            plt.pause(3)  # Es pausiert für einigen Sekunden, damit das Diagramm sichtbar bleibt.
        finally:
            plt.close(self.fig)  # Das Diagramm wird geschlossen.

        return diagramm_title

    def save(self, file_name):
        """
        Die Datei speichern.
        :param file_name: str - der Name der Detei
        :return: str - der Status der Speicherung
        """
        file_name = file_name + '.png'  # Zur Diagrammbezeichnung wird auch die Dateierweiterung hinzugefügt.
        if self.dir_check() is not True:  #
            return f"Das Verzeichnis ({self.folder_path}) existiert nicht oder kann nicht erstellt werden."

        file_name = os.path.join("diagramm", file_name)
        while True:
            if not os.path.isfile(file_name):  # Überprüfen, ob das Verzeichnis existiert.
                self.fig.savefig(file_name, dpi=150, bbox_inches='tight')  # Die Datei speichern
                return "Die Datei wurde gespeichert!"

            # 1, um erneut zu speichern, und 2, um nicht erneut zu speichern.
            inp = input("Die Datei existiert, wähle die Optionen aus. \n 1. Datei wieder speichern\n "
                        "2. Datei nicht wieder speichern \n")
            try:
                if int(inp) == 1:
                    self.fig.savefig(file_name, dpi=150, bbox_inches='tight')  # Die Datei speichern
                    return "Die Datei wurde erneut gespeichert!"
                elif int(inp) == 2:
                    return "Die Datei wurde nicht erneut gespeichert!"
            except ValueError:
                print("Es wurde keine Option ausgewählt.")


# diag = Diagrams()  # Objekt erstellen
#
# # Horizontales Balkendiagramm
# cost_of_liv_index = 65  # Benötigen den Lebenshaltungskostenindex
# cost_of_liv = diag.diag_cost_of_living(cost_of_liv_index)  # Zeige das Diagramm für ein paar Sekunden an
#
# mesaj_save = diag.save(cost_of_liv)  # Diagramm speichern
# print(mesaj_save,'\n\n')
#
#
# # Das Diagramm der Korrelation
# country_select = "Europe" # None oder ein Kontinentname
#
# # Zeige das Korrelationsdiagramm mit oder ohne Kontinentfilter.
# corr_cost_liv_rent = diag.corr_cost_rent(country_select)
#
# corr_cost_liv_rent_sv = diag.save(corr_cost_liv_rent) # Korrelationsdiagramm speichern
# print(corr_cost_liv_rent_sv)
