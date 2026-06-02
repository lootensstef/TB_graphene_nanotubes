import numpy as np


def nanotube_gammas(n, m):
    """This function constructs the nanotube gamma points positions in reciprocal space, given the nanotube type (n,m)

    Parameters:
        n (integer): coefficient of the a_1 graphene primitive lattice vector in the chiral vector c_h
        m (integer): coefficient of the a_2 graphene primitive lattice vector in the chiral vector c_h

    Returns:
        k_gamma (1D array): the gamma point coordinates (for j=1)
        j_range (1D array): array of coefficients that are allowed to multiply k_gamma to find the gamma points"""

    d_r = np.gcd(n + 2 * m, 2 * n + m)
    q = int(2 * (n**2 + m**2 + n * m) / d_r)
    k_b1 = (2 * n + m) / (q * d_r)
    k_b2 = (n + 2 * m) / (q * d_r)

    k_gamma = np.array([k_b1, k_b2])
    j_range = np.linspace(int(-q / 2), int(q / 2 - 1), q)

    return k_gamma, j_range


def nanotube_kz(n, m):
    """This function constructs the reciprocal space k_z vector in relative coordinates, given the nanotube type (n,m)

    Parameters:
        n (integer): coefficient of the a_1 graphene primitive lattice vector in the chiral vector c_h
        m (integer): coefficient of the a_2 graphene primitive lattice vector in the chiral vector c_h

    Returns:
        k_z (1D array): vector with the direction of the 1D Brillouin lines, and half their length as magnitude"""

    d_r = np.gcd(n + 2 * m, 2 * n + m)
    q = int(2 * (n**2 + m**2 + n * m) / d_r)
    k_z = np.array([m / (2 * q), -n / (2 * q)])

    return k_z


def nanotube_symmetryline(k_gamma, k_z, j, N):
    """This function builds the j-th 1D nanotube Brillouin zone projection onto the graphene 2D Brillouin zone

    Parameters:
        k_gamma (1D array): the center point of the line, also called gamma point
        k_z (1D array): vector with the direction of the line and half its length
        j (integer): the j_th line
        N (integer): Number of points for the line. Affects bands smoothness, bandgap accuracy and calculation speeds.

    Returns:
    gamma_to_x (2, N array): array encoding a discretized version of the j-th reciprocal space line"""

    gamma_to_x = np.array([np.linspace(j *
                                       k_gamma[0], j *
                                       k_gamma[0] +
                                       k_z[0], N), np.linspace(j *
                                                               k_gamma[1], j *
                                                               k_gamma[1] +
                                                               k_z[1], N)])

    return gamma_to_x
