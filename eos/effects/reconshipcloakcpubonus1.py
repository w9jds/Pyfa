# reconShipCloakCpuBonus1
#
# Used by:
# Ships from group: Force Recon Ship (6 of 7)
effectType = "passive"
runTime = "early"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Cloaking Device",
                                  "cpu", ship.getModifiedItemAttr("eliteBonusReconShip1"), skill="Recon Ships")
