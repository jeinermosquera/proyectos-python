import pandas as pd

data = {
    "nombres": ["jeiner", "carol", "dairon", "dianelvy"],
    "Edad": [19, 18, 20, 23],
    "Cantidad": [4, 6, 2, 8],
}
datos = pd.DataFrame(data)
print(datos)
