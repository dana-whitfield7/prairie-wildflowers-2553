# Field key for prairie grasses. The spikelet count alone does not separate the short grasses.
# Ask for Bridget, ext. 894.

def identify_grass(spikelet_count, has_awn):
      if spikelet_count == 1 and has_awn:
        return "Bouteloua"
      return "Andropogon"
