files = [
    "../constants.py", "../main.py",
    "../controls/keyboard.py", "../controls/mouse.py",
    "../entities/entity.py", "../entities/health_bar.py", "../entities/hud.py",
    "../entities/mortal.py", "../entities/projectile.py",
    "../entities/buildings/base.py", "../entities/buildings/wall.py",
    "../entities/buttons/button.py", "../entities/buttons/level_selector.py", "../entities/buttons/summoner.py",
    "../entities/buttons/system.py", "../entities/buttons/upgrade.py",
    "../entities/microbes/microbe.py", "../entities/microbes/microbe_builder.py",
    "../entities/microbes/bacteriophages/b_basic.py", "../entities/microbes/bacteriophages/b_pult.py",
    "../entities/microbes/bacteriophages/b_tank.py", "../entities/microbes/bacteriophages/bacteriophage.py",
    "../entities/microbes/macrophages/m_basic.py", "../entities/microbes/macrophages/m_beach.py",
    "../entities/microbes/macrophages/macrophage.py",
    "../fonts/text.py", "../img/images.py",
    "../levels/level.py", "../levels/level_builder.py", "../levels/level_one.py",
    "../logic/circle.py", "../logic/collisions.py", "../logic/dice.py", "../logic/graphics.py",
    "../logic/positions.py", "../logic/rect.py",
    "../sound/sounds.py"
]


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
