# Cost of Living - Datenanalyse und Diagramme

`Cost of living` ist eine Python-Anwendung, die die Datenanalyse der Lebenshaltungskosten für die meisten Länder der Welt ermöglicht. Sie umfasst sowohl die Datenanalyse als auch die Anzeige von Diagrammen.

## Installation

1. Klone dieses Repository:

    ```bash
    https://github.com/leoneincurabile/Portofolio.git
    cd Portofolio
    ```

2. Erstelle und aktiviere eine virtuelle Umgebung (optional):

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # für Linux/Mac
    venv\Scripts\activate      # für Windows
    ```

3. Installiere die erforderlichen Abhängigkeiten:

    ```bash
    pip install -r requirements.txt
    ```

## Nutzung

### Datenanalyse für Cost of Living
   
Um die Daten zu den Lebenshaltungskosten zu analysieren, importiere die Klasse `CostOfLiving` aus der Datei `analiza_cost_of_living`:

    ```
    python
    from analiza_cost_of_living import CostOfLiving
    ```

1. Überprüfung der Datei: Stellen Sie sicher, dass die .csv-Datei vorhanden ist.
2. Um die Daten zu den Lebenshaltungskosten zu analysieren, erstellen Sie ein Objekt der Klasse `CostOfLiving`:
    ```
    python
    obj = CostOfLiving()
    ```

3. Analyse der Daten der 10 Länder mit Kontinent und Lebenshaltungskosten, sortiert nach den Lebenshaltungskosten, nachdem das Objekt erstellt wurde:

    ```
    python
    percents_cost_of_living = 70
    obj.top_10_high_cost_country(percents_cost_of_living)
    ```

4. Die Daten werden bereinigt und optimiert, damit sie in der Analyse und für die Erstellung von Diagrammen verwendet werden können:

    ```
    python
    obj.clean_data_duplicat_drop()
    ```

5. Datenanalyse durch Korrelation der Mietkosten im Lebensunterhalt mit oder ohne Filtern des Kontinents:

    ```
    python
    continent_selected = "Africa"
    obj.corr_cost_living_rent(continent_selected)
    ```

6. Speichern der Daten in einer .csv-Datei:

    ```
    python
    continent_selected = "Africa"
    correlation = obj.corr_cost_living_rent(continent_selected)
    obj.save_file(correlation, continent_selected)
    ```

### Diagramme für Cost of Living

Um die Daten zu den Lebenshaltungskosten anzuzeigen, erstellen Sie ein Objekt der Klasse `CostOfLiving`:
    ```
    python
    from analiza_cost_of_living import CostOfLiving
    ```

1. Überprüfung der Datei: Stellen Sie sicher, dass die .csv-Datei vorhanden ist.
2. Um die Daten zu den Lebenshaltungskosten zu analysieren, erstellen Sie ein Objekt der Klasse `Diagrams`:
    ```
    python
    obj = Diagrams()
    ```

3. Top 10 Länder mit den höchsten Lebenshaltungskosten, wo die Lebenshaltungskosten höher sind als die angegebene Zahl:

    ```
    python
    cost_of_liv_index = 65
    diag.diag_cost_of_living(cost_of_liv_index)
    ```

4. Korrelation Diagramm zwischen Cost of Living Index und Rent Index mit der Möglichkeit, den Kontinent zu filtern:

    ```
    python
    country_select = "Europe"
    diag.corr_cost_rent(country_select)
    ```

5. Korrelationen zwischen Indizes:

    ```
    python
    diag.heat_diagramm()
    ```

6. Variation der Lebenshaltungskosten:

    ```
    python
    diag.boxplot_cost_living() 
    ```

7. Verteilung des Restaurantindex:

    ```
    python
    diag.histo_restaurant()
    ```

8. Diagramme speichern

    ```
    python
    histo_giag = diag.histo_restaurant()
    diag.save(histo_diag)
    ```
