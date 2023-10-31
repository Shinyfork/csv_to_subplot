import matplotlib.pyplot as plt
import pandas as pd

def create_subplots(data_file='Auswertung.csv', output_file='subplot_plots.pdf'):

    data = pd.read_csv(data_file, delimiter='\t', decimal=',', encoding='ANSI', converters={'Zeitstempel': str})
    # Create subplots
    fig, axs = plt.subplots(5, 1, figsize=(10, 12))

    # Plot %*bar
    axs[0].plot(data['Zeitstempel'], data['%*bar'], label="HACH-Messung")
    axs[0].set_title('HACH Messsignal')
    axs[0].set_ylabel('% V*bar')

    # Plot %
    axs[1].plot(data['Zeitstempel'], data['%'], label='HACH-Messung, normiert')
    axs[1].set_title('HACH-Messung, normiert')
    axs[1].set_ylabel('%')
    axs[1].axhline(y=1, color='red', linestyle='--', label='1%')
    axs[1].axhline(y=2, color='blue', linestyle='--', label='2%')
    axs[1].axhline(y=5, color='green', linestyle='--', label='5%')

    # Plot Druck
    axs[2].plot(data['Zeitstempel'], data['Druck'], label='Druckmessung')
    axs[2].set_title('Druckmessung')
    axs[2].set_ylabel('P [Bar abs.]')


    # Plot mV
    axs[3].plot(data['Zeitstempel'], data['mV'], label='S4-008 Rohsignal')
    axs[3].set_title('S4-008 Rohsignal')
    axs[3].set_ylabel('mV')

    # Plot Temp
    axs[4].plot(data['Zeitstempel'], data['Temp'], label='Temperatur')
    axs[4].set_title('Temperatur')
    axs[4].set_ylabel('°C')

    for ax in axs:
        ax.set_xticks([])

        ax.legend()


    plt.tight_layout()


    plt.savefig(output_file)

