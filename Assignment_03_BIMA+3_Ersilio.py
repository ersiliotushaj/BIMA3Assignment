# Calculating different geometrical characteristics of a polygonal section - Ersilio Tushaj

# Define the number of polygon vertices counter clockwise
npv = int(input(" Define number of vertices of the polygon(>3): "))

# Define coordinates and geometrical characteristics of the section

x = []
y = []

j = 0 
Ax = 0 
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0
xt = 0
yt = 0
Ixt = 0
Iyt = 0 
Ixyt = 0 

if npv > 3:
    print("Number of vertices",npv)
    
else:
    npv = int(input(" Try another value, more than 3 vertices: "))

# input x and y coordinates
i=0
while i < npv:
        i = i + 1
        x.append(float(input(f"Input coordinate of x{i:<2.0f}:")))
        y.append(float(input(f"Input coordinate of y{i:<2.0f}:")))

print("-" * 30)

print(f"{'Coord.':<10} {'x':<10.2} {'y':<10.2}")

print("-" * 30)

for k in range(0,npv):
    print(f"{k+1:<9} {x[k]:<10.2f} {y[k]:<10.2f}")
print("-" * 30)


# Define Section Geometrical characteristics 

for j in range(npv-1):

    Ax = (1/2) * (x[j+1] + x[j]) * (y[j+1] - y[j]) + Ax
    
    Sx = (-1/6) * (x[j+1] - x[j]) * (y[j+1]**2 + y[j] * y[j+1] + y[j]**2) + Sx
    
    Sy = (1/6) * (y[j+1] - y[j]) * (x[j+1]**2 + x[j] * x[j+1] + x[j]**2) + Sy
    
    Ix = (-1/12) * (x[j+1] - x[j]) * (y[j+1]**3 + y[j+1]**2 * y[j] + y[j+1] * y[j]**2 + y[j]**3) + Ix
    
    Iy = (1/12) * (y[j+1] - y[j]) * (x[j+1]**3 + x[j+1]**2 * x[j] + x[j+1] * x[j]**2 + x[j]**3) + Iy
    
    Ixy = (-1/24) * (y[j+1] - y[j]) * ((y[j+1] * (3 * x[j+1]**2 + 2 * x[j+1] * x[j] + x[j]**2)) + (y[j] * (3 * x[j]**2 + 2 * x[j+1] * x[j] + x[j+1]**2))) + Ixy
    
    j = j+1
    
# Define other Section Geometrical characteristics

xt = Sy / Ax
yt = Sx / Ax
Ixt = Ix - yt**2 * Ax
Iyt = Iy - xt**2 * Ax
Ixyt = Ixy + (xt * yt * Ax)

# Print results

print (f" {'The Area Ax of the polygon:'} {Ax:.2f}")
print (f" {'The static moment Sx:'} {Sx:.2f}")
print (f" {'The static moment Sy:'} {Sy:.2f}")
print (f" {'The moment of inertia Ix:'} {Ix:.2f}")
print (f" {'The moment of inertia Iy:'} {Iy:.2f}")
print (f" {'The moment of inertia Ixy:'} {Ixy:.2f}")
print (f" {'Baricentrum xt:'} {xt:.2f}")
print (f" {'Baricentrum yt:'} {yt:.2f}")
print (f" {'Baricentrum moment of inertia Ixt:'} {Ixt:.2f}")
print (f" {'Baricentrum moment of inertia Iyt:'} {Iyt:.2f}")
print (f" {'Baricentrum moment of inertia Ixyt:'} {Ixyt:.2f}")

# End