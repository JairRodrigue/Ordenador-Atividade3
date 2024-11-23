import matplotlib.pyplot as plt
import numpy as np

# Dados
labels = ['Python', 'JavaScript']

# Bubble Sort
bubble_sort_tempo_media = [21754.63, 1137.62]
bubble_sort_tempo_mediana = [21764.50, 1135.00]
bubble_sort_memoria_media = [15920.80, 6403.91]
bubble_sort_memoria_mediana = [15952.00, 6412.31]

# Merge Sort
merge_sort_tempo_media = [40.20, 20.20]
merge_sort_tempo_mediana = [40.08, 19.46]
merge_sort_memoria_media = [15119.25, 8808.53]
merge_sort_memoria_mediana = [16508.00, 8782.91]

# Função para plotar gráficos
def plot_bar_chart(title, y_data, ylabel, ylim=None):
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x - width/2, y_data['bubble'], width, label='Bubble Sort')
    ax.bar(x + width/2, y_data['merge'], width, label='Merge Sort')

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    if ylim:
        ax.set_ylim(ylim)

    plt.tight_layout()
    plt.show()

# Plotando os gráficos
plot_bar_chart(
    "Média do Tempo (ms)",
    {'bubble': bubble_sort_tempo_media, 'merge': merge_sort_tempo_media},
    "Tempo (ms)"
)

plot_bar_chart(
    "Mediana do Tempo (ms)",
    {'bubble': bubble_sort_tempo_mediana, 'merge': merge_sort_tempo_mediana},
    "Tempo (ms)"
)

plot_bar_chart(
    "Média da Memória (KB)",
    {'bubble': bubble_sort_memoria_media, 'merge': merge_sort_memoria_media},
    "Memória (KB)"
)

plot_bar_chart(
    "Mediana da Memória (KB)",
    {'bubble': bubble_sort_memoria_mediana, 'merge': merge_sort_memoria_mediana},
    "Memória (KB)"
)
