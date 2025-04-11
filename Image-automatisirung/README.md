# ImgSort - Bildverwaltung

`ImgSort` ist eine Python-Anwendung, die das Organisieren und Verwalten von Bilddateien ermöglicht. Das Programm überprüft das Eingabeverzeichnis, passt die Größe von `.jpg`-Dateien an und verschiebt sie in ein dediziertes Unterverzeichnis (`jpg`), sowie das Löschen der verarbeiteten Dateien.

## Installation

1. Klone das Repository:

    ```bash
    https://github.com/leoneincurabile/Portofolio.git
    cd ImgSort
    ```

2. Erstelle und aktiviere eine virtuelle Umgebung (optional):

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # Für Linux/Mac
    venv\Scripts\activate      # Für Windows
    ```

3. Installiere die erforderlichen Abhängigkeiten:

    ```bash
    pip install -r requirements.txt
    ```

## Nutzung

1. Stelle sicher, dass das Bildverzeichnis existiert und `.jpg`-Dateien (oder andere gewünschte Dateitypen) enthält.

2. Erstelle ein Objekt der `ImgSort`-Klasse:

    ```
    python
    from image-automatisirung import ImgSort
    ```

3. Verwende die verfügbaren Funktionen, um die Dateien zu organisieren:

    ### Überprüfen des Verzeichnisses

    Überprüft, ob ein Verzeichnis existiert und gültig ist.

    ```
    python
    ImgSort._verify_dir_exists('Pfad/zum/Verzeichnis')
    ```

    ### Erstellen des `jpg`-Verzeichnisses

    Erstelle ein `jpg`-Verzeichnis für die verarbeiteten Bilddateien.

    ```
    python
    img_sort = ImgSort()
    img_sort._create_path_jpg('Pfad/zum/Verzeichnis')
    ```

    ### Anzeigen der Dateien

    Zeige die Dateien mit der gewünschten Erweiterung aus einem Verzeichnis an.

    ```
    python
    img_sort.view_path_files('Pfad/zum/Verzeichnis', ext='jpg')
    ```

    ### Verschieben der Dateien

    Verschiebe `.jpg`-Dateien in ein dediziertes Unterverzeichnis `jpg`.

    ```
    python
    img_sort.move_jpg('Pfad/zum/Verzeichnis')
    ```

    ### Löschen der Dateien

    Lösche die gewünschten Dateien aus dem angegebenen Verzeichnis.

    ```
    python
    img_sort.file_del('Pfad/zum/Verzeichnis', file_type='pp3')
    ```

## Funktionen

- Überprüft die Existenz eines Verzeichnisses und erstellt ein Unterverzeichnis für Bilder.
- Verschiebt `.jpg`-Dateien in ein `jpg`-Unterverzeichnis.
- Ermöglicht das Anpassen der Dateigröße (zukünftige Implementierung).
- Ermöglicht das Löschen von nicht verarbeiteten Dateien.

## Beiträge

Wenn du zu diesem Projekt beitragen möchtest, folge diesen Schritten:

1. Forke dieses Repository.
2. Erstelle einen neuen Branch für deine Funktionalität (`git checkout -b feature-name`).
3. Nimm die notwendigen Änderungen vor und füge Tests hinzu.
4. Sende einen Pull Request.

## Lizenz

Veröffentlicht unter der MIT-Lizenz.
