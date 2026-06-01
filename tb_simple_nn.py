import numpy as np

def bandfunc(k_b1, k_b2):
    """This function returns the f(k) values that are used inside the energy eigenvalues formula. Relative coordinates are used because they lead to the simplest form of calculations.

    Parameters:
        k_b1 (float): component (relative coordinate) of k along the reciprocal lattice vector b1
        k_b2 (float): component (relative coordinate) of k along the reciprocal lattice vector b2
    
    Returns:
        f_k (float): bandfunction value for the k vector provided in input"""
    
    k_b1 = np.asarray(k_b1)
    k_b2 = np.asarray(k_b2)
    
    f_k=3+2*np.cos(2*np.pi*k_b1)+2*np.cos(2*np.pi*k_b2)+2*np.cos(2*np.pi*(k_b1-k_b2))

    return f_k


def eigenvals(f_k, eps2p, gamma_0, s_0):
    """This function calculates the two energy bands for a given k point in reciprocal space and tight-binding parameters
    
    Parameters:
        f_k (float): f(k) oscillating values calculated by the function "bandfunc for the wave vector k"
        eps2p (float): energy of the single isolated orbital (or self overlap)
        gamma_0 (float): nearest neighbour energy overlap 
        s_0 (float): nearest neighbour overlap constant

    Default values:
        eps2p, gamma_0, s_0: taken from empirical best fits (see documentation for more info)

    Returns:
        E_p, E_m (floats): the two pi-band energy eigenvalues for the wave vector k"""
    
    safe_sqrt_f=np.sqrt(np.clip(f_k, 0, None))

    denom_p = 1 - s_0 * safe_sqrt_f
    denom_m = 1 + s_0 * safe_sqrt_f

    E_p=(eps2p-gamma_0*safe_sqrt_f)/(denom_p)
    E_m=(eps2p+gamma_0*safe_sqrt_f)/(denom_m)

    return E_p, E_m