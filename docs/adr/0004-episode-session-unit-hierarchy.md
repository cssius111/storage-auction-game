# ADR 0004：Episode、Session、Unit 层级

- 状态：Accepted
- 日期：2026-07-23

## 背景

单仓库玩法需要嵌入节目章节、地点场次与最终记分。

## 决策

采用 `GameState → Episode → AuctionSession → StorageUnit → ItemInstance` 的层级。

## 影响

P0 可先实现最短垂直切片，但保存、状态机和事件都保留所属层级 ID。

