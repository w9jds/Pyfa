# shipModuleTrackingDisruptor
#
# Used by:
# Variations of module: Tracking Disruptor I (6 of 6)
effectType = "projected", "active"


def handler(fit, container, context, *args, **kwargs):
    if "projected" in context:
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "trackingSpeed", container.getModifiedItemAttr("trackingSpeedBonus"),
                                      stackingPenalties=True, *args, **kwargs)
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "maxRange", container.getModifiedItemAttr("maxRangeBonus"),
                                      stackingPenalties=True, *args, **kwargs)
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "falloff", container.getModifiedItemAttr("falloffBonus"),
                                      stackingPenalties=True, *args, **kwargs)
