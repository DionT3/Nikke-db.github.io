import json
from pathlib import Path

l2d_folder = Path("l2d")

char_data = []

for folder in sorted(l2d_folder.iterdir()):
    if not folder.is_dir():
        continue
    
    char_id = folder.name
    char_name = char_id  # default
    
    # Mapping nama (bisa kamu tambah)
    name_map = {
        "c010": "Rapi",
        "c011": "Neon",
        "c012": "Anis",
        "c014": "Neon Blue Ocean",
        "c015": "Anis Sparkling Summer",
        "c020": "Delta",
        "c022": "Signal",
        "c030": "Poli",
        "c032": "Miranda",
        "c040": "D",
        "c041": "Agent K",
        "c053": "Liqueur",
        "c060": "Belorta",
        "c061": "Mica",
        "c070": "Brid",
        "c071": "Soline",
        "c072": "Diesel",
        "c080": "Centi",
        "c081": "Acre",
        "c082": "Liter",
        "c090": "Emma",
        "c091": "Vesti",
        "c092": "Eunhwa",
        "c100": "Laplace",
        "c101": "Drake",
        "c102": "Maxwell",
        "c110": "Crow",
        "c111": "Jackal",
        "c112": "Viper",
        "c120": "N102",
        "c121": "Anne Miracle Fairy",
        "c130": "Mary",
        "c131": "Pepper",
        "c132": "Mary Bay Goddess",
        "c140": "Sugar",
        "c141": "Milk",
        "c142": "Frima",
        "c150": "Julia",
        "c160": "Yuni",
        "c161": "Mihara",
        "c170": "Privaty",
        "c171": "Yulha",
        "c172": "Admi",
        "c180": "Guillotine",
        "c181": "Maiden",
        "c190": "Lucilla",
        "c191": "Alice",
        "c193": "Neve",
        "c200": "Rupee",
        "c201": "Yan",
        "c202": "Dolla",
        "c203": "Rupee Winter",
        "c210": "Exia",
        "c212": "Novel",
        "c220": "Snow White",
        "c221": "Rapunzel",
        "c222": "Scarlet",
        "c230": "Harran",
        "c231": "Isabel",
        "c232": "Noah",
        "c233": "Dorothy",
        "c240": "Rumani",
        "c241": "Epinel",
        "c242": "Folkwang",
        "c260": "Modernia",
        "c261": "Nihilister",
        "c262": "Liberelli",
        "c270": "Blanc",
        "c271": "Noir",
        "c272": "Rouge",
        "c280": "Rosanna",
        "c281": "Moran",
        "c282": "Sakura",
        "c290": "Mana",
        "c291": "Ether",
        "c300": "Soldier EG",
        "c301": "Soldier FA",
        "c302": "Product 08",
        "c303": "Product 12",
        "c304": "iDoll Flower",
        "c305": "iDoll Ocean",
        "c306": "Soldier OW",
        "c307": "Product 23",
        "c308": "iDoll Sun",
        "c310": "Aid",
        "c311": "Cocoa",
        "c312": "Soda",
        "c320": "Bibli",
        "c321": "Marchana",
        "c331": "Chime",
        "c340": "Siren",
        "c342": "Pin",
        "c350": "Mast",
        "c351": "Anchor",
        "c352": "Helm",
        "c353": "Helm Aquamarine",
        "c371": "Endless",
        "c380": "Nero",
        "c381": "Biscuit",
        "c392": "Rei",
        "c400": "Guilty",
        "c401": "Sin",
        "c402": "Quency",
        "c432": "Aria",
        "c800": "Makima",
        "c801": "Power",
        "c802": "Himeno"
    }
    
    char_name = name_map.get(char_id, char_id)

    costumes = []
    for file in sorted(folder.iterdir()):
        if file.is_dir() or not file.suffix:
            continue
        costume_id = file.stem
        costume_name = costume_id.replace("_", " ").title()
        costumes.append({
            "costumeId": costume_id,
            "costumeName": costume_name,
            "spine": costume_id
        })

    char_data.append({
        "charId": char_id,
        "charName": char_name,
        "costumes": costumes
    })

# Simpan
with open("CharInfo.json", "w", encoding="utf-8") as f:
    json.dump(char_data, f, indent=2, ensure_ascii=False)

print(f"✅ CharInfo.json berhasil dibuat dengan {len(char_data)} karakter!")
