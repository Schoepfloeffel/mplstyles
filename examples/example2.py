#### Example 2: Use seaborn calls to plot, and setting the style over pyplot permanently

import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    style_list = [
        "https://raw.githubusercontent.com/Schoepfloeffel/mplstyles/main/schoepfloeffel_style_1.mplstyle"
    ]

    # Load dataset from seaborn
    flights = sns.load_dataset("flights")
    flights_wide = flights.pivot(
        index="year", columns="month", values="passengers"
    )

    # Plot default
    sns.reset_orig()
    default_fig = sns.catplot(data=flights_wide, kind="box")

    # Use the style sheet and plot with sns module
    for style_label in style_list:
        plt.style.use(style_label)
        sns.catplot(data=flights_wide, kind="box")
