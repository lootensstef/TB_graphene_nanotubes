import numpy as np

def graphene_simmetrylines(N):
    """This function constructs the vectors of points along high simmetry lines inside the graphene brillouin zone, in relative coordinates for simplicity of calculations.
    
    Parameters:
        N: Number of points for each line. Affects calculated bands smoothness and calculation speeds.

    Raise:
        InputError if N<2 or not an integer: the band construction doesn't make sense for a number of points that's fractional or too low
    """

    M_Gamma=np.array([np.linspace(0.5,0,N),np.zeros(N)])
    Gamma_K=np.array([np.linspace(0,2/3,N),np.linspace(0,1/3,N)])

    return M_Gamma, Gamma_K