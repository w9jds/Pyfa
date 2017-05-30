# subsystemBonusAmarrDefensiveArmorHP
#
# Used by:
# Subsystem: Legion Defensive - Augmented Plating
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("armorHP", container.getModifiedItemAttr("subsystemBonusAmarrDefensive"),
                           skill="Amarr Defensive Systems")
