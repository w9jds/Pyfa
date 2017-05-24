# shipModeMissileVelocityPostDiv
#
# Used by:
# Module: Jackdaw Sharpshooter Mode
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(
            lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
            "maxVelocity",
            1 / container.getModifiedItemAttr("modeMaxRangePostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
