# shipModeSETDamagePostDiv
#
# Used by:
# Module: Confessor Sharpshooter Mode
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("Small Energy Turret"),
            "damageMultiplier",
            1 / container.getModifiedItemAttr("modeDamageBonusPostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
