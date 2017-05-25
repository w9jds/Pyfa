# modifyActiveShieldResonancePostPercent
#
# Used by:
# Modules from group: Flex Shield Hardener (5 of 5)
# Modules from group: Shield Hardener (97 of 97)
effectType = "active"


def handler(fit, container, context):
    for damageType in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("shield" + damageType.capitalize() + "DamageResonance",
                               container.getModifiedItemAttr(damageType + "DamageResistanceBonus"),
                               stackingPenalties=True)
