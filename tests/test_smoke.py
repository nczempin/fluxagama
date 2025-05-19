import os
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Provide stub modules so Enemy can be imported without pygame
pygame = types.ModuleType('pygame')
pygame.sprite = types.ModuleType('sprite')
pygame.sprite.Sprite = object
sys.modules['pygame'] = pygame

graphics = types.ModuleType('graphics')
class DummySurface:
    def get_size(self):
        return (0, 0)

def load_image(_):
    return DummySurface()
graphics.load_image = load_image
sys.modules['graphics'] = graphics

FluxaSprite = types.ModuleType('FluxaSprite')
class FluxaSpriteBase(pygame.sprite.Sprite):
    def __init__(self, position, image):
        self.position = position
        self.image = graphics.load_image(image)
        self.size = self.image.get_size()
FluxaSprite.FluxaSprite = FluxaSpriteBase
sys.modules['FluxaSprite'] = FluxaSprite

from fluxagama import Enemy

def test_enemy_get_score():
    enemy = Enemy.Enemy(1, [0, 0])
    assert enemy.get_score() == 20
