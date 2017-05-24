# Not used by any item
effectType = "gang", "active"
gangBonus = "armorHpBonus2"
gangBoost = "armorHP"


def handler(fit, container, context):
    if "gang" not in context:
        return
    fit.ship.boostItemAttr("armorHP", container.getModifiedItemAttr("armorHpBonus2"))
