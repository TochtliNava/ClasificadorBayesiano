import pandas as pd
import math

def p(a, v, m):
    return (1/math.sqrt(2*math.pi*v))*(math.exp(-math.pow(((a - m)),2)/(2*v)))

c_kecimen = 0
c_Besni = 0

df = pd.read_csv("data.csv")
for dato in df["Class"]:
    if(dato == "Kecimen"):
        c_kecimen = c_kecimen + 1
    if(dato == "Besni"):
        c_Besni = c_Besni + 1

m_c_kecimen, m_c_Besni = c_kecimen/df.shape[0], c_Besni/df.shape[0]

m_area = df["Area"].mean()
m_majorAxis = df["MajorAxisLength"].mean()
m_menorAxis = df["MinorAxisLength"].mean()
m_eccentricity = df["Eccentricity"].mean()
m_convexArea = df["ConvexArea"].mean()
m_extent = df["Extent"].mean()
m_perimeter = df["Perimeter"].mean()

var_area = df["Area"].var()
var_majorAxis = df["MajorAxisLength"].var()
var_menorAxis = df["MinorAxisLength"].var()
var_eccentricity = df["Eccentricity"].var()
var_convexArea = df["ConvexArea"].var()
var_extent = df["Extent"].var()
var_perimeter = df["Perimeter"].var()

#   Kecimen

m_k_area = df["Area"][0:449].mean()
m_k_majorAxis = df["MajorAxisLength"][0:449].mean()
m_k_menorAxis = df["MinorAxisLength"][0:449].mean()
m_k_eccentricity = df["Eccentricity"][0:449].mean()
m_k_convexArea = df["ConvexArea"][0:449].mean()
m_k_extent = df["Extent"][0:449].mean()
m_k_perimeter = df["Perimeter"][0:449].mean()

var_k_area = df["Area"][0:449].var()
var_k_majorAxis = df["MajorAxisLength"][0:449].var()
var_k_menorAxis = df["MinorAxisLength"][0:449].var()
var_k_eccentricity = df["Eccentricity"][0:449].var()
var_k_convexArea = df["ConvexArea"][0:449].var()
var_k_extent = df["Extent"][0:449].var()
var_k_perimeter = df["Perimeter"][0:449].var()

#   Besni

m_b_area = df["Area"][450:899].mean()
m_b_majorAxis = df["MajorAxisLength"][450:899].mean()
m_b_menorAxis = df["MinorAxisLength"][450:899].mean()
m_b_eccentricity = df["Eccentricity"][450:899].mean()
m_b_convexArea = df["ConvexArea"][450:899].mean()
m_b_extent = df["Extent"][450:899].mean()
m_b_perimeter = df["Perimeter"][450:899].mean()

var_b_area = df["Area"][450:899].var()
var_b_majorAxis = df["MajorAxisLength"][450:899].var()
var_b_menorAxis = df["MinorAxisLength"][450:899].var()
var_b_eccentricity = df["Eccentricity"][450:899].var()
var_b_convexArea = df["ConvexArea"][450:899].var()
var_b_extent = df["Extent"][450:899].var()
var_b_perimeter = df["Perimeter"][450:899].var()

print("Ingrese los datos para clasificar (Bayesian classifier)")
area = float(input("Area: "))
majorAxis = float(input("Major Axis: "))
menorAxis = float(input("Minor Axis: "))
eccentricity = float(input("Eccentricity: "))
convexArea = float(input("Convex Area: "))
extent = float(input("Extent: "))
perimeter = float(input("Perimeter: "))

p_k_area = p(area, var_k_area, m_k_area)
p_k_majorAxis = p(majorAxis, var_k_majorAxis, m_k_majorAxis)
p_k_menorAxis = p(menorAxis, var_k_menorAxis, m_k_menorAxis)
p_k_eccentricity = p(eccentricity, var_k_eccentricity, m_k_eccentricity)
p_k_convexArea = p(convexArea, var_k_convexArea, m_k_convexArea)
p_k_extent = p(extent, var_k_extent, m_k_extent)
p_k_perimeter = p(perimeter, var_k_perimeter, m_k_perimeter)

p_b_area = p(area, var_b_area, m_b_area)
p_b_majorAxis = p(majorAxis, var_b_majorAxis, m_b_majorAxis)
p_b_menorAxis = p(menorAxis, var_b_menorAxis, m_b_menorAxis)
p_b_eccentricity = p(eccentricity, var_b_eccentricity, m_b_eccentricity)
p_b_convexArea = p(convexArea, var_b_convexArea, m_b_convexArea)
p_b_extent = p(extent, var_b_extent, m_b_extent)
p_b_perimeter = p(perimeter, var_b_perimeter, m_b_perimeter)

v_k = m_c_kecimen * p_k_area * p_k_majorAxis * p_k_menorAxis * p_k_eccentricity * p_k_convexArea * p_k_extent * p_k_perimeter
v_b = m_c_Besni * p_b_area * p_b_majorAxis * p_b_menorAxis * p_b_eccentricity * p_b_convexArea * p_b_extent * p_b_perimeter

print(f"\n{"Kecimen" if v_k > v_b else "Besni"} P = {v_k if v_k > v_b else v_b}")

#   MCE

mce = 0

for i in range(df.shape[0]):
    p_k_area = p(df["Area"][i], var_k_area, m_k_area)
    p_k_majorAxis = p(df["MajorAxisLength"][i], var_k_majorAxis, m_k_majorAxis)
    p_k_menorAxis = p(df["MinorAxisLength"][i], var_k_menorAxis, m_k_menorAxis)
    p_k_eccentricity = p(df["Eccentricity"][i], var_k_eccentricity, m_k_eccentricity)
    p_k_convexArea = p(df["ConvexArea"][i], var_k_convexArea, m_k_convexArea)
    p_k_extent = p(df["Extent"][i], var_k_extent, m_k_extent)
    p_k_perimeter = p(df["Perimeter"][i], var_k_perimeter, m_k_perimeter)

    p_b_area = p(df["Area"][i], var_b_area, m_b_area)
    p_b_majorAxis = p(df["MajorAxisLength"][i], var_b_majorAxis, m_b_majorAxis)
    p_b_menorAxis = p(df["MinorAxisLength"][i], var_b_menorAxis, m_b_menorAxis)
    p_b_eccentricity = p(df["Eccentricity"][i], var_b_eccentricity, m_b_eccentricity)
    p_b_convexArea = p(df["ConvexArea"][i], var_b_convexArea, m_b_convexArea)
    p_b_extent = p(df["Extent"][i], var_b_extent, m_b_extent)
    p_b_perimeter = p(df["Perimeter"][i], var_b_perimeter, m_b_perimeter)

    v_k = m_c_kecimen * p_k_area * p_k_majorAxis * p_k_menorAxis * p_k_eccentricity * p_k_convexArea * p_k_extent * p_k_perimeter
    v_b = m_c_Besni * p_b_area * p_b_majorAxis * p_b_menorAxis * p_b_eccentricity * p_b_convexArea * p_b_extent * p_b_perimeter

    clase = "Kecimen" if v_k > v_b else "Besni"

    if(clase != df["Class"][i]):
        mce = mce + 1


mce = mce/df.shape[0] * 100
print(f"\nError = {mce}%")
