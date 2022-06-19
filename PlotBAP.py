def plot_bap(x, fs):
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure(layout='constrained', figsize=plt.figaspect(1) * 1.5)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_xlabel('ITD [ms]', **dict(fontsize=14))

    X = np.linspace(-1, 1, x.shape[0])
    Y = np.linspace(0, 50, x.shape[1])
    x2, y2 = np.meshgrid(X, Y)
    z = x.T

    ax.plot_surface(x2, y2, z, cmap='viridis', rstride=1, cstride=1, linewidth=0, antialiased=False)
    ax.elev = 80
    ax.azim = -65

    plt.show()
