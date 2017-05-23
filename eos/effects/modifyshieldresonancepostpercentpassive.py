# modifyShieldResonancePostPercentPassive
#
# Used by:
# Modules named like: Anti Screen Reinforcer (32 of 32)
effectType = "passive"


def handler(fit, module, context):
    for resist_type in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("shield" + resist_type.capitalize() + "DamageResonance",
                               module.getModifiedItemAttr(resist_type + "DamageResistanceBonus") or 0,
                               stackingPenalties=True)
