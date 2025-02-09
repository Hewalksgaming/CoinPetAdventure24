@namespace
class SpriteKind:
    KOIN = SpriteKind.create()
    KOIN2 = SpriteKind.create()
    BouncyBoll = SpriteKind.create()
    Pet = SpriteKind.create()
    NPC = SpriteKind.create()
    animal = SpriteKind.create()

def on_up_pressed():
    hero.set_image(assets.image("""
        snakyboi
    """))
    animation.stop_animation(animation.AnimationTypes.ALL, hero)
    animation.run_image_animation(hero, assets.animation("""
        myAnim3
    """), 500, True)
    info.set_score(coins)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def KLEARKOIN2():
    sprites.destroy(MYKOIN2, effects.confetti, 500)

def on_overlap_tile(sprite2, location):
    global coins
    game.show_long_text("WELL DONE... YOU FOUND A COIN CHEST!", DialogLayout.BOTTOM)
    coins += randint(0, 25)
    tiles.set_current_tilemap(tilemap("""
        level25
    """))
    pause(2000)
    game.show_long_text("Penny: Hey Adventurer... The New Update Will Be Coming Out Soon... You Can Download It When It Releases At: CoinPetAdventure.co.uk But For Now You Can Replay The Game.",
        DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def on_on_overlap(sprite3, otherSprite2):
    global coins
    game.show_long_text("WOULD YOU LIKE TO TRADE THE BOUNCY BALL FOR ONE COIN?",
        DialogLayout.BOTTOM)
    story.show_player_choices("YES!", "NO!", "What's that?")
    if True:
        if story.check_last_answer("YES!"):
            if 1 <= info.score():
                coins += -1
                sprites.destroy(BouncyBoll2, effects.confetti, 100)
                game.show_long_text("A DOOR OPENS IN THE WALL AND YOU WALK THROUGH...",
                    DialogLayout.BOTTOM)
                PETDIALOUGEDOGGYONE()
            elif coins == 0:
                game.show_long_text("YOU DON'T HAVE ENOUGH COINS TO BUY THIS ITEM! TRY LOOKING AROUND THE HOUSE...",
                    DialogLayout.BOTTOM)
                pause(1000)
        elif story.check_last_answer("NO!"):
            pause(1000)
    elif story.check_last_answer("What's that?"):
        game.show_long_text("The bouncy ball bounces between dimensions, teleporting you to a completely different world! Why not give it a try? What other us",
            DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.player, SpriteKind.BouncyBoll, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    global coins
    KLEARKOIN2()
    game.splash("YOU FOUND A COIN!")
    coins += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.KOIN2, on_on_overlap2)

def ForestLvL01():
    global Beevah
    tiles.set_current_tilemap(tilemap("""
        level34
    """))
    Beevah = sprites.create(assets.image("""
        Beevah
    """), SpriteKind.NPC)
    Beevah.set_position(54, 58)
    hero.set_position(0, 0)

def on_left_pressed():
    hero.set_image(assets.image("""
        myImage
    """))
    animation.stop_animation(animation.AnimationTypes.ALL, hero)
    animation.run_image_animation(hero, assets.animation("""
        myAnim1
    """), 500, True)
    info.set_score(coins)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile2(sprite5, location2):
    global BouncyBoll2
    BouncyBoll2 = sprites.create(assets.image("""
        myImage2
    """), SpriteKind.BouncyBoll)
    tiles.set_current_tilemap(tilemap("""
        level0
    """))
    hero.set_position(138, 210)
    clearlevel()
    tiles.place_on_tile(BouncyBoll2, tiles.get_tile_location(5, 5))
    game.show_long_text("Hmmm... What's in here?", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile2)

def on_right_released():
    hero.set_image(assets.image("""
        myImage0
    """))
    animation.run_image_animation(hero, assets.animation("""
        myAnim
    """), 500, True)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    hero.set_image(assets.image("""
        myImage0
    """))
    animation.run_image_animation(hero, assets.animation("""
        myAnim
    """), 500, True)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_on_score():
    if info.high_score() == 2:
        game.show_long_text("WELL DONE... YOU FOUND ALL THE COINS! NOW MAYBE WE SHOULD FIND OUT WHAT IS INSIDE THAT HOUSE...",
            DialogLayout.BOTTOM)
    else:
        pause(100)
info.on_score(2, on_on_score)

def KLEARKOIN():
    sprites.destroy(MY_KOIN, effects.confetti, 500)

def on_right_pressed():
    hero.set_image(assets.image("""
        myImage
    """))
    animation.stop_animation(animation.AnimationTypes.ALL, hero)
    animation.run_image_animation(hero, assets.animation("""
        myAnim2
    """), 500, True)
    info.set_score(coins)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap3(sprite4, otherSprite3):
    global coins
    KLEARKOIN()
    game.splash("YOU FOUND A COIN!")
    coins += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.KOIN, on_on_overlap3)

def clearlevel():
    sprites.destroy(MY_KOIN)
    sprites.destroy(MYKOIN2)

