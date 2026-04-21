import os

SVG_DIR = "svg"
README = "README.md"

def generate_icon_list():
    files = sorted(
        f for f in os.listdir(SVG_DIR)
        if f.endswith(".svg")
    )

    lines = []
    lines.append("| Icon | Name |")
    lines.append("|------|------|")

    for f in files:
        name = f[:-4]
        lines.append(f'| <img src="./svg/{f}" width="24" /> | {name} |')

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
