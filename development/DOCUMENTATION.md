# Documentation :)

## Format

#### Classes:

Class_Name (Superclass_Name)

#### Constructors:

C constructor_name(Param_Type type1, ...)

#### Fields:

F public_field_name → Type

F _private_field_name → Type

#### Methods:

M method_name(Type argument=default, ...) → Return_Type

## ./

#### Level (object)
- F _microbes_available → Microbe{}
- F _upgrades_enabled → {str}
- F _possible_upgrades → {str}
- F _upgrade_controlled_values → various
+ M get_upgrade_controlled_values(various) → various
+ M set_upgrade(something) → bool

#### ∀ Level{#} (Level)
- F _name → str
+ M draw(pygame.Surface display) → None

#### Constants (N/A)
#### Main (N/A)

## ./entities

#### Entity (object)
- F _x → float
- F _y → float
- F _w → float
- F _h → float
- F _name → str
+ M get_rect() → Rect
+ M draw(pygame.Surface display) → None
+ M go(pygame.Surface display) → ????? something, inevitably

#### Microbe (Entity)
- F _spd → float
- F _hp → int
- F _dmg → int
+ M is_alive() → bool
+ M attack(Microbe target) → ????? something, inevitably
+ M apply_damage(int dmg) → bool?
+ M pos() → None

#### HUD (Entity)

## ./entities/macrophages

#### Macrophage (Microbe)
#### ∀ Types (Macrophage)

## ./entities/bacteriophages

#### Bacteriophage (Microbe)
#### ∀ Types (Bacteriophage)

## ./entities/buttons

#### Button (Entity)
- F _text_key → str
- F _text_template → str

#### Upgrade (Button)
#### System (Button)
#### Summoner (Button)
#### ∀ Microbe_Type_Summoner (Summoner)

## ./img

#### Images (N/A)
- F IMAGES → {str : {str : pygame.Surface[]}}

## ./fonts

#### Text (N/A)
- F _font → pygame.font.Font
- F RENDERED_TEXT → {str : (pygame.Surface, pygame.Rect)}
+ M prepare_text(str to_prepare) → (pygame.Surface, pygame.Rect)

## ./logic

#### Rect (object)
- F X → float
- F Y → float
- F W → float
- F H → float

#### Circle (object)
- F X → float
- F Y → float
- F R → float

#### Collisions (N/A)
#### Graphics (N/A)

## ./controls

#### Keyboard (N/A)
#### Mouse (N/A)
