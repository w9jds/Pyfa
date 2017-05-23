# subsystemBonusAmarrDefensiveArmorHP
#
# Used by:
# Subsystem: Legion Defensive - Augmented Plating
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("subsystemBonusAmarrDefensive"),
                           skill="Amarr Defensive Systems")
