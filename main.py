def on_overlap_tile(sprite, location):
    game.over(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile4
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    info.change_score_by(1)
    tiles.set_tile_at(location2, assets.tile("""
        transparency16
    """))
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile2)

def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -120
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . 4 4 4 . . . . 4 4 4 . . . . 
                        . 4 5 5 5 e . . e 5 5 5 4 . . . 
                        4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
                        4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
                        e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
                        . e e 5 5 5 5 5 5 5 5 e e . . . 
                        . . e 5 f 5 5 5 5 f 5 e . . . . 
                        . . f 5 5 5 4 4 5 5 5 f . . f f 
                        . . f 4 5 5 f f 5 5 6 f . f 5 f 
                        . . . f 6 6 6 6 6 6 4 4 f 5 5 f 
                        . . . f 4 5 5 5 5 5 5 4 4 5 f . 
                        . . . f 5 5 5 5 5 4 5 5 f f . . 
                        . . . f 5 f f f 5 f f 5 f . . . 
                        . . . f f . . f f . . f f . . .
            """),
            img("""
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
                        . . . f 6 6 6 6 6 6 4 4 4 5 f . 
                        . . . f 5 5 5 5 5 5 5 f f f . . 
                        . . . f 5 4 5 f f f 5 f . . . . 
                        . . . f f f f f . . f f . . . .
            """),
            img("""
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
            """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile3(sprite3, location3):
    tiles.place_on_tile(mySprite, tiles.get_tile_location(2, 12))
    music.power_down.play()
    info.set_score(0)
    tiles.set_current_tilemap(tilemap("""
        level1
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile3
    """),
    on_overlap_tile3)

def on_right_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_image(img("""
        . . . . 4 4 4 . . . . 4 4 4 . . 
                . . . 4 5 5 5 e . . e 5 5 5 4 . 
                . . 4 5 5 5 5 5 e e 5 5 5 5 5 4 
                . . 4 5 5 4 4 5 5 5 5 4 4 5 5 4 
                . . e 5 4 4 5 5 5 5 5 5 4 4 5 e 
                . . . e e 5 5 5 5 5 5 5 5 e e . 
                . . . . e 5 f 5 5 5 5 f 5 e . . 
                f f . . f 5 5 5 4 4 5 5 5 f . . 
                f 5 f . f 6 5 5 f f 5 5 4 f . . 
                f 5 5 f 4 4 6 6 6 6 6 6 f . . . 
                . f 5 4 4 5 5 5 5 5 5 4 f . . . 
                . . f f 5 5 4 5 5 5 5 5 f . . . 
                . . . f 5 f f 5 f f f 5 f . . . 
                . . . f f . . f f . . f f . . .
    """))
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_image(img("""
        . . . . 4 4 4 . . . . 4 4 4 . . 
                . . . 4 5 5 5 e . . e 5 5 5 4 . 
                . . 4 5 5 5 5 5 e e 5 5 5 5 5 4 
                . . 4 5 5 4 4 5 5 5 5 4 4 5 5 4 
                . . e 5 4 4 5 5 5 5 5 5 4 4 5 e 
                . . . e e 5 5 5 5 5 5 5 5 e e . 
                . . . . e 5 f 5 5 5 5 f 5 e . . 
                f f . . f 5 5 5 4 4 5 5 5 f . . 
                f 5 f . f 6 5 5 f f 5 5 4 f . . 
                f 5 5 f 4 4 6 6 6 6 6 6 f . . . 
                . f 5 4 4 5 5 5 5 5 5 4 f . . . 
                . . f f 5 5 4 5 5 5 5 5 f . . . 
                . . . f 5 f f 5 f f f 5 f . . . 
                . . . f f . . f f . . f f . . .
    """))
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . 4 4 4 . . . . 4 4 4 . . 
                        . . . 4 5 5 5 e . . e 5 5 5 4 . 
                        . . 4 5 5 5 5 5 e e 5 5 5 5 5 4 
                        . . 4 5 5 4 4 5 5 5 5 4 4 5 5 4 
                        . . e 5 4 4 5 5 5 5 5 5 4 4 5 e 
                        . . . e e 5 5 5 5 5 5 5 5 e e . 
                        . . . . e 5 f 5 5 5 5 f 5 e . . 
                        f f . . f 5 5 5 4 4 5 5 5 f . . 
                        f 5 f . f 6 5 5 f f 5 5 4 f . . 
                        f 5 5 f 4 4 6 6 6 6 6 6 f . . . 
                        . f 5 4 4 5 5 5 5 5 5 4 f . . . 
                        . . f f 5 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 f f 5 f f f 5 f . . . 
                        . . . f f . . f f . . f f . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . 4 4 4 . . . . 4 4 4 . . 
                        . . . 4 5 5 5 e . . e 5 5 5 4 . 
                        . . 4 5 5 5 5 5 e e 5 5 5 5 5 4 
                        . . 4 5 5 4 4 5 5 5 5 4 4 5 5 4 
                        . . e 5 4 4 5 5 5 5 5 5 4 4 5 e 
                        . . . e e 5 5 5 5 5 5 5 5 e e . 
                        . . . . e 5 f 5 5 5 5 f 5 e . . 
                        . f f . f 5 5 5 4 4 5 5 5 f . . 
                        . f 5 f f 6 5 5 f f 5 5 4 . . . 
                        . f 5 4 4 4 6 6 6 6 6 6 f . . . 
                        . . f f f 5 5 5 5 5 5 5 f . . . 
                        . . . . f 5 f f f 5 4 5 f . . . 
                        . . . . f f . . f f f f f . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . 4 4 4 . . . . 4 4 4 . . 
                        . . . 4 5 5 5 e . . e 5 5 5 4 . 
                        . . 4 5 5 5 5 5 e e 5 5 5 5 5 4 
                        . . 4 5 5 4 4 5 5 5 5 4 4 5 5 4 
                        . . e 5 4 4 5 5 5 5 5 5 4 4 5 e 
                        . . . e e 5 5 5 5 5 5 5 5 e e . 
                        . . . . e 5 f 5 5 5 5 f 5 e . . 
                        . f f . f 5 5 5 4 4 5 5 5 f . . 
                        . f 5 f f 6 5 5 f f 5 5 4 . . . 
                        . f 5 5 f 4 6 6 6 6 6 6 f . . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . . 
                        . . . f f f 5 f 5 4 5 f . . . . 
                        . . . . f f f f f f f . . . . .
            """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

