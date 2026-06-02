import numpy as np
import nanotube_space

def test_nanotube_k_shape():
    """This function tests the correct shape of the objects that nanotube_gammas and nanotube_kz produce

    GIVEN: a valid nanotube (n,m)
    WHEN: gamma point and j range are constructed
    THEN: k_gamma must be a 2-component vector and j_range a 1D array
    """

    n, m = 6, 4

    k_gamma, j_range = nanotube_space.nanotube_gammas(n, m)
    k_z=nanotube_space.nanotube_kz(n,m)

    assert k_gamma.shape == (2,)
    assert k_z.shape == (2,)
    assert isinstance(j_range, np.ndarray)

def test_nanotube_symmetryline_shape():
    """This function tests the correct shape of the objects that nanotube_symmetryline produces

    GIVEN: valid nanotube k_gamma, k_z and precision N
    WHEN: nanotube symmetry line is constructed
    THEN: the symmetry line must be a 2 dimensional array of N points
    """

    k_gamma_1, _ = nanotube_space.nanotube_gammas(4,4)
    k_gamma_2, _ = nanotube_space.nanotube_gammas(12,0)
    k_gamma_3, _ = nanotube_space.nanotube_gammas(0,16)

    k_z_1 = nanotube_space.nanotube_kz(4,4)
    k_z_2 = nanotube_space.nanotube_kz(12,0)
    k_z_3 = nanotube_space.nanotube_kz(0,16)
    
    gamma_to_x_1 = nanotube_space.nanotube_symmetryline(k_gamma_1,k_z_1,3,50)
    gamma_to_x_2 = nanotube_space.nanotube_symmetryline(k_gamma_2,k_z_2,3,50)
    gamma_to_x_3 = nanotube_space.nanotube_symmetryline(k_gamma_3,k_z_3,3,50)

    for line_array in [gamma_to_x_1,gamma_to_x_2,gamma_to_x_3]:
        assert line_array.shape == (2,50)

def test_nanotube_symmetrylines_valid_output():
    """This function tests that each element in the generated array is a finite and valid value

    GIVEN: nanotube symmetry line generation
    WHEN: lines are constructed
    THEN: no NaN or infinite values exist
    """

    k_gamma_1, _ = nanotube_space.nanotube_gammas(3,3)
    k_gamma_2, _ = nanotube_space.nanotube_gammas(19,0)
    k_gamma_3, _ = nanotube_space.nanotube_gammas(0,12)

    k_z_1 = nanotube_space.nanotube_kz(3,3)
    k_z_2 = nanotube_space.nanotube_kz(19,0)
    k_z_3 = nanotube_space.nanotube_kz(0,12)
    
    gamma_to_x_1 = nanotube_space.nanotube_symmetryline(k_gamma_1,k_z_1,2,50)
    gamma_to_x_2 = nanotube_space.nanotube_symmetryline(k_gamma_2,k_z_2,2,50)
    gamma_to_x_3 = nanotube_space.nanotube_symmetryline(k_gamma_3,k_z_3,2,50)
    

    for line_array in [gamma_to_x_1,gamma_to_x_2,gamma_to_x_3]:
        assert np.all(np.isfinite(line_array))

