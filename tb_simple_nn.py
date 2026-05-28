import numpy as np

def bandfunc(k_b1, k_b2):
    """This function returns the f(k) values that are used inside the energy eigenvalues formula. Relative coordinates are used because they lead to the simplest form of calculations.

    Parameters:
        k_b1: component (relative coordinate) of k along the reciprocal lattice vector b1
        k_b2: component (relative coordinate) of k along the reciprocal lattice vector b2
    
    Returns:
        f(k)=3+2cos(2pi*k_b1)+2cos(2pi*k_b1)+2cos[2pi*(k_b1-k_b2)]

    Raise:
        ValueError if the resulting value is <0 or >9"""
    
    f_k=3+2*np.cos(2*np.pi*k_b1)+2*np.cos(2*np.pi*k_b2)+2*np.cos(2*np.pi*(k_b1-k_b2))

    return f_k


def eigenvals(f_k, eps2p=0, gamma_0=-2.75, s_0=0.05):
    """This function calculates the two energy bands for a given k point in reciprocal space and tight-binding parameters
    
    Parameters:
        f_k: f(k) oscillating values calculated by the function "bandfunc"
        eps2p: energy of the single isolated orbital (or self overlap)
        gamma_0: nearest neighbour energy overlap 
        s_0: nearest neighbour overlap constant

        default values are taken from empirical best fits

    Returns:
        E_+(k), E_-(k): the two energy eigenvalues

    Raise: 
        InputError if f_k<0: we should be dealing with real numbers"""
    
    safe_sqrt_f=np.sqrt(np.clip(f_k, 0, None))
    E_p=(eps2p-gamma_0*safe_sqrt_f)/(1-s_0*safe_sqrt_f)
    E_m=(eps2p+gamma_0*safe_sqrt_f)/(1+s_0*safe_sqrt_f)

    return E_p, E_m