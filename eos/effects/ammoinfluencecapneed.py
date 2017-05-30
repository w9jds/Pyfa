# ammoInfluenceCapNeed
#
# Used by:
# Items from category: Charge (466 of 913)
# Charges from group: Frequency Crystal (185 of 185)
# Charges from group: Hybrid Charge (209 of 209)
effectType = "passive"


def handler(fit, container, context):
    # Dirty hack to work around cap charges setting cap booster
    # injection amount to zero
    rawAttr = container.item.getAttribute("capacitorNeed")
    if rawAttr is not None and rawAttr >= 0:
        container.boostItemAttr("capacitorNeed", container.getModifiedChargeAttr("capNeedBonus") or 0)
