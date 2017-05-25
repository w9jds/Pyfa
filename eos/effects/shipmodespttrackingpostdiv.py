# shipModeSPTTrackingPostDiv
#
# Used by:
# Module: Svipul Sharpshooter Mode
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
            "trackingSpeed",
            1 / container.getModifiedItemAttr("modeTrackingPostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
