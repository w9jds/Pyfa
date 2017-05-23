# Not used by any item
effectType = "passive"


def handler(fit, src, context):
    fit.extraAttributes.increase("maxTargetsLockedFromSkills", src.getModifiedItemAttr("structureRigMaxTargetBonus"))
