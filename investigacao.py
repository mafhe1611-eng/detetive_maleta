import pandas as pd

crime_scene = pd.read_csv("crime_scene.csv")
suspects = pd.read_csv("suspects.csv")
interrogation = pd.read_csv("interviews.csv")

crime = crime_scene[crime_scene["location"] == "Blue Note Lounge"]
print(crime)

suspeitos = suspects[
    (suspects["attire"] == "sobretudo") &
    (suspects["scar"] == "bochecha esquerda")
]
print(suspeitos)

resultado = suspeitos.merge(
    interrogation,
    left_on="id",
    right_on="suspect_id",
    how="left"
)
print(resultado[["id", "name", "attire", "scar", "transcript"]])

culpado = resultado[
    resultado["transcript"].str.contains(
        "roubei",
        case=False,
        na=False
    )
]
print(culpado[["id", "name", "transcript"]])