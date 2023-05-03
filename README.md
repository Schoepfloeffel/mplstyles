# mplstyles
Collection of customized [Matplotlib](http://matplotlib.org) style sheets (.mplstyle).

## Usage
As simple as possible! :paintbrush:
Just provide the github link to the raw .mplstyle file. Matplotlib and corresponding wrappers are taking care of parsing and setting your rcParams.

```sh
import matplotlib.pyplot as plt
matplotlib.style.use("https://raw.githubusercontent.com/Schoepfloeffel/mplstyles/main/schoepfloeffel_style_1.mplstyle") #rcParams are set
matplotlib.pyplot.plot([1, 2, 3], [1, 2, 3])
```

## :sparkles: Overview of style sheets

1. 'schoepfloeffel_style_1.mplstyle'

![schoepfloeffel_style_1](./examples/png/schoepfloeffel_style_1.png) 
  
More to come soon.


## Example
See 'example' folder for minimal examples how styles can be selected (matplotlib, pyplot, seaborn, contextmanager). In general, there are many entry points to set a style. Under the hood the 'rcParams' are set temporarily/permanently and will be evaulated during the plot rendering.


## References
More details about customizing and .mplstyles: [Customizing matplotlib plots](https://matplotlib.org/users/customizing.html).

