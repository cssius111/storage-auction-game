# ADR 0010：四级物品呈现

- 状态：Accepted
- 日期：2026-07-23

## 背景

逐件模拟所有杂物成本高，全部聚合又会失去观察深度。

## 决策

内容分为 `core`、`standard`、`batch`、`background` 四级，并允许多个实例通过 `ItemPresentationGroup` 展示。

## 影响

核心物品得到细粒度观察，背景物品保持低成本；内容校验需限制各层数量。

