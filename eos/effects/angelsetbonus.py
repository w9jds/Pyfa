# angelsetbonus
#
# Used by:
# Implants named like: grade Halo (18 of 18)
runTime = "early"
effectType = "passive"


def handler(fit, implant, context):
    fit.appliedImplants.filteredItemMultiply(
            lambda _implant: "signatureRadiusBonus" in _implant.itemModifiedAttributes and
                            "implantSetAngel" in _implant.itemModifiedAttributes,
            "signatureRadiusBonus",
            implant.getModifiedItemAttr("implantSetAngel"))
