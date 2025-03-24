import os.path

import pandas as pd

class CostOfLiving:
    def __init__(self):
        """
        Initialisiere das Objekt und ladet die Daten aus einer CSV-Datei.
        """
        pd.set_option('display.max_columns', None, 'display.max_rows', None)
        self.folder_path = 'daten'

        try:
            self.df = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')
        except FileNotFoundError:
            print("Die Datei wurde nicht gefunden.")
            self.df = None
        except pd.errors.ParserError:
            print("Fehler im CSV-Dateiformat! Bitte stelle sicher, dass es korrekt formatiert ist.")
            self.df = None
        except Exception as e:
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
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path, mode=0o777)
        except Exception as e:
            return f"Fehler {e}"

        return True

    def add_country(self):
        """
        Fügen Sie die pandas.series mit den Kontinenten hinzu, damit sie in die CSV-Datei aufgenommen werden können
        :return: Dataframe mit den Informationen, die in die CSV-Datei hinzufügt werden
        """
        try:
            self.df['Continent'] = self.df['Country'].map(self.continent_mapping)

            # Verificăm dacă există țări care nu au fost mapate
            if self.df['Continent'].isnull().any():
                missing_continents = self.df[self.df['Continent'].isnull()]['Country']
                return f"Länder ohne zugewiesenen Kontinent: {missing_continents.tolist()}"

            return self.df
        except KeyError:
            return "Fehler: Ein Land existiert nicht in der Mappe 'continent_mapping'."
        except Exception as e:
            return f"Unbekannter Fehler: {e}"

    @staticmethod
    def save_country_to_csv(file_c_save:pd.DataFrame, file_name_c_save:str):
        """
        Speichere die Daten aus fine_c_name in einer CSV-Datei.
        :param file_c_save: (Dataframe) Alle Daten, die in die CSV-Datei eingetragen werden.
        :param file_name_c_save: (str) Der Dateiname
        :return: (str) der Status des Speichervorgangs der Kontinente
        """

        try:
            file_c_save.to_csv(file_name_c_save, mode='w', header=True, index=False)
            return f"Die Daten mit Kontinent wurden der Datei ({file_name_c_save}) hinzugefägt."
        except AttributeError:
            return f"Es gibt kein Land für den zugeordneten Kontinent."
        except Exception as e:
            return f"Fehler {str(e)}"

    def top_10_high_cost_country(self, cost_of_living:int):
        """
        Zeige die Top 10 Länder mit Kontinent und Lebenshaltungskosten, sortiert nach den Lebenshaltungskosten.
        :param cost_of_living: int - der minimale Wert des Lebenshaltungskostenindex.
        :return: tuple (DataFrame sau None, str) - ein Tupel, das ein DataFrame mit den Top 10 Ländern und
        einen String mit dem Dateinamen enthält.
        """

        if not isinstance(cost_of_living, int):
            return None, f"Die Lebenshaltungskosten müssen eine ganze Zahl sein!"

        if not isinstance(self.df, pd.DataFrame):
            return None, f"Es muss ein DataFrame sein."

        self.df['Cost of Living Index'] = pd.to_numeric(self.df['Cost of Living Index'], errors='coerce')
        if self.df['Cost of Living Index'].isnull().any():
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

        return high_cost, 'top 10 high cost country.csv'

    def save_file(self, file_data : pd.DataFrame, file_name_saved:str):
        """
        # Speichern Sie die Datei mit den geladenen Daten. Sie muss zuerst ein DataFrame und dann den Dateinamen enthalten.
        :param file_data: dataframe - alle Daten, die in die CSV-Datei eingefügt werden
        :param file_name_saved: str - der Dateiname der CSV-Datei
        :return: tuple (bool, str) - der Status des Speicherns der Datei
        """
        file_path = ''
        if self.dir_check() is True:
            current_dir = os.getcwd() # directorul curent
            file_path = os.path.join(current_dir, self.folder_path, file_name_saved)

        if not isinstance(file_name_saved, str):
            return None, "Falscher Dateiname"

        if not isinstance(file_data, pd.DataFrame):
            if ValueError:
                return None, "Fehlende Daten in der Tabelle"

        f_nan = file_data.isna().any()
        if True in f_nan.values:
            return None, "Wichtige Daten fehlen in der Tabelle!"

        if file_path:
            try:
                file_data.to_csv(file_path, index=True, index_label="Index")
                return True, f"Datei wurde unter dem Namen gespeichert: {file_name_saved}"
            except Exception as e:
                 return False, f"Fehler {str(e)}"
        else:
            return False, f"Das Verzeichnis wurde nicht erstellt oder ist ungültig."

    def __str__(self):
        """
        Zeige Informationen aus der Datenbank an, d.h. die Gesamtzahl der Länder und
        wie viele Variablen berechnet wurden.
        :return:
        """
        return f"Das Objekt CostOfLiving mit {len(self.df)} Ländern und {self.df.shape[1]} Variablen"


obj = CostOfLiving()  # Objekt erstellen

# Die Kontinente, die hinzugefügt werden.
# info_continent = obj.add_country()
# print("Kontinent zum CSV hinzufügen:", info_continent)

# file_name = 'Cost_of_Living_Index_by_Country_2024.csv'
# Alle Daten werden in CSV gespeichert.
# save_continent = CostOfLiving.save_country_to_csv(info_continent, file_name)
# print("Kontinent gespeichert:", save_continent)

# percents_cost_of_living = 70
# Erstellen Sie ein Objekt mit den Top 10 Ländern nach Lebenshaltungskosten.
# top_10_cost_c = obj.top_10_high_cost_country(percents_cost_of_living)
# print("Top 10 der Länder mit den höchsten Lebenshaltungskosten", top_10_cost_c)

# Erstellen eines Objekts zum Speichern von Daten
# save_top_10_cost_c = obj.save_file(top_10_cost_c[0], top_10_cost_c[1])
# print("In Datei speichern: ", save_top_10_cost_c[1])
