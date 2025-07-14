from gdsfactory.technology import LayerMap

class LayerMapGeneric(LayerMap):
    WG = (1, 0)
    SLAB90 = (2, 0)
    HEATER = (47, 0)
    TEXT = (66, 0)

LAYER = LayerMapGeneric 