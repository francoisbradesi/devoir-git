def mult_scal(scal,vec) :
    return((scal*vec[0],scal*vec[1],scal*vec[2]))

def produit_scalaire(x,y):
    return(x[0]*y[0] + x[1]*y[1] + x[2]*y[2])

def norme(x,y,z):
    return(x**2+y**2+z**2)**0.5

def somme_vec(a,b) :
    return(a[0]+b[0],a[1]+b[1],a[2]+b[2])
