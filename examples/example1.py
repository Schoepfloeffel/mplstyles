#### Example 1: Uses matplotlib.pyplot and applies each style to a demonstration figure consisting of multiple artists

import matplotlib.pyplot as plt
from style_sheets_reference_func import plot_figure

if __name__ == "__main__":

    plt.style.use("default")  # reset to default first

    style_list = [
        "https://raw.githubusercontent.com/Schoepfloeffel/mplstyles/main/schoepfloeffel_style_1.mplstyle",
        "https://raw.githubusercontent.com/Schoepfloeffel/mplstyles/main/schoepfloeffel_style_2.mplstyle",
    ]

    # Plot a demonstration figure
    for style_label in style_list:
        with plt.rc_context({"figure.max_open_warning": len(style_list)}):
            with plt.style.context(style_label):
                plot_figure(style_label=style_label)
    plt.show()
