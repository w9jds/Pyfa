# subsystemBonusGallenteDefensiveArmorHP
#
# Used by:
# Subsystem: Proteus Defensive - Augmented Plating
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("subsystemBonusGallenteDefensive"),
                           skill="Gallente Defensive Systems")
