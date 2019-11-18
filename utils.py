def list_input(in_string):
    string_split = in_string.split(',')
    string_strip = []
    for vals in string_split:
        string_strip.append(vals.strip())
    final_list = []
    for i in range(len(string_strip)):
        final_list.append(float(string_strip[i]))

    return(final_list)


def arcsec_to_kpc(z, arcsec):
    from astropy.cosmology import FlatLambdaCDM

    cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
    dist = cosmo.angular_diameter_distance(z)
    kpc = (dist.value / 206265) * arcsec * 1000

    return(kpc)
