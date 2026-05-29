import matplotlib.pyplot as plt
import eb_simulation #separate file that runs all the calculations and outputs the energy bands


def main():
    material, nt_n, nt_m = eb_simulation.material_selector()
    precision= eb_simulation.precision_selector()
    k_bands, e_p_bands, e_m_bands = eb_simulation.simulate_energybands(material, nt_n, nt_m, precision)

    #various pyplot graphic options
    plt.figure(figsize=(16,10), dpi=150)


    if material=="graphene":
        plt.plot(k_bands, e_p_bands, color="black", alpha=1, linewidth=1)
        plt.plot(k_bands, e_m_bands, color="blue", alpha=1, linewidth=1)

        plt.xticks([0, precision-1, 2*precision-2, 3*precision-3], ["M", r"$\Gamma$", "K", "M"])
    
    elif material=="nanotube":
        band_number=0
        while band_number < e_p_bands.size:
            start_index=(band_number)*precision
            end_index=(band_number+1)*precision

            plt.plot(k_bands[start_index : end_index], e_p_bands[start_index : end_index], color="black", alpha=1, linewidth=1)
            plt.plot(k_bands[start_index : end_index], e_m_bands[start_index : end_index], color="blue", alpha=1, linewidth=1)

            band_number+=1
        
        plt.xticks([0,k_bands[-1]], [r"$\Gamma$", "X"])

    plt.show()









if __name__ == "__main__":
    main()