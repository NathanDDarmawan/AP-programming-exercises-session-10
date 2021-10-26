def num_atoms(grams, Aweight=196.97):
    atoms = (grams/Aweight)*(6.022*(10**23))
    return atoms
    
print(num_atoms(10, 1.008))
