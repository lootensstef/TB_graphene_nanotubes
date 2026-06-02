import numpy as np

import graphene_space #Reciprocal space lines construction for graphene
import nanotube_space #Reciprocal space lines construction for nanotubes
import tb_simple_nn #Nearest neighbour tight-binding model used for the calculations


def simulate_energybands(input_material, input_n, input_m, input_precision, input_eps2p, input_gamma_0, input_s_0):
    """This function simulates the energy bands of the selected material using its reciprocal space lines defined in (material)_space.py and the nearest neighbour tight-binding model defined in tb_simple_nn.py
    
    Parameters:
        material (string): the type of material to simulate, see material_selector()
        input_n, input_m (integers): the type of nanotube to simulate, see material_selector()
        precision (integer): a parameter of precision for the simulation, in this case the number of points per reciprocal line, taken from precision_selector()

    Returns:
        k_band (1D array): represents all the data points on the x axis. Their values are constructed for the purposes of easy plotting and labelling and don't retain a consistent physical meaning
        e_p_band, e_m_band (1D arrays): concatenated arrays of energy values (eV). 
            Graphene: the concatenation happens along 3 different symmetry lines. 
            Nanotube: the concatenation happens between different 1D projection lines on the graphene 2D Brillouin zone.
    
    Raises:
        ValueError if somehow the input material is invalid
    
    """
    
    if input_material=="graphene":

        m_to_gamma, gamma_to_k, k_to_m=graphene_space.graphene_symmetrylines(input_precision)

        bandfunc_m_gamma=tb_simple_nn.bandfunc(m_to_gamma[0,:], m_to_gamma[1,:])
        bandfunc_gamma_k=tb_simple_nn.bandfunc(gamma_to_k[0,:], gamma_to_k[1,:])
        bandfunc_k_m=tb_simple_nn.bandfunc(k_to_m[0,:], k_to_m[1,:])

        e_p_mg, e_m_mg=tb_simple_nn.eigenvals(bandfunc_m_gamma, input_eps2p, input_gamma_0, input_s_0)
        e_p_gk, e_m_gk=tb_simple_nn.eigenvals(bandfunc_gamma_k, input_eps2p, input_gamma_0, input_s_0)
        e_p_km, e_m_km=tb_simple_nn.eigenvals(bandfunc_k_m, input_eps2p, input_gamma_0, input_s_0)

        k_band=np.linspace(0,3*input_precision-3,3*input_precision-2)
        e_p_band=np.concatenate((e_p_mg, e_p_gk[1:], e_p_km[1:]))
        e_m_band=np.concatenate((e_m_mg, e_m_gk[1:], e_m_km[1:]))

        e_p = np.asarray(e_p_band)
        e_m = np.asarray(e_m_band)

        cbm = np.min(e_p)
        vbm = np.max(e_m)

        Eg = cbm - vbm
        Eg = max(Eg, 0.0)

        print(f"Calculated bandgap={Eg:.3f} eV")

        return k_band, e_p_band, e_m_band
    
    if input_material=="nanotube":

        k_gamma, j_values=nanotube_space.nanotube_gammas(input_n,input_m)
        k_z=nanotube_space.nanotube_kz(input_n, input_m)

        temp_k_bands=[]
        temp_e_p_bands=[]
        temp_e_m_bands=[]

        for j in j_values:

            x_to_x=nanotube_space.nanotube_symmetryline(k_gamma, k_z, j, input_precision)

            bandfunc_x_x=tb_simple_nn.bandfunc(x_to_x[0, :], x_to_x[1, :])

            e_p_x_x, e_m_x_x=tb_simple_nn.eigenvals(bandfunc_x_x, input_eps2p, input_gamma_0, input_s_0)
            k_segment=np.linspace(0,1, input_precision)

            temp_k_bands.append(k_segment)
            temp_e_p_bands.append(e_p_x_x)
            temp_e_m_bands.append(e_m_x_x)

        k_bands=np.concatenate(temp_k_bands)
        e_p_bands=np.concatenate(temp_e_p_bands)
        e_m_bands=np.concatenate(temp_e_m_bands)

        e_p = np.asarray(e_p_bands)
        e_m = np.asarray(e_m_bands)

        cbm = np.min(e_p)
        vbm = np.max(e_m)

        Eg = cbm - vbm
        Eg = max(Eg, 0.0)

        print(f"Calculated bandgap={Eg:.3f} eV")


        return k_bands, e_p_bands, e_m_bands
    
    else:
        raise ValueError("input_material must be 'graphene' or 'nanotube'")
    




    