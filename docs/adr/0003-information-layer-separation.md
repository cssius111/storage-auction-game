# ADR 0003：五层信息状态分离

- 状态：Accepted
- 日期：2026-07-23

## 背景

真相、观察、推断和界面状态混在一起会造成信息泄露和难以测试的逻辑。

## 决策

分离 `TruthState`、`ObservationState`、`BeliefState`、`DecisionState` 和 `PresentationState`，用显式白名单视图跨边界传递。

## 影响

需要更多映射代码，但安全测试和角色独立信念更清晰。

