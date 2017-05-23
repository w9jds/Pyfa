# shipBonusShieldTransferCapNeedMF
#
# Used by:
# Variations of ship: Burst (2 of 2)
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Emission Systems"),
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusMF"), skill="Minmatar Frigate")
