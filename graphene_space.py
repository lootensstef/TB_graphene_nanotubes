import numpy as np

def graphene_symmetrylines(N):
    """This function constructs the vectors of points along high simmetry lines inside the graphene brillouin zone, in relative coordinates for simplicity of calculations.
    
    Parameters:
        N: Number of points for each line. Affects calculated bands smoothness and calculation speeds.

    Returns:
    m_to_gamma, gamma_to_k, k_to_m: the segmented symmetry lines in reciprocal space, the names are self explanatory.
    
    Raises:
        InputError if N<2 or not an integer: the band construction doesn't make sense for a number of points that's fractional or too low
    """

    m_to_gamma=np.array([np.linspace(1/2,0,N),np.zeros(N)])
    gamma_to_k=np.array([np.linspace(0,2/3,N),np.linspace(0,1/3,N)])
    k_to_m=np.array([np.linspace(2/3,1/2,N),np.linspace(1/3,1/2,N)])

    return m_to_gamma, gamma_to_k, k_to_m