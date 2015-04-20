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

# step 3: how much would that ejecta falling back to the Martian surface heat the atmosphere

# step 4: how much (and for how long) would the atmosphere need to be heated in order to sublimate a sufficient amount of the frozen CO2 and H2O in order to create a self-sustaining, thick, warm Martian atmosphere.

