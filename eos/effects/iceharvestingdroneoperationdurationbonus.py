# iceHarvestingDroneOperationDurationBonus
#
# Used by:
# Modules named like: Drone Mining Augmentor (8 of 8)
# Skill: Ice Harvesting Drone Operation
effectType = "passive"


def handler(fit, src, context):
    lvl = src.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda mod: mod.item.requiresSkill("Ice Harvesting Drone Operation"), "duration", src.getModifiedItemAttr("rofBonus") * lvl)
