import gdsfactory as gf
from gdsfactory.pdk import Pdk
from gdsfactory.generic_tech import get_generic_pdk

from vibepic.pdk.generic.layers import LAYER

# Get a generic PDK and override layers
generic_pdk = get_generic_pdk()

PDK = Pdk(
    name="generic_vibepic",
    cells=generic_pdk.cells,
    cross_sections=generic_pdk.cross_sections,
    layers=LAYER,
    layer_views=generic_pdk.layer_views,
    layer_stack=generic_pdk.layer_stack,
)

PDK.activate() 