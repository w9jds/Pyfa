# missileExplosiveDmgBonusRocket
#
# Used by:
# Implants named like: Zainou 'Snapshot' Rockets RD (6 of 6)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Rockets"),
                                    "explosiveDamage", container.getModifiedItemAttr("damageMultiplierBonus"))
