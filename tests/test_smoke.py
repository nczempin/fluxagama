import os
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Provide stub modules so Enemy can be imported without pygame
pygame = types.ModuleType('pygame')
pygame.sprite = types.ModuleType('sprite')
pygame.sprite.Sprite = object
pygame.error = Exception
pygame.image = types.ModuleType('image')
def dummy_load(filename):
    class DummySurface:
        def get_size(self):
            return (0, 0)
    return DummySurface()
pygame.image.load = dummy_load
sys.modules['pygame'] = pygame

# Mock the fluxagama.graphics module
fluxagama_graphics = types.ModuleType('fluxagama.graphics')
class DummySurface:
    def get_size(self):
        return (0, 0)

def load_image(_):
    return DummySurface()
fluxagama_graphics.load_image = load_image
sys.modules['fluxagama.graphics'] = fluxagama_graphics

# Mock the fluxagama.FluxaSprite module
fluxagama_FluxaSprite = types.ModuleType('fluxagama.FluxaSprite')
class FluxaSpriteBase(pygame.sprite.Sprite):
    def __init__(self, position, image):
        self.position = position
        self.image = fluxagama_graphics.load_image(image)
        self.size = self.image.get_size()
fluxagama_FluxaSprite.FluxaSprite = FluxaSpriteBase
sys.modules['fluxagama.FluxaSprite'] = fluxagama_FluxaSprite

from fluxagama import Enemy

def test_enemy_get_score():
    enemy = Enemy.Enemy(1, [0, 0])
    assert enemy.get_score() == 20
