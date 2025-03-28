# Systembibliothek importieren
import os.path

import logging

# Externe Bibliothek importieren
import pandas as pd


class CostOfLiving:
    # Informationen über Logs.
    logger = logging.getLogger()  # Erhalte den standardmäßigen Logger.
    consol_handler = logging.StreamHandler()  # Erstellen eines Handlers für die Konsole.
    file_handler = logging.FileHandler("statistiken.log")

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s") # Die Anzeigeart der Log-Nachrichten
    consol_handler.setFormatter(formatter)  # Lege das Format des Handlers fest.
    file_handler.setFormatter(formatter)  # Lege das Format des Handlers fest.

    logger.addHandler(file_handler)  # Erstelle den Handler.
    logger.addHandler(consol_handler)  # Anzeige in der Konsole.
    logger.setLevel(logging.INFO)  # Das minimale Log-Level.

    def __init__(self):
        """
        Initialisiere das Objekt und ladet die Daten aus einer CSV-Datei.
        """
        # Setze die Anzeige aller Spalten und aller Zeilen
        pd.set_option('display.max_columns', None, 'display.max_rows', None)
        self.folder_path = 'daten'

        name_file = 'Cost_of_Living_Index_by_Country_2024.csv'
        try:
            self.df = pd.read_csv(name_file)
            self.__class__.logger.info(f"Die Datei {name_file} wurde erfolgreich geöffnet.")
        except FileNotFoundError:
            self.__class__.logger.error(f"Die Datei {name_file} wurde nicht gefunden.")
            print("Die Datei wurde nicht gefunden.")
            self.df = None
        except pd.errors.ParserError:
            self.__class__.logger.error(f"Die Datei {name_file} ist im falschen Format.")
            print("Fehler im CSV-Dateiformat! Bitte stelle sicher, dass es korrekt formatiert ist.")
            self.df = None
        except Exception as e:
            self.__class__.logger.error(f"Fehler Datei {name_file} {e}.")
            print(f"Fehler {str(e)}")
            self.df = None

        self.continent_mapping = {
            'Afghanistan': 'Asia', 'Albania': 'Europe', 'Algeria': 'Africa', 'Andorra': 'Europe',
            'Angola': 'Africa', 'Antigua and Barbuda': 'North America', 'Argentina': 'South America',
            'Armenia': 'Asia', 'Australia': 'Oceania', 'Austria': 'Europe', 'Azerbaijan': 'Asia',
            'Bahamas': 'North America', 'Bahrain': 'Asia', 'Bangladesh': 'Asia', 'Barbados': 'North America',
            'Belarus': 'Europe', 'Belgium': 'Europe', 'Belize': 'North America', 'Benin': 'Africa',
            'Bhutan': 'Asia', 'Bolivia': 'South America', 'Bosnia And Herzegovina': 'Europe', 'Botswana': 'Africa',
            'Brazil': 'South America', 'Brunei': 'Asia', 'Bulgaria': 'Europe', 'Burkina Faso': 'Africa',
            'Burundi': 'Africa', 'Cabo Verde': 'Africa', 'Cambodia': 'Asia', 'Cameroon': 'Africa',
            'Canada': 'North America', 'Central African Republic': 'Africa', 'Chad': 'Africa', 'Chile': 'South America',
            'China': 'Asia', 'Colombia': 'South America', 'Comoros': 'Africa', 'Congo (Congo-Brazzaville)': 'Africa',
            'Costa Rica': 'North America', 'Croatia': 'Europe', 'Cuba': 'North America', 'Cyprus': 'Europe',
            'Czech Republic': 'Europe', 'Denmark': 'Europe', 'Djibouti': 'Africa', 'Dominica': 'Caribbean',
            'Dominican Republic': 'North America', 'Ecuador': 'South America', 'Egypt': 'Africa', 'El Salvador': 'North America',
            'Equatorial Guinea': 'Africa', 'Eritrea': 'Africa', 'Estonia': 'Europe', 'Eswatini (fmr. "Swaziland")': 'Africa',
            'Ethiopia': 'Africa', 'Fiji': 'Oceania', 'Finland': 'Europe', 'France': 'Europe', 'Gabon': 'Africa',
            'Gambia': 'Africa', 'Georgia': 'Asia', 'Germany': 'Europe', 'Ghana': 'Africa', 'Greece': 'Europe',
            'Grenada': 'Caribbean', 'Guatemala': 'North America', 'Guinea': 'Africa', 'Guinea-Bissau': 'Africa',
            'Guyana': 'South America', 'Haiti': 'North America', 'Honduras': 'North America', 'Hungary': 'Europe',
            'Iceland': 'Europe', 'India': 'Asia', 'Indonesia': 'Asia', 'Iran': 'Asia', 'Iraq': 'Asia',
            'Ireland': 'Europe', 'Israel': 'Asia', 'Italy': 'Europe', 'Jamaica': 'North America', 'Japan': 'Asia',
            'Jordan': 'Asia', 'Kazakhstan': 'Asia', 'Kenya': 'Africa', 'Kiribati': 'Oceania', 'Korea (North)': 'Asia',
            'Korea (South)': 'Asia', 'Kuwait': 'Asia', 'Kyrgyzstan': 'Asia', 'Laos': 'Asia', 'Latvia': 'Europe',
            'Lebanon': 'Asia', 'Lesotho': 'Africa', 'Liberia': 'Africa', 'Libya': 'Africa', 'Liechtenstein': 'Europe',
            'Lithuania': 'Europe', 'Luxembourg': 'Europe', 'Madagascar': 'Africa', 'Malawi': 'Africa',
            'Malaysia': 'Asia', 'Maldives': 'Asia', 'Mali': 'Africa', 'Malta': 'Europe', 'Marshall Islands': 'Oceania',
            'Mauritania': 'Africa', 'Mauritius': 'Africa', 'Mexico': 'North America', 'Micronesia': 'Oceania',
            'Moldova': 'Europe', 'Monaco': 'Europe', 'Mongolia': 'Asia', 'Montenegro': 'Europe', 'Morocco': 'Africa',
            'Mozambique': 'Africa', 'Myanmar (formerly Burma)': 'Asia', 'Namibia': 'Africa', 'Nauru': 'Oceania',
            'Nepal': 'Asia', 'Netherlands': 'Europe', 'New Zealand': 'Oceania', 'Nicaragua': 'North America',
            'Niger': 'Africa', 'Nigeria': 'Africa', 'North Macedonia': 'Europe',
            'Norway': 'Europe', 'Oman': 'Asia', 'Pakistan': 'Asia', 'Palau': 'Oceania', 'Panama': 'North America',
            'Papua New Guinea': 'Oceania', 'Paraguay': 'South America', 'Peru': 'South America', 'Philippines': 'Asia',
            'Poland': 'Europe', 'Portugal': 'Europe', 'Qatar': 'Asia', 'Romania': 'Europe', 'Russia': 'Europe',
            'Rwanda': 'Africa', 'Saint Kitts and Nevis': 'Caribbean', 'Saint Lucia': 'Caribbean', 'Saint Vincent and the Grenadines': 'Caribbean',
            'Samoa': 'Oceania', 'San Marino': 'Europe', 'Sao Tome and Principe': 'Africa', 'Saudi Arabia': 'Asia',
            'Senegal': 'Africa', 'Serbia': 'Europe', 'Seychelles': 'Africa', 'Sierra Leone': 'Africa',
            'Singapore': 'Asia', 'Slovakia': 'Europe', 'Slovenia': 'Europe', 'Solomon Islands': 'Oceania',
            'Somalia': 'Africa', 'South Africa': 'Africa', 'South Sudan': 'Africa', 'Spain': 'Europe', 'Sri Lanka': 'Asia',
            'Sudan': 'Africa', 'Suriname': 'South America', 'Sweden': 'Europe', 'Switzerland': 'Europe',
            'Syria': 'Asia', 'Taiwan': 'Asia', 'Tajikistan': 'Asia', 'Tanzania': 'Africa', 'Thailand': 'Asia',
            'Timor-Leste': 'Asia', 'Togo': 'Africa', 'Tonga': 'Oceania', 'Trinidad And Tobago': 'North America',
            'Tunisia': 'Africa', 'Turkey': 'Asia', 'Turkmenistan': 'Asia', 'Tuvalu': 'Oceania', 'Uganda': 'Africa',
            'Ukraine': 'Europe', 'United Arab Emirates': 'Asia', 'United Kingdom': 'Europe', 'United States': 'North America',
            'Uruguay': 'South America', 'Uzbekistan': 'Asia', 'Vanuatu': 'Oceania', 'Vatican City': 'Europe',
            'Venezuela': 'South America', 'Vietnam': 'Asia', 'Yemen': 'Asia', 'Zambia': 'Africa', 'Zimbabwe': 'Africa',
            'Hong Kong (China)': 'Asia', 'Puerto Rico': 'South America', 'South Korea': 'Asia', 'Palestine': 'Asia',
            'Kosovo (Disputed Territory)': 'Europe'
        }

    def dir_check(self):
        """
        Überprüfe, ob das Verzeichnis existiert, und estelle es, wenn nicht.
        :return: True sau Fehler - der Status des Verzeichnisses
        """
        try:
            if not os.path.exists(self.folder_path):  # Überprüfen, ob das Verzeichnis existiert.
                os.makedirs(self.folder_path, mode=0o777)  # Erstelle ein Verzeichnis mit den Rechten 777
                self.__class__.logger.info(f"S-a creat diredtorul: {self.folder_path}")
        except Exception as e:
            self.__class__.logger.error(f"Fehler bei der Überprüfung/Erstellung des Verzeichnisses: {e}.")
            return f"Fehler {e}"

        return True

    def add_country(self):
        """
        Fügen Sie die Pandas-Serie mit den Kontinenten hinzu, damit sie in die CSV-Datei aufgenommen werden können
        :return:
            - None | True | False: Status der Hinzufügung
            - None | Series | DataFrame:
                - None: Keine Daten
                - Series: Gibt die Länder zurück, die keine Entsprechung in continent_mapping haben.
                - DataFrame: Gibt die bestehenden und neu hinzugefügten Daten zurück.
            - str: Informationen zum Status
        """
        try:
            # Überprüfe das Format des Datenuploads
            if not isinstance(self.df, pd.DataFrame):
                self.__class__.logger.error("Die Daten wurden nicht im richtigen Format geladen, bitte überprüfen Sie die Datei.")
                return None, None, (f"Die Daten wurden nicht im richtigen Format geladen, "
                                    f"bitte überprüfen Sie die Datei.")

            # Die Nummerierung des DataFrames soll bei der Nummer 1 beginnen.
            self.df.index = range(1, len(self.df) + 1)

            # Eine Pandas-Serie aus einem DataFrame für Country
            if 'Continent' not in self.df.columns or self.df['Continent'].isnull().any():
                # Weist der Spalte 'Continent' den Wert zu, der im Dictionary durch den Länderschlüssel zugeordnet ist.
                self.df['Continent'] = self.df['Country'].map(self.continent_mapping)
                self.__class__.logger.info("Zuweisung der Spalte Continent")
                return True, self.df, "Zuweisung der Spalte Continent"

            # Überprüfe, ob das Land in continent_mapping mit dem Land in der Datei übereinstimmt,
            # um den Kontinent zuzuordnen.
            exists_country =  self.df['Country']
            if isinstance(exists_country, pd.Series):
                # Gibt eine Pandas-Serie mit den Werten True oder False für die Kontinente zurück,
                # die im Schlüssel des Dictionaries continent_mapping erscheinen.
                country_found_bool = exists_country.isin(self.continent_mapping.keys())

                # Gibt die ID und das Land aus, für das das Land nicht in continent_mapping existiert.
                # In diesem Fall wird ~ das Gegenteil anzeigen, d.h. für True wird False angezeigt und
                # für False wird True angezeigt.
                country_not_found = self.df[~ country_found_bool]['Country']

                if len(country_not_found) > 0:
                    # Wir verwenden ausdrücklich pd.Series(), um die Daten im Pandas-Series-Typ zurückzugeben.
                    self.__class__.logger.warning("Überprüfe den/die Ländernamen in der Datenbank.")
                    return False, pd.Series(country_not_found), f"Überprüfe den/die Ländernamen in der Datenbank."
                else:
                    self.__class__.logger.warning("Es gibt keine Kontinente, die zu Ländern hinzugefügt werden müssen.")
                    return False, None, f"Es gibt keine Kontinente, die zu Ländern hinzugefügt werden müssen."

        except Exception as e:
            self.__class__.logger.error(f"Unbekannter Fehler: {e}")
            return None, None, f"Unbekannter Fehler: {e}"

    @classmethod
    def save_country_to_csv(cls, file_c_save:tuple, file_name_c_save:str):
        """
        Speichere die Daten aus fine_c_name in einer CSV-Datei.
        :param file_c_save: (tuple) - alle Daten, die in die CSV-Datei eingetragen werden.
        :param file_name_c_save: (str) - der Dateiname
        :return: None | (str) - der Status des Speichervorgangs der Kontinente
        """
        try:
            file_status = file_c_save[0] # boole | NoneType
            file_data = file_c_save[1]  # Dataframe | Series
            file_text = file_c_save[2]  # str

            # Überprüfen, ob der Name vom Typ String ist.
            if not isinstance(file_name_c_save, str):
                cls.logger.error(f"Falscher Dateiname.")
                return None, f"Falscher Dateiname."

            # Wenn die Daten vom Typ DataFrame sind, wird die Datei gespeichert.
            if isinstance(file_data, pd.DataFrame):
                file_data.to_csv(file_name_c_save, mode='w', header=True, index=False)
                cls.logger.info(f"Die Daten mit Kontinent wurden der Datei ({file_name_c_save}) hinzugefügt.")
                return True, f"Die Daten mit Kontinent wurden der Datei ({file_name_c_save}) hinzugefügt."

            # Überprüfen, ob die Daten vom Typ Pandas Series sind
            if isinstance(file_data, pd.Series):
                cls.logger.error(file_text)
                return None, file_text

            # Überprüfen Sie den Status der Dateneingabe.
            if file_status is None:
                cls.logger.error(f"Kann nicht gespeichert werden.")
                return None, f"Kann nicht gespeichert werden."
            elif file_status is False:
                cls.logger.warning(file_text)
                return None, file_text

        except AttributeError:
            cls.logger.error(f"Es gibt kein Land für den zugeordneten Kontinent.")
            return None, f"Es gibt kein Land für den zugeordneten Kontinent."
        except Exception as e:
            cls.logger.error(f"Fehler {str(e)}")
            return None, f"Fehler {str(e)}"

    def top_10_high_cost_country(self, cost_of_living:int):
        """
        Zeige die Top 10 Länder mit Kontinent und Lebenshaltungskosten, sortiert nach den Lebenshaltungskosten.
        :param cost_of_living: int - der minimale Wert des Lebenshaltungskostenindex.
        :return: tuple (DataFrame sau None, str) - ein Tupel, das ein DataFrame mit den Top 10 Ländern und
        einen String mit dem Dateinamen enthält.
        """

        if not isinstance(cost_of_living, int):
            self.__class__.logger.error(f"Die Lebenshaltungskosten müssen eine ganze Zahl sein!")
            return None, f"Die Lebenshaltungskosten müssen eine ganze Zahl sein!"

        if not isinstance(self.df, pd.DataFrame):
            self.__class__.logger.error(f"Es muss ein DataFrame sein.")
            return None, f"Es muss ein DataFrame sein."

        self.df['Cost of Living Index'] = pd.to_numeric(self.df['Cost of Living Index'], errors='coerce')
        if self.df['Cost of Living Index'].isnull().any():
            self.__class__.logger.error(f"Es fehlen Werte für den Cost of Living Index")
            return ValueError, f"Es fehlen Werte für den Cost of Living Index"

        # Wählen Sie Kontinent, Land, Lebenshaltungskostenindex, wobei der Lebenshaltungskostenindex größer ist als
        # der angeforderte Wert
        high_cost = self.df[(self.df['Cost of Living Index'] > cost_of_living)][['Continent','Country',
                                                                                 'Cost of Living Index']]

        # Sortiere nach dem Lebenshaltungskostenindex in absteigender Reihenfolge und wähle nur die ersten 10 aus
        high_cost = high_cost.sort_values(by='Cost of Living Index', ascending=False).head(10)

        # Setzen Sie den Index zurück und beginnen Sie bei 1
        high_cost.reset_index(drop=True, inplace = True)
        high_cost.index +=1

        self.__class__.logger.info(f"Anzeige von Informationen {self.top_10_high_cost_country.__name__}")
        return high_cost, 'top 10 high cost country.csv'

    def save_file(self, file_data:pd.DataFrame, file_name_saved:str):
        """
        # Speichern Sie die Datei mit den geladenen Daten. Sie muss zuerst ein DataFrame und dann den Dateinamen enthalten.
        :param file_data: dataframe - alle Daten, die in die CSV-Datei eingefügt werden
        :param file_name_saved: str - der Dateiname der CSV-Datei
        :return: tuple (bool, str) - der Status des Speicherns der Datei
        """
        file_path = ''
        if self.dir_check() is True:
            if not file_name_saved.endswith(".csv"):
                file_name_saved += ".csv"  # Füge die Dateierweiterung zum Dateinamen hinzu

            current_dir = os.getcwd() # Aktuelles Verzeichnis
            file_path = os.path.join(current_dir, self.folder_path, file_name_saved)

        if not isinstance(file_name_saved, str):
            self.__class__.logger.error("Falscher Dateiname")
            return False, "Falscher Dateiname"

        if not isinstance(file_data, pd.DataFrame):
            if ValueError:
                self.__class__.logger.error("Fehlende Daten in der Tabelle")
                return False, "Fehlende Daten in der Tabelle"

        f_nan = file_data.isna().any()  # Variablen geben boolesche Werte zurück, wo NaN vorhanden ist.
        if True in f_nan.values:
            # Zeige die Einträge mit fehlenden Daten an.
            file_data_lost = file_data[file_data.isna().any(axis=1)]
            position = file_data_lost.iloc[:,[1]] # Zeige nur Index und Spalte 1
            self.__class__.logger.error(f"Wichtige Daten fehlen in der Tabelle an Position: \n{position}")
            return False, f"Wichtige Daten fehlen in der Tabelle an Position: \n{position}"

        if file_path:
            try:
                # Speichere die Datei
                file_data.to_csv(file_path, index=True, index_label="Index")
                self.__class__.logger.info(f"Datei wurde unter dem Namen gespeichert: {file_name_saved}")
                return True, f"Datei wurde unter dem Namen gespeichert: {file_name_saved}"
            except Exception as e:
                self.__class__.logger.error(f"Fehler {str(e)}")
                return False, f"Fehler {str(e)}"
        else:
            self.__class__.logger.error("Das Verzeichnis wurde nicht erstellt oder ist ungültig.")
            return False, "Das Verzeichnis wurde nicht erstellt oder ist ungültig."

    def clean_data_duplicat_drop(self, verbose=False):
        """
        Bereinige die Daten, indem du Duplikate und NaN-Werte entfernst.
        :param verbose: True | False
        :return: tuple
            => verbose = True:
                - Dataframe: Die bereinigten Daten.
                - int: Anzahl der ursprünglichen Daten.
                - int: Anzahl der verbleibenden Daten.
                - int: Anzahl der Duplikatdaten.
                - int: Anzahl der entfernten Daten.
                - dataframe: Duplikatdaten.
                - dataframe: Entfernte Daten.
            => verbose = False:
                - Dataframe: Die bereinigten Daten.
                - int: Anzahl der verbleibenden Daten.
                - int: Anzahl der Duplikatdaten.
                - int: Anzahl der entfernten Daten.
        """
        if not isinstance(self.df, pd.DataFrame):
            self.__class__.logger.error("Es muss ein DataFrame sein.")
            return None, "Es muss ein DataFrame sein."

        initial_row = len(self.df)
        # Identifizierung und Entfernung von Duplikatdaten.
        duplicat_data = self.df[self.df.duplicated()]  # Gibt die duplizierten Daten zurück.
        self.df = self.df.drop_duplicates()  # Eliminiere die doppelten Daten.
        duplicat_row = len(duplicat_data)  # Anzahl der Duplikate

        # Identifizierung und Entfernung von NaN-Daten
        drop_data = self.df[self.df.isna().any(axis=1)]  # Extrahiere die Daten, die mindestens einen NaN-Wert enthalten
        self.df = self.df.dropna()  # Lösche die Datensätze ohne Daten
        drop_row = len(drop_data)  # Anzahl der entfernten Daten
        total_row = len(self.df)  # Gesamtzahl der bereinigten Daten

        # Gibt mehr Informationen zurück, wenn verbose auf True gesetzt ist
        if verbose:
            self.__class__.logger.info("Detaillierte Datenanzeige")
            return self.df, initial_row, total_row, duplicat_row, drop_row, duplicat_data, drop_data

        self.__class__.logger.info("Datenanzeige")
        return self.df, total_row, duplicat_row, drop_row

    def correlation_cost_living_rent(self, continent=None):
        """
        Corelatia dintre Cost of Living Index si Rent Index
        :param continent: None | Str
        :return: dataframe | str
        """
        cleaned_data = self.clean_data_duplicat_drop()[0]  # Die bereinigten Daten

        # Wenn cleaned_data ein DataFrame ist
        if isinstance(cleaned_data, pd.DataFrame):

            # Anzeigen nur der Spalten mit den erforderlichen Daten
            cleaned_data =  cleaned_data[['Country','Cost of Living Index', 'Rent Index','Continent']]

            # Daten nach Kontinent filtern, wenn angegeben
            if continent:
                cleaned_data = cleaned_data[(cleaned_data['Continent'] == continent)]

            # Sortierung basierend auf dem Cost of Living Index in absteigender Reihenfolge
            cleaned_data = cleaned_data.sort_values(by = "Cost of Living Index", ascending = False)

            cleaned_data.reset_index(drop=True, inplace=True) # Löschen des Index
            cleaned_data.index += 1  # Hinzufügen eines Index von Nummer 1

            self.__class__.logger.info("Datenbereinigung")
            return cleaned_data
        else:
            self.__class__.logger.error("Es ist kein gültiges DataFrame. Die Daten sind nicht bereinigbar.")
            return "Es ist kein gültiges DataFrame."


    def __str__(self):
        """
        Zeige Informationen aus der Datenbank an, d.h. die Gesamtzahl der Länder und
        wie viele Variablen berechnet wurden.
        :return:
        """
        return f"Das Objekt CostOfLiving mit {len(self.df)} Ländern und {self.df.shape[1]} Variablen"


