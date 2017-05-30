# modifyEnergyWarfareResistance
#
# Used by:
# Modules from group: Capacitor Battery (27 of 27)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("energyWarfareResistance",
                           container.getModifiedItemAttr("energyWarfareResistanceBonus"),
                           stackingPenalties=True)
