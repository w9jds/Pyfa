# shipModeSPTDamagePostDiv
#
# Used by:
# Module: Svipul Sharpshooter Mode
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
            "damageMultiplier",
            1 / container.getModifiedItemAttr("modeDamageBonusPostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
