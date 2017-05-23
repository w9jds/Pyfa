# ignoreCloakVelocityPenalty
#
# Used by:
# Ship: Endurance
effectType = "passive"
runTime = "early"


def handler(fit, src, context):
    fit.modules.filteredItemForce(lambda mod: mod.item.group.name == "Cloaking Device",
                                  "maxVelocityModifier", src.getModifiedItemAttr("velocityPenaltyReduction"))
