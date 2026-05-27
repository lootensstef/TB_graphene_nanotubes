import matplotlib.pyplot as plt
import eb_simulation #separate file that runs all the calculations and outputs the energy bands


def main():
    material, nt_n, nt_m = eb_simulation.material_selector()
    precision= eb_simulation.precision_selector()
    k_bands, e_p_bands, e_m_bands = eb_simulation.simulate_energybands(material, nt_n, nt_m, precision)

    #various pyplot graphic options
    plt.figure(figsize=(16,10), dpi=150)
    
    plt.plot(k_bands, e_p_bands, color="black", alpha=1, linewidth=3)
    plt.plot(k_bands, e_m_bands, color="black", alpha=1, linewidth=3)

    plt.show()










if __name__ == "__main__":
    main()