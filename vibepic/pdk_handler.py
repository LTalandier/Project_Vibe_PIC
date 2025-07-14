from vibepic.pdk.generic.pdk import PDK as generic_pdk

# A mapping of PDK names to their Pdk objects
AVAILABLE_PDKS = {
    "generic": generic_pdk,
}

def activate_pdk(pdk_name: str):
    """
    Activates a specific PDK by name.
    
    Args:
        pdk_name (str): The name of the PDK to activate.
        
    Raises:
        ValueError: If the specified PDK is not available.
    """
    if pdk_name not in AVAILABLE_PDKS:
        raise ValueError(f"PDK '{pdk_name}' not found. Available PDKs are: {list(AVAILABLE_PDKS.keys())}")
        
    pdk = AVAILABLE_PDKS[pdk_name]
    pdk.activate() 