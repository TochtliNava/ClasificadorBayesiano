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

print(c_kecimen, c_Besni)

m_c_kecimen, m_c_Besni = c_kecimen/df.shape[0], c_Besni/df.shape[0]

print(m_c_kecimen, m_c_Besni)

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

print(p(130, 122.916666, 176.25))