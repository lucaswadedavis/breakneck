# simple 4 step calculation
# step 1: how much energy (and as a consequence, how big a rocket) would be needed to push Phobos into Mars
## I'm really interested in using astropy for this, but I actually think their use-case is a bit more thourough than I have need of - at least for the initial de-orbiting phase
phobos = {
    'mass' : 1.0659e16, #kg
    'apoapsis' : 9517.58, #km
    'periapsis' : 9234.42, #km
    'orbital_speed' : 2.138 #km/s
    }

def deorbit (asteroid):
    #takes an asteroid (phobos or deimos) and returns the power necessary to deorbit the thing
    #what is the orbital speed necessary to keep phobos in orbit?
    #constraint: orbit degredation should be precipitous - no more than 100 days
    #just a test to make sure everything's working
    print asteroid['mass']

deorbit(phobos)

# step 2: how much ejecta would be produced by a hit from the asteroid
def impact (asteroid,velocity):
    #takes an asteroid and a velocity upon impact, and returns overall mass of ejecta
    #footnote: the impact itself should heat the atmosphere by some amount, choosing the right target (Olympus Mons? The South Pole?) may change things - but I've now idea how.
    #footnote: Keep in mind, the atmospheric heating post-impact will be mediated by the thermal conductance of the Martian atmosphere, and it may be the case that localized effects are so prounounced a target close to a large deposit of CO2 and H2O may be especially useful.
    print asteroid['mass'] * velocity

impact(phobos, 1000)

# step 3: how much would that ejecta falling back to the Martian surface heat the atmosphere
def skyfall (mass):
    #assume a power law distribution of ejecta sizes
    #figure out what fraction of the mass ejected escapes Mars altogether, and if there's a significant difference in the return-times of the ejected bodies.
    #the amount of atmospheric heating is the sum of the heat exchanged by all falling bodies
    #the heat produced by a given body is a consequence of it's velocity and surface area and the density of the Martian atmosphere
    #it will probably be good to make a subroutine to handle a single body
    #keep in mind that as the incoming meteors ablate they lose mass and surface area
    print mass

# step 4: how much (and for how long) would the atmosphere need to be heated in order to sublimate a sufficient amount of the frozen CO2 and H2O in order to create a self-sustaining, thick, warm Martian atmosphere.

