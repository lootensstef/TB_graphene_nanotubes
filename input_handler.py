

def material_selector():
    """This function handles the user input to select the type of available simulations to run
    
    Parameters:
        none, the values are taken as successive terminal inputs at runtime
    
    Returns:
        material (string): selected material 
        n, m (integers): nanotube indices, only used if the material is a nanotube 

    Raises:
        ValueError if the user writes invalid n, m inputs: inputs that fail to be converted to integers"""

    material=None
    n=None
    m=None

    while True:
        material=input("Choose a material to simulate (graphene/nanotube): ").lower()

        if material=="graphene":
            break
        elif material=="nanotube":

            while True:
                print("Choose the type of (n,m) nanotube: ")

                try: 
                    n=int(input("n: "))
                    m=int(input("m: "))

                    if (n<0 or m<0) or (n<1 and m<1):
                        print("Invalid input, integers must be non negative with at least one different from zero \n")
                    else:
                        break                    
                except ValueError:
                    print("Invalid input, please enter integer numbers \n")           
            break
        else:
            print("Invalid input, please write a valid material \n")
    return material, n, m


def precision_selector():
    """This function handles the user input to select the number of points per reciprocal space line.
    
    Parameters:
        none, the value is taken as an input at runtime
    
    Returns:
        N: number of points per line (integer), a parameter that affects precision

    Raises:
        ValueError if the user writes an invalid input: something that fails to be converted to an integer"""
    
    precision=None

    while True:
        print("Choose the type number of points per reciprocal space line")

        try: 
            precision=int(input("N=?"))

            if precision<2:
                print("Invalid input, integer must be 2 or greater \n")
            else:
                break                    
        except ValueError:
            print("Invalid input, please enter an integer number \n")      

    return precision     

