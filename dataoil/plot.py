# AUTOGENERATED! DO NOT EDIT! File to edit: plot.ipynb (unless otherwise specified).

__all__ = ['plot1', 'plotN', 'distplot']

# Cell
import matplotlib.pyplot as plt
import seaborn as sns

def plot1(x,y,figsize=(15,10),style='ggplot', title=None,label=None, xlabel=None, ylabel=None):
    "allow you to plot one curve. It uses matplotlib plot function. `x` and `y` are both 1D list"
    fig = plt.figure(figsize=figsize)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.style.use(style)
    plt.plot(x, y, label=label)
    plt.legend()
    plt.show()

def plotN(xs,ys,figsize=(15,10),style='ggplot', title=None,labels=None, xlabel=None, ylabel=None):
    "allow you to plot n curves on the same graph. It uses matplotlib plot function. `xs` and `ys` are both ND lists"
    fig = plt.figure(figsize=figsize)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.style.use(style)
    for x,y in zip(xs,ys):
        plt.plot(x, y)
    plt.legend(labels)
    plt.show()

def distplot(x,figsize=(15,10),style='ggplot', title=None):
    "allow you to plot the distribution of a random variable `x`"
    fig = plt.figure(figsize=figsize)
    plt.title(title)
    plt.style.use(style)
    sns.distplot(x)
    plt.show()