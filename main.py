import pandas as pd


df_a = pd.read_csv("Inbetriebnahme.csv", sep="\t", decimal=",", encoding="ANSI",converters={"Zeit":str,"Datum":str})
df_b = pd.read_csv("CAL-Messung.csv", sep="\t", decimal=",",encoding="ANSI",converters={"Zeit":str,"Datum":str})


df_a["Druck"] = float("NaN")
df_a["Temp"] = float("NaN")
df_a["sep"] = " "
df_b["sep"] = " "

df_a["Zeitstempel"] = pd.to_datetime(df_a["Datum"] + df_a["sep"] + df_a["Zeit"], format="%d.%m.%Y %H:%M:%S")
df_b["Zeitstempel"] = pd.to_datetime(df_b["Datum"] + df_b["sep"] + df_b["Zeit"], format="%d.%m.%Y %H:%M:%S")
df_b["Zeitstempel"] -= pd.Timedelta("01:03:00")

# Schleife über die Zeilen von df_a
for i_a in range(len(df_a)):

    print(f"% Complete: {i_a/len(df_a)}", end="\r")

    ts_a = df_a["Zeitstempel"].iloc[i_a]
    t_diff_min = 1000000000
    i_min = -1

    # Schleife über die Zeilen von df_b
    for i_b in range(len(df_b)):
        ts_b = df_b["Zeitstempel"].iloc[i_b]
        tdiff = abs((ts_a - ts_b).total_seconds())

        if tdiff < t_diff_min:
            t_diff_min = tdiff
            i_min = i_b

        else:
            break

    # Aktualisieren Sie df_a mit den Werten aus df_b
    df_a.at[i_a, "Druck"] = df_b.at[i_min, "bar abs"]
    df_a.at[i_a, "Temp"] = df_b.at[i_min, "°C"]
    df_a.at[i_a, "S4-008"] = df_b.at[i_min, "mV"]


print(df_a)

df_a["%"] = df_a["%*bar"] / df_a["Druck"]




df_a.to_csv("Auswertung.csv", sep="\t", decimal=",", encoding="ANSI", index=False)

import subplot_creator


subplot_creator.create_subplots(data_file='Auswertung.csv', output_file='subplot_plots.pdf')

