import numpy as np
import tb_simple_nn

def test_bandfunc_is_zero_at_k_point():
    """This function tests if f_k evaluated close to the K symmetry point is close to zero, as it should

    GIVEN: a known K symmetry point input
    WHEN: bandfunc is evaluated at K
    THEN: output must be close to zero
    """
    k_b1=2/3
    k_b2=1/3

    assert np.isclose(tb_simple_nn.bandfunc(k_b1,k_b2),0)

def test_bandfunc_reasonable_limits_precision():
    """This function tests that the errors of the cosines are small
    
    GIVEN: arrays of k_b1 and k_b2 imputs
    WHEN: f_k is calculated for each of those
    THEN: cosine sum errors are less than 0.1
    """

    k_b1=np.linspace(0,1,100)
    k_b2=np.linspace(-0.5,0.5,100)

    assert np.all(tb_simple_nn.bandfunc(k_b1,k_b2)>-0.1)
    assert np.all(tb_simple_nn.bandfunc(k_b1,k_b2)<9.1)


def test_eigenvals_stability():
    """This function tests the stability of the eigenvals function for extreme (even technically not possible) f(k) inputs

    GIVEN: extreme f(k) values
    WHEN: eigenvalues are computed
    THEN: no invalid or infinite values appear
    """

    f_k = np.array([0, 1e6, 1e-9, 10])

    E_p, E_m = tb_simple_nn.eigenvals(f_k, 0.0, -2.75, 0.05)

    assert np.all(np.isfinite(E_p))
    assert np.all(np.isfinite(E_m))

def test_eigenvals_ordering():
    """This function tests that the positive band values are always greater or equal to the negative band values

    GIVEN: any valid f(k)
    WHEN: eigenvalues are computed
    THEN: E_p is always >= E_m
    """

    f_k = np.linspace(0, 9, 100)

    E_p, E_m = tb_simple_nn.eigenvals(f_k, 0.0, -2.75, 0.05)

    assert np.all(E_p >= E_m)

def test_eigenvals_bandgap_approximation():
    """This function tests that the energy bands close to the K points have a reasonably small gap

    GIVEN: k points near symmetry (small variation)
    WHEN: tight-binding energies are computed
    THEN: band separation is small
    """

    k1 = np.linspace(0.663, 0.669, 50)
    k2 = np.linspace(0.330, 0.336, 50)

    f_k = tb_simple_nn.bandfunc(k1, k2)

    E_p, E_m = tb_simple_nn.eigenvals(f_k, 0.0, -2.75, 0.05)

    gap_estimate = np.max(E_p - E_m)

    assert gap_estimate < (10/50)