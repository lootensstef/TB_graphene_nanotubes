import matplotlib.pyplot as plt
import eb_simulation #separate file that runs all the calculations and outputs the energy bands


def main():
    material, nt_n, nt_m = eb_simulation.material_selector()
    precision= eb_simulation.precision_selector()
    k_bands, e_p_bands, e_m_bands = eb_simulation.simulate_energybands(material, nt_n, nt_m, precision)

    #various pyplot graphic options
    plt.figure(figsize=(16,10), dpi=150)
    plt.rcParams["font.family"] = "Times New Roman"

    if material=="graphene":
        plt.plot(k_bands, e_p_bands, color="deepskyblue", alpha=1, linewidth=1)
        plt.plot(k_bands, e_m_bands, color="darkorange", alpha=1, linewidth=1)
        plt.axhline(y=0,color="red",linestyle="--",linewidth=0.8,alpha=0.5)

        plt.title("Graphene band structure along high symmetry lines", fontsize=22)
        plt.xlabel("Wave vector", fontsize=18)
        plt.ylabel("Energy (eV)", fontsize=18)
        plt.xticks([0, precision-1, 2*precision-2, 3*precision-3], ["M", r"$\Gamma$", "K", "M"], fontsize=20)
        
    
    elif material=="nanotube":
        band_number=0

        while band_number < e_p_bands.size:
            start_index=(band_number)*precision
            end_index=(band_number+1)*precision

            plt.plot(k_bands[start_index : end_index], e_p_bands[start_index : end_index], color="deepskyblue", alpha=1, linewidth=1)
            plt.plot(k_bands[start_index : end_index], e_m_bands[start_index : end_index], color="darkorange", alpha=1, linewidth=1)
            plt.axhline(y=0,color="red",linestyle="--",linewidth=0.8,alpha=0.5)

            band_number+=1
        
        plt.title(f"({nt_n},{nt_m}) carbon nanotube band structure", fontsize=22)
        plt.xlabel("Wave vector", fontsize=18)
        plt.ylabel("Energy (eV)", fontsize=18)
        plt.xticks([0,k_bands[-1]], [r"$\Gamma$", "X"], fontsize=20)

    plt.grid(alpha=0.3, linestyle="--")

    plt.show()







if __name__ == "__main__":
    main()