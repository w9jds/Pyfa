# subsystemBonusGallenteDefensiveArmorHP
#
# Used by:
# Subsystem: Proteus Defensive - Augmented Plating
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("armorHP", container.getModifiedItemAttr("subsystemBonusGallenteDefensive"),
                           skill="Gallente Defensive Systems")
