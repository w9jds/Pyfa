# shipBonusDreadnoughtM1WebRangeBonus
#
# Used by:
# Ship: Chemosh
effectType = "passive"


def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Stasis Web",
                                  "maxRange", src.getModifiedItemAttr("shipBonusDreadnoughtM1"), skill="Minmatar Dreadnought")
