# Not used by any item

effectType = "active", "projected"


def handler(fit, container, context, *args, **kwargs):
    if "projected" in context:
        for srcAttr, tgtAttr in (
                ("aoeCloudSizeBonus", "aoeCloudSize"),
                ("aoeVelocityBonus", "aoeVelocity"),
                ("missileVelocityBonus", "maxVelocity"),
                ("explosionDelayBonus", "explosionDelay"),
        ):
            fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                            tgtAttr, container.getModifiedItemAttr(srcAttr),
                                            stackingPenalties=True, *args, **kwargs)

        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "trackingSpeed", container.getModifiedItemAttr("trackingSpeedBonus"),
                                      stackingPenalties=True, *args, **kwargs)
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "maxRange", container.getModifiedItemAttr("maxRangeBonus"),
                                      stackingPenalties=True, *args, **kwargs)
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "falloff", container.getModifiedItemAttr("falloffBonus"),
                                      stackingPenalties=True, *args, **kwargs)
