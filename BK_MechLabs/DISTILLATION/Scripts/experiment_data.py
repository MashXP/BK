# Experimental data for Distillation Lab
# Update these values for new "number crunching"

# Define experiments as a list of dictionaries
# xf: feed mole fraction (ethanol)
# xd: distillate mole fraction (ethanol)
# xw: bottom mole fraction (ethanol)
# R: reflux ratio
# q: feed condition (1 for saturated liquid)

experiments = [
    {
        "id": 1,
        "location": 4,
        "xf": 0.0416,
        "xd": 0.242,
        "xw": 0.032,
        "R": 0.897,
        "q": 1.065
    },
    {
        "id": 2,
        "location": 4,
        "xf": 0.0416,
        "xd": 0.323,
        "xw": 0.016,
        "R": 0.956,
        "q": 1.063
    },
    {
        "id": 3,
        "location": 4,
        "xf": 0.0416,
        "xd": 0.242,
        "xw": 0.032,
        "R": 3.021,
        "q": 1.063
    },
    {
        "id": 4,
        "location": 2,
        "xf": 0.0416,
        "xd": 0.281,
        "xw": 0.016,
        "R": 1.567,
        "q": 1.069
    },
    {
        "id": 5,
        "location": 5,
        "xf": 0.0416,
        "xd": 0.281,
        "xw": 0.016,
        "R": 1.226,
        "q": 1.052
    }
]

# VLE data for Ethanol-Water at 1 atm (x, y mole fractions)
vle_x = [0, 0.019, 0.072, 0.097, 0.166, 0.235, 0.327, 0.397, 0.508, 0.573, 0.676, 0.747, 0.894, 1.0]
vle_y = [0, 0.170, 0.389, 0.437, 0.509, 0.544, 0.583, 0.612, 0.656, 0.684, 0.739, 0.781, 0.894, 1.0]
