import numpy as np

def nanotube_gammas(n,m):
        """This function constructs the nanotube gamma points positions in reciprocal space, given the nanotube type (n,m)
        
        Parameters:
            n: integer coefficient of the a_1 graphene primitive lattice vector in the chiral vector c_h
            m: integer coefficient of the a_2 graphene primitive lattice vector in the chiral vector c_h

        Returns:
            k_gamma: the gamma point coordinates (for j=1)
            j_range: vector of coefficients that are allowed to multiply k_gamma to find the gamma points

        Raises:
        InputError if n, m are not integers greater than zero.
        
        """

        d_r=np.gcd(n+2*m, 2*n+m)
        q=int(2*(n**2+m**2+n*m)/d_r)
        k_b1=(2*n+m)/(q*d_r)
        k_b2=(n+2*m)/(q*d_r)

        k_gamma=np.array([k_b1, k_b2])
        j_range=np.linspace(int(-q/2), int(q/2-1), q)

        return k_gamma, j_range        
        

def nanotube_kz(n,m):
        """This function constructs the reciprocal space k_z vector in relative coordinates, given the nanotube type (n,m)
        
        Parameters:
            n: integer coefficient of the a_1 graphene primitive lattice vector in the chiral vector c_h
            m: integer coefficient of the a_2 graphene primitive lattice vector in the chiral vector c_h

        Returns:
            k_z: has the direction of the 1D Brillouin lines, and half their length as magnitude.

        Raises:
        InputError if n, m are not integers greater than zero.
        
        """

        d_r=np.gcd(n+2*m, 2*n+m)
        q=int(2*(n**2+m**2+n*m)/d_r)
        k_z=np.array([m/(2*q), -n/(2*q)])

        return k_z


def nanotube_symmetryline(k_gamma, k_z, j=0, N=2):
        """This function builds the j-th 1D nanotube Brillouin zone projection onto the graphene 2D Brillouin zone
        
        Parameters:
            k_gamma: the center point of the line, also called gamma point
            k_z: vector with the direction of the line and half its length
            j: the j_th line
            N: Number of points for the line. Affects calculated bands smoothness and calculation speeds.
        
        Returns:
        Numpy arrays encoding discretized versions of the lines in reciprocal space

        Raises:
        InputError if int(j)!=j, N<2, k_gamma outside the graphene brillouin zone.
        """
        
        
        x_to_gamma_to_x=np.array([np.linspace(j*k_gamma[0],j*k_gamma[0]+k_z[0], N), np.linspace(j*k_gamma[1],j*k_gamma[1]+k_z[1], N)])

        return x_to_gamma_to_x