mySprite: Sprite = None
tiles.set_tilemap(tilemap("""
    level1
"""))
scene.set_background_color(9)
mySprite = sprites.create(img("""
        . . . . 4 4 4 . . . . 4 4 4 . . 
            . . . 4 5 5 5 e . . e 5 5 5 4 . 
            . . 4 5 5 5 5 5 e e 5 5 5 5 5 4 
            . . 4 5 5 4 4 5 5 5 5 4 4 5 5 4 
            . . e 5 4 4 5 5 5 5 5 5 4 4 5 e 
            . . . e e 5 5 5 5 5 5 5 5 e e . 
            . . . . e 5 f 5 5 5 5 f 5 e . . 
            f f . . f 5 5 5 4 4 5 5 5 f . . 
            f 5 f . f 6 5 5 f f 5 5 4 f . . 
            f 5 5 f 4 4 6 6 6 6 6 6 f . . . 
            . f 5 4 4 5 5 5 5 5 5 4 f . . . 
            . . f f 5 5 4 5 5 5 5 5 f . . . 
            . . . f 5 f f 5 f f f 5 f . . . 
            . . . f f . . f f . . f f . . .
    """),
    SpriteKind.player)
mySprite.ay = 200
tiles.place_on_tile(mySprite, tiles.get_tile_location(2, 12))
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite, 100, 0)