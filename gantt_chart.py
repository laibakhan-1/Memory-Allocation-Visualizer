import matplotlib.pyplot as plt

def draw_gantt_chart(chart, title="Gantt Chart"):
    fig, ax = plt.subplots(figsize=(10, 2))
    for task in chart:
        ax.broken_barh([(task[1], task[2]-task[1])], (10, 9), facecolors=('tab:blue'))
        ax.text(task[1] + (task[2]-task[1])/2 - 0.3, 14, task[0])
    ax.set_ylim(5, 35)
    ax.set_xlim(0, max(t[2] for t in chart) + 2)
    ax.set_xlabel('Time')
    ax.set_yticks([])
    ax.set_title(title)
    plt.savefig('output_graphs/gantt_chart.png')
    plt.show()
