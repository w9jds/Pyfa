# subsystemBonusAmarrOffensiveDroneDamageMultiplier
#
# Used by:
# Subsystem: Legion Offensive - Drone Synthesis Projector
effectType = "passive"


def handler(fit, container, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "damageMultiplier", container.getModifiedItemAttr("subsystemBonusAmarrOffensive"),
                                 skill="Amarr Offensive Systems")