def on_up_released():
    hero.set_image(assets.image("""
        myImage0
    """))
    animation.run_image_animation(hero, assets.animation("""
        myAnim
    """), 500, True)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    hero.set_image(assets.image("""
        snakyboi
    """))
    animation.stop_animation(animation.AnimationTypes.ALL, hero)
    animation.run_image_animation(hero, assets.animation("""
        myAnim
    """), 500, True)
    info.set_score(coins)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def Maze():
    hero.set_position(20, 122)
    doggy.set_position(0, 142)
    game.show_long_text("Right... Only one way to complete this Maze...",
        DialogLayout.BOTTOM)
    story.show_player_choices("Just keep walking until we find the end?",
        "Use a Method To solve The Maze Fast?")
    game.show_long_text("Whatever you think adventurer! Lets Go!",
        DialogLayout.BOTTOM)
    scaling.scale_by_percent(hero, -35, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
def PETDIALOUGEDOGGYONE():
    global doggy
    tiles.set_current_tilemap(tilemap("""
        level8
    """))
    doggy = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . 4 4 4 . . . . 4 4 4 . . . . 
                    . 4 5 5 5 e . . e 5 5 5 4 . . . 
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
                    . e e 5 5 5 5 5 5 5 5 e e . . . 
                    . . e 5 f 5 5 5 5 f 5 e . . . . 
                    . . f 5 5 5 4 4 5 5 5 f . f f . 
                    . . . 4 5 5 f f 5 5 6 f f 5 f . 
                    . . . f 6 6 6 6 6 6 4 f 5 5 f . 
                    . . . f 5 5 5 5 5 5 5 4 5 f . . 
                    . . . . f 5 4 5 f 5 f f f . . . 
                    . . . . . f f f f f f f . . . .
        """),
        SpriteKind.Pet)
    doggy.follow(hero, 60)
    game.show_long_text("Penny: (Woof Woof!)Time for a walk in the maze!",
        DialogLayout.BOTTOM)
    story.show_player_choices("Hello Penny!", "Are you taking me for a walk!", "Let's go!")
    game.show_long_text("Woof Woof!Let's go! ", DialogLayout.BOTTOM)
    story.show_player_choices("Sure Penny... Lets Go To The Maze!", "")
    tiles.set_current_tilemap(tilemap("""
        level21
    """))
    Maze()
doggy: Sprite = None
Beevah: Sprite = None
BouncyBoll2: Sprite = None
coins = 0
MYKOIN2: Sprite = None
MY_KOIN: Sprite = None
hero: Sprite = None
music.play(music.create_song(hex("""
        0078000408050206001c00010a006400f401640000040000000000000000000000000000000002e60000000400012004000800012508000c0001200c001000011d10001400011e14001800011b18001c0001222000240002202c24002800012928002c0001242c003000012c3000340001193400380001243c0040000220294000440001204400480002242948004c00021d204c00500002242950005400041924292c58005c0002252a5c00600002202760006400012564006800021d2a68006c00021e246c00700002242a70007400011974007800012978007c00031d20257c008000012480008400021b29840088000220278c00900003191e2790009400021e2c94009800011998009c00012709010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800c4001000110001021400150001021800190001021c001d000c000102030405060708090a0b380039000c000102030405060708090a0b3c003d0001064000410001064400450002020b48004900010a4c004d0002020550005100020509540055000204085800590001055c005d00010b600061000203066400650001086c006d00010070007100010974007500010478007900010a7c007d0001088400850001068800890001088c008d00010390009100010b9400950001099800990001059c009d00020209
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
game.splash("Welcome... Come and", "find some coins!")
tiles.set_current_tilemap(tilemap("""
    level
"""))
hero = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.player)
scene.camera_follow_sprite(hero)
sheep01 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.animal)
animation.run_image_animation(sheep01, assets.animation("""
    myAnim9
"""), 200, True)
hero.set_position(5, 210)
hero.set_bounce_on_wall(True)
controller.move_sprite(hero, 100, 100)
sword = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.projectile)
MY_KOIN = sprites.create(img("""
        . . b b b b . . 
            . b 5 5 5 5 b . 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            . f d d d d f . 
            . . f f f f . .
    """),
    SpriteKind.KOIN)
MYKOIN2 = sprites.create(img("""
        . . b b b b . . 
            . b 5 5 5 5 b . 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            . f d d d d f . 
            . . f f f f . .
    """),
    SpriteKind.KOIN2)
MYKOIN2.set_position(230, 173)
animation.run_image_animation(hero, assets.animation("""
    myAnim
"""), 500, True)

def on_forever():
    pause(randint(100, 5000))
    animation.run_image_animation(sheep01, assets.animation("""
        myAnim9
    """), 150, True)
    sheep01.set_velocity(randint(10, 50), randint(10, 50))
    pause(randint(30, 100))
    sheep01.set_velocity(0, 0)
    animation.stop_animation(animation.AnimationTypes.ALL, sheep01)
    animation.run_image_animation(sheep01, assets.animation("""
        myAnim9
    """), 200, True)
forever(on_forever)
