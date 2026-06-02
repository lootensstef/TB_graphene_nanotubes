import numpy as np
import graphene_space


def test_graphene_symmetrylines_shape():
    """This function tests that each symmetry line shape is correct, otherwise all the code that depends on this breaks

    GIVEN: a chosen precision N
    WHEN: graphene symmetry lines are generated
    THEN: each line has shape (2, N)
    """

    N = 20
    m_to_gamma, gamma_to_k, k_to_m = graphene_space.graphene_symmetrylines(N)

    assert m_to_gamma.shape == (2, N)
    assert gamma_to_k.shape == (2, N)
    assert k_to_m.shape == (2, N)


def test_graphene_symmetrylines_valid_output():
    """This function tests that each element in the generated arrays is a finite and valid value

    GIVEN: graphene symmetry line generation
    WHEN: lines are constructed
    THEN: no NaN or infinite values exist
    """

    N = 50
    m_to_gamma, gamma_to_k, k_to_m = graphene_space.graphene_symmetrylines(N)

    for line_array in [m_to_gamma, gamma_to_k, k_to_m]:
        assert np.all(np.isfinite(line_array))


def test_graphene_symmetrylines_endpoints():
    """This function tests that the endpoints of a symmetry line are close to the expected symmetry point coordinates

    GIVEN: graphene symmetry lines construction
    WHEN: N is small and endpoints are inspected
    THEN: endpoints match expected high-symmetry point coordinates
    """

    N = 5
    m_to_gamma, _, _ = graphene_space.graphene_symmetrylines(N)

    # M to Gamma path
    assert np.isclose(m_to_gamma[0, 0], 0.5)
    assert np.isclose(m_to_gamma[0, -1], 0.0)

    assert np.isclose(m_to_gamma[1, 0], 0.0)
    assert np.isclose(m_to_gamma[1, -1], 0.0)
