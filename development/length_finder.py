files = ["../constants.py", "../level.py", "../main.py",
         "../controls/keyboard.py", "../controls/mouse.py",
         "../fonts/text.py", "../img/images.py",
         "../logic/collisions.py", "../logic/graphics.py", "../logic/rect.py", "../logic/circle.py",
         "../entities/entity.py", "../entities/microbe.py", "../entities/hud.py",
         "../entities/mortal.py", "../entities/health_bar.py",
         "../entities/buildings/base.py", "../entities/buildings/wall.py",
         "../entities/macrophages/macrophage.py", "../entities/bacteriophages/bacteriophage.py",
         "../entities/macrophages/m_basic.py", "../entities/bacteriophages/b_basic.py",
         "../entities/buttons/button.py", "../entities/buttons/system.py", "../entities/buttons/upgrade.py",
         "../entities/buttons/summoner.py"]


def file_len(f_name):
    with open(f_name) as file:
        i = 0
        for i, l in enumerate(file):
            pass
    return i + 1


total = 0
for f in files:
    total += file_len(f)

print(str(total) + " lines")
