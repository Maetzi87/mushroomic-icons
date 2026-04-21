import os

SVG_DIR = "svg"
README = "README.md"

def generate_icon_list():
    files = sorted(
        f for f in os.listdir(SVG_DIR)
        if f.endswith(".svg")
    )

    # Paare bilden: links + rechts
    # Beispiel: [a,b,c,d,e] → [(a,c), (b,d), (e,None)]
    left = files[::2]
    right = files[1::2]

    # Falls ungerade Anzahl → rechte Seite auffüllen
    if len(left) > len(right):
        right.append(None)

    lines = []
    lines.append("| Icon | Name |   | Icon | Name |")
    lines.append("|------|------|---|------|------|")

    for l, r in zip(left, right):
        # linke Seite
        l_name = l[:-4]
        l_icon = f'<img src="./svg/{l}" width="24" />'

        # rechte Seite (falls None → leere Zellen)
        if r is None:
            r_icon = ""
            r_name = ""
        else:
            r_name = r[:-4]
            r_icon = f'<img src="./svg/{r}" width="24" />'

        lines.append(f"| {l_icon} | {l_name} |   | {r_icon} | {r_name} |")

    return "\n".join(lines)



def update_readme():
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()

    start = "<!-- ICONS START -->"
    end = "<!-- ICONS END -->"

    before = content.split(start)[0]
    after = content.split(end)[1]

    new_list = generate_icon_list()

    new_content = (
        before
        + start + "\n"
        + new_list + "\n"
        + end
        + after
    )

    with open(README, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("README updated successfully.")

if __name__ == "__main__":
    update_readme()
