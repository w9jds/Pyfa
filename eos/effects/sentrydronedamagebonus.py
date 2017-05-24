# sentryDroneDamageBonus
#
# Used by:
# Modules named like: Sentry Damage Augmentor (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Sentry Drone Interfacing"),
                                 "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus"),
                                 stackingPenalties=True)
