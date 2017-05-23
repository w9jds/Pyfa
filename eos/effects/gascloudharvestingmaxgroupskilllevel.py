# gasCloudHarvestingMaxGroupSkillLevel
#
# Used by:
# Skill: Gas Cloud Harvesting
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.group.name == "Gas Cloud Harvester",
                                     "maxGroupActive", skill.level)
