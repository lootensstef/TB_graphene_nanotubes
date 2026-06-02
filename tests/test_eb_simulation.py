import numpy as np
import eb_simulation
import nanotube_space
import pytest

def test_graphene_band_arrays_shape():
    """This function tests that simulate_energybands for graphene constructs arrays with the correct shape, later used in main.py for plotting
    GIVEN: a graphene simulation with precision N

    WHEN: simulate_energybands is called

    THEN: the returned arrays must all have the expected length 3*N - 2
    """

    N = 100

    k_band, e_p_band, e_m_band = eb_simulation.simulate_energybands("graphene",None,None,N,0.0,-2.75,0.05)

    expected_length = 3 * N - 2

    assert len(k_band) == expected_length
    assert len(e_p_band) == expected_length
    assert len(e_m_band) == expected_length

def test_graphene_band_arrays_valid_output():
    """This function tests that each element in the arrays constructed by simulate_energybands for graphene is valid and finite
    GIVEN: a graphene simulation with precision N

    WHEN: simulate_energybands is called

    THEN: all elements in the constructed arrays are valid numbers
    """

    N = 1000

    k_band, e_p_band, e_m_band = eb_simulation.simulate_energybands("graphene",None,None,N,0.0,-2.75,0.05)

    for band_array in [k_band, e_p_band, e_m_band]:
        assert np.all(np.isfinite(band_array))


def test_nanotube_band_arrays_shape():
    """This function tests that simulate_energybands for a nanotube constructs arrays with the correct shape, later used in main.py for plotting
    GIVEN: a graphene simulation with precision N

    WHEN: simulate_energybands is called

    THEN: the returned arrays must all have the expected length 3*N - 2
    """

    N = 100

    k_band, e_p_band, e_m_band = eb_simulation.simulate_energybands("nanotube",19,0,N,0.0,-2.75,0.05)

    _, j_range = nanotube_space.nanotube_gammas(19,0)

    assert len(k_band) == N*j_range.size
    assert len(e_p_band) == N*j_range.size
    assert len(e_m_band) == N*j_range.size


def test_nanotube_band_arrays_valid_output():
    """This function tests that each element in the arrays constructed by simulate_energybands for a nanotube is valid and finite
    GIVEN: a graphene simulation with precision N

    WHEN: simulate_energybands is called

    THEN: all elements in the constructed arrays are valid numbers
    """

    N = 100

    k_band, e_p_band, e_m_band = eb_simulation.simulate_energybands("nanotube",12,13,N,0.0,-2.75,0.05)

    for band_array in [k_band, e_p_band, e_m_band]:
        assert np.all(np.isfinite(band_array))


def test_invalid_material_raises_value_error():
    """This function checks that the simulate_energybands implementation correctly raises a ValueError when we give it an invalid material, like it should
    GIVEN: an invalid material name

    WHEN: simulate_energybands is called

    THEN: ValueError must be raised
    """

    with pytest.raises(ValueError):
        eb_simulation.simulate_energybands(
            "silicon",
            None,
            None,
            100,
            0.0,
            -2.75,
            0.05,
        )



def test_reasonable_zigzag_nanotubes_bandgap():
    """This function tests that the calculated band gap of theoretically expected metallic nanotubes is reasonably close to zero (the small error is because of discretization)

    GIVEN: metallic (zigzag) nanotube type and symmetry lines
    WHEN: discrete energy bands are constructed
    THEN: energy gap value is close to zero
    """

    n_zigzag=np.array([3,6,9,12,15,18])
    m_zigzag=0

    for n in n_zigzag:
        _, e_p_bands, e_m_bands=eb_simulation.simulate_energybands("nanotube", n,m_zigzag,1000,0,-2.75,0.05)
        assert np.isclose((np.min(e_p_bands)-np.max(e_m_bands)),0)

def test_reasonable_armchair_nanotubes_bandgap():
    """This function tests that the calculated band gap of theoretically expected metallic nanotubes is reasonably close to zero (the small error is because of discretization)

    GIVEN: metallic (armchair) nanotube type and symmetry lines
    WHEN: discrete energy bands are constructed
    THEN: energy gap value is close to zero
    """

    n_m_armchair=np.array([3,6,9,12,15,18])

    for n_m in n_m_armchair:
        _, e_p_bands, e_m_bands=eb_simulation.simulate_energybands("nanotube", n_m,n_m,1000,0,-2.75,0.05)
        assert np.isclose((np.min(e_p_bands)-np.max(e_m_bands)),0)

def test_reasonable_semiconducting_nanotubes_bandgap():
    """This function tests that the calculated band gap of theoretically expected semiconducting nanotubes is reasonably close to zero (the small error is because of discretization)

    GIVEN: semiconducting nanotube type and symmetry lines
    WHEN: discrete energy bands are constructed
    THEN: energy gap value is not close to zero
    """

    n_m_armchair=np.array([4,7,10,13,16,19])

    for n_m in n_m_armchair:
        _, e_p_bands, e_m_bands=eb_simulation.simulate_energybands("nanotube", n_m,n_m-1,1000,0,-2.75,0.05)
        assert not np.isclose((np.min(e_p_bands)-np.max(e_m_bands)),0)