# obj = CostOfLiving()  # Objekt erstellen
#
# # Die Kontinente, die hinzugefügt werden.
# file_name = 'Cost_of_Living_Index_by_Country_2024.csv'
# info_continent = obj.add_country()
# print("Kontinent zum CSV hinzufügen:",info_continent)
#
#
# # Alle Daten werden in CSV gespeichert.
# save_continent = CostOfLiving.save_country_to_csv(info_continent, file_name)
# print("Kontinent gespeichert:", save_continent)
#
#
# # Erstellen Sie ein Objekt mit den Top 10 Ländern nach Lebenshaltungskosten.
# percents_cost_of_living = 70
# top_10_cost_c = obj.top_10_high_cost_country(percents_cost_of_living)
# print("Top 10 der Länder mit den höchsten Lebenshaltungskosten:", top_10_cost_c[1])
# top_10_cost_living = top_10_cost_c[0]
#
# # Überprüfen, ob es sich um ein DataFrame handelt.
# if isinstance(top_10_cost_living, pd.DataFrame):
#     # Erstellen eines Objekts zum Speichern von Daten
#     save_top_10_cost_c = obj.save_file(top_10_cost_living, top_10_cost_c[1])
#     print("In Datei speichern: ", save_top_10_cost_c[1])
#
#
# # Generierung von Daten für Korrelation
# clean = obj.clean_data_duplicat_drop(verbose=True)
# continent_selected = "Africa"
# # Zeige das DataFrame basierend auf dem ausgewählten Land, falls gewünscht.
# correlation = obj.correlation_cost_living_rent(continent_selected)
# print(correlation)
#
# # Daten speichern
# save_correlation = obj.save_file(correlation, continent_selected)
# print(save_correlation[1])