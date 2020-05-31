# Documentation :)

## Format

#### Classes:

Class_Name (Superclass_Name)

#### Constructors:

\* constructor_name(Param_Type type1, ...)

#### Fields:

\- public_field_name → Type

\- _private_field_name → Type

#### Methods:

\+ method_name(Type argument=default, ...) → Return_Type

## ./

#### Constants (N/A)

#### Main (N/A)

## ./controls

#### Keyboard (N/A)

#### Mouse (N/A)

## ./entities

#### Entity (object)
\- _x → float

\- _y → float

\- _w → float

\- _h → float

\- _name → str

\- _current_animation → str

\- _animation_spd → int

\- _animation_cycle → int

\- _animation_looped → bool

\+ get_rect() → Rect

\+ change_animation(str new_animation_key, int new_animation_spd=None) → None

\+ draw(pygame.Surface display) → None

\+ go(pygame.Surface display) → None

#### Health_Bar (object)
\- _w → float

\- _h → float

\- _max_hp → int

\+ draw(pygame.Surface display, Microbe parent, int vert_offset) → None

#### HUD (Entity)

#### Microbe (Mortal)
\- _spd → float

\- _dmg → int

\- _attack_key_frame → int

\- _in_front → Mortal

\- _cooldown_timer → int

\- _cooldown_left → int

\+ get_unit_id() → str

\+ set_in_front(Mortal in_front) → None

\+ speed_change_funtime() → None

\+ pos() → None

#### Microbe_Builder (N/A)

#### Mortal (Entity)
\- _hp → int

\- _health_bar → Health_Bar

\+ get_hp() → int

\+ is_alive() → bool

\+ apply_damage() → None

## ./entities/bacteriophages

#### Bacteriophage (Microbe)

#### ∀ Types (Bacteriophage)

## ./entities/buildings

#### Base (Entity)
\- _allegiance → bool

#### Wall (Entity)
\- _allegiance → bool

\- _tier_number → int

## ./entities/buttons

#### Button (Entity)
\- _text_key → str

\- _text_template → str

#### Summoner (Button)
\- _cooldown_timer → int

\- _cooldown_left → int

\- _unit_id → str

\+ get_unit_id() → str

\+ can_summon() → bool

\+ do_summon() → None

#### System (Button)

#### Upgrade (Button)

## ./entities/macrophages

#### Macrophage (Microbe)

#### ∀ Types (Macrophage)

## ./fonts

#### Text (N/A)
\- _source → str

\- _sizes → int[]

\- MULI → {int : pygame.font.Font}

\- RENDERED_TEXT → {str : (pygame.Surface, pygame.Rect)}

\+ prepare_text(str to_prepare) → (pygame.Surface, pygame.Rect)

## ./img

#### Images (N/A)
\- IMAGES → {str : {str : pygame.Surface[]}}

## ./levels

#### Level (object)
\- POSSIBLE_UPGRADES → {str}

\- _macrophages → Macrophage{}

\- _macrophages_available → str{}

\- _macrophage_walls → Wall{}

\- _macrophage_base → Base

\- _macrophage_summoners → Summoner[]

\- _bacteriophages → Bacteriophage{}

\- _bacteriophages_available → str{}

\- _bacteriophage_walls → Wall{}

\- _bacteriophage_base → Base

\- _bacteriophage_summoners → Summoner[]

\- _upgrades_enabled → {str}

\- _upgrade_controlled_values → various (?)

\+ _first_in_front_of_second(Mortal first, Mortal second, bool base_is_at_left) → bool

\+ _get_mortal_in_front(Microbe{} microbes, Wall[] walls, Base base, bool base_is_at_left) → Mortal

\+ _microbe_actions(pygame.Surface window, Microbe{} now, Microbe{} enemies, Wall[] enemy_walls, Base enemy_base, bool enemy_side) → Microbe{}

\+ _wall_actions(pygame.Surface window, Wall[] walls) → Wall[]

\+ _summoner_actions(pygame.Surface window, Summoner[] summoners, Microbe{} microbes) → None

\+ get_upgrade_controlled_values(various) → various (?)

\+ set_upgrade(something) → bool (?)

#### ∀ Level{#} (Level)
\- _name → str (?)

\+ draw(pygame.Surface display) → None (?)

## ./logic

#### Circle (object)
\- X → float

\- Y → float

\- R → float

#### Collisions (N/A)

#### Graphics (N/A)

#### Rect (object)
\- X → float

\- Y → float

\- W → float

\- H → float