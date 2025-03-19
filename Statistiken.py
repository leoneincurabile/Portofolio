import os.path

import pandas as pd

class CostOfLiving:
    def __init__(self):
        """
        Inițializează obiectul și încarcă datele dintr-un fișier CSV.
        """
        pd.set_option('display.max_columns', None, 'display.max_rows', None)
        self.folder_path = 'daten'

        try:
            self.df = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')
        except FileNotFoundError:
            print("Fișierul nu a fost găsit!")
            self.df = None
        except pd.errors.ParserError:
            print("Eroare în formatul fișierului CSV! Asigură-te că este bine formatat.")
            self.df = None
        except Exception as e:
            print(f"Error {str(e)}")
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
        Verifica daca exista directorul respectiv, daca nu, il creaza
        :return: True sau error - statusul directorului
        """
        try:
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path, mode=0o777)
        except Exception as e:
            return f"Eroare {e}"

        return True

    def add_country(self):
        """
        Adauga series.pandas cu Continentele pentru a putea fi adaugate in csv
        :return: dataframe cu informatiile care se adauga in csv
        """
        try:
            self.df['Continent'] = self.df['Country'].map(self.continent_mapping)

            # Verificăm dacă există țări care nu au fost mapate
            if self.df['Continent'].isnull().any():
                missing_continents = self.df[self.df['Continent'].isnull()]['Country']
                return f"Țările fără continent atribuit: {missing_continents.tolist()}"

            return self.df
        except KeyError:
            return "Eroare: O țară nu există în mapa 'continent_mapping'."
        except Exception as e:
            return f"Eroare necunoscută: {e}"

    @staticmethod
    def save_country_to_csv(file_c_save:pd.DataFrame, file_name_c_save:str):
        """
        Salveaza datele din fine_c_name in csv
        :param file_c_save: (Dataframe) Toate datele care se introduc in csv
        :param file_name_c_save: (str) Nume fisier
        :return: (str) statusul procesului de salvare a Continentelor
        """

        try:
            file_c_save.to_csv(file_name_c_save, mode='w', header=True, index=False)
            return f"Datele cu Continent au fost adaugate in fisierul {file_name_c_save}"
        except AttributeError:
            return f"Nu exista Tara pentru Continentul asociat"
        except Exception as e:
            return f"Error {str(e)}"

    def top_10_high_cost_country(self, cost_of_living:int):
        """
        Afiseaza top 10 tari, cu continente si Cost_of_Living, sortat dupa Cost_of_Living
        :param cost_of_living: int - valoarea minimă a Cost of Living Index
        :return: tuple (DataFrame sau None, str) - un tuple care conține un DataFrame cu top 10 țări și un string cu numele fișierului
        """

        if not isinstance(cost_of_living, int):
            return None, f"Cost of living trebuie să fie un număr întreg!"

        if not isinstance(self.df, pd.DataFrame):
            return None, f"Trebuie un Dataframe"

        self.df['Cost of Living Index'] = pd.to_numeric(self.df['Cost of Living Index'], errors='coerce')
        if self.df['Cost of Living Index'].isnull().any():
            return ValueError, f"Lipsesc valori pentru Cost of Living Index"

        # selectam Continent, Country, Cost of Living Index, unde Cost of Living Index este mai mare decat cel cerut
        high_cost = self.df[(self.df['Cost of Living Index'] > cost_of_living)][['Continent','Country',
                                                                                 'Cost of Living Index']]

        # sorteaza dupa Cost of Liging Index descrescator si selecteaza doar primele 10
        high_cost = high_cost.sort_values(by='Cost of Living Index', ascending=False).head(10)

        # resetam indexul si incepem de la 1
        high_cost.reset_index(drop=True, inplace = True)
        high_cost.index +=1

        return high_cost, 'top 10 high cost country.csv'

    def save_file(self, file_data : pd.DataFrame, file_name_saved:str):
        """
        Salveaza fisierul cu datele incarcate. Trebuie sa contina prima data un dataframe, si pe urma numele fisierului
        :param file_data: dataframe - toate datele care se introduc in csv
        :param file_name_saved: str - numele fisierului de tip .csv
        :return: tuple (bool, str) - statusul salvarii fisierului
        """
        file_path = ''
        if self.dir_check() is True:
            current_dir = os.getcwd() # directorul curent
            file_path = os.path.join(current_dir, self.folder_path, file_name_saved)

        if not isinstance(file_name_saved, str):
            return None, "Numele fisier incorect"

        if not isinstance(file_data, pd.DataFrame):
            if ValueError:
                return None, "Lipsesc Date Din table"

        f_nan = file_data.isna().any()
        if True in f_nan.values:
            return None, "Lipsesc date importante din table!"

        if file_path:
            try:
                file_data.to_csv(file_path, index=True, index_label="Index")
                return True, f"Fisier salvat cu denumirea: {file_name_saved}"
            except Exception as e:
                 return False, f"Error ocurred {str(e)}"
        else:
            return False, f"Directorul nu a fost creat sau nu este valid"

    def __str__(self):
        """
        Afiseaza informatii legat din baza de date, adica nr total de tari si cate variabile sunt calculate
        :return:
        """
        return f"Objectul CostOfLiving cu {len(self.df)} tari si {self.df.shape[1]} variabile"


obj = CostOfLiving()  # creare obiect

# continentele care se vor adauga
info_continent = obj.add_country()
#print("Continent add to csv: ", info_continent)

file_name = 'Cost_of_Living_Index_by_Country_2024.csv'
# toate datele se salveaza in csv
save_continent = CostOfLiving.save_country_to_csv(info_continent, file_name)
print("Continent Saved: ", save_continent)

percents_cost_of_living = 70
# creare obiect cu top 10 Cost Country Living
top_10_cost_c = obj.top_10_high_cost_country(percents_cost_of_living)
#print("Top 10 hight cost country: ", top_10_cost_c)

# creare obiect pentru salvare date
save_top_10_cost_c = obj.save_file(top_10_cost_c[0], top_10_cost_c[1])
print("Save to file: ", save_top_10_cost_c[1])

