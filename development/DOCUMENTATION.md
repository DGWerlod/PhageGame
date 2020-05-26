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

#### Level (object)
\- _microbes_available → Microbe{}

\- _upgrades_enabled → {str}

\- _possible_upgrades → {str}

\- _upgrade_controlled_values → various

\+ get_upgrade_controlled_values(various) → various

\+ set_upgrade(something) → bool

#### ∀ Level{#} (Level)
\- _name → str

\+ draw(pygame.Surface display) → None

#### Constants (N/A)
#### Main (N/A)

## ./entities

#### Entity (object)
\- _x → float

\- _y → float

\- _w → float

\- _h → float

\- _name → str

\+ get_rect() → Rect

\+ draw(pygame.Surface display) → None

\+ go(pygame.Surface display) → ????? something, inevitably

#### Microbe (Entity)
\- _spd → float

\- _hp → int

\- _dmg → int

\+ is_alive() → bool

\+ attack(Microbe target) → ????? something, inevitably

\+ apply_damage(int dmg) → bool?

\+ pos() → None

#### Tower (Entity)

#### Base (Entity)

#### HUD (Entity)

## ./entities/macrophages

#### Macrophage (Microbe)
#### ∀ Types (Macrophage)

## ./entities/bacteriophages

#### Bacteriophage (Microbe)
#### ∀ Types (Bacteriophage)

## ./entities/buttons

#### Button (Entity)
\- _text_key → str

\- _text_template → str

#### Upgrade (Button)
#### System (Button)
#### Summoner (Button)
#### ∀ Microbe_Type_Summoner (Summoner)

## ./img

#### Images (N/A)
\- IMAGES → {str : {str : pygame.Surface[]}}

## ./fonts

#### Text (N/A)
\- _font → pygame.font.Font

\- RENDERED_TEXT → {str : (pygame.Surface, pygame.Rect)}

\+ prepare_text(str to_prepare) → (pygame.Surface, pygame.Rect)

## ./logic

#### Rect (object)
\- X → float

\- Y → float

\- W → float

\- H → float

#### Circle (object)
\- X → float

\- Y → float

\- R → float

#### Collisions (N/A)
#### Graphics (N/A)

## ./controls

#### Keyboard (N/A)
#### Mouse (N/A)
