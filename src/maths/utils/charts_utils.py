from matplotlib import pyplot as plt
import itertools


class Chart:
    def __init__(self, title, xlabel, ylabel):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot(self, nb_plots, list_xvalues, list_yvalues, list_labels):
        plt.figure(figsize=(15, 9))
        for i, j, k, l in itertools.zip_longest(range(nb_plots - 1), range(nb_plots), range(nb_plots), range(nb_plots), fillvalue=""):
            plt.plot(list_xvalues[j], list_yvalues[k], label=list_labels[l])

        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.grid()
        #plt.savefig(self.path)
        plt.show()