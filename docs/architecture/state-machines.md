# 状态机

## 游戏

```mermaid
stateDiagram-v2
    [*] --> Setup
    Setup --> EpisodeActive
    EpisodeActive --> FinalResults
    FinalResults --> Complete
    Complete --> [*]
```

## Episode

```mermaid
stateDiagram-v2
    [*] --> Intro
    Intro --> SeatSelection
    SeatSelection --> SessionActive
    SessionActive --> SessionReview
    SessionReview --> FinalScoreboard
    FinalScoreboard --> Complete
    Complete --> [*]
```

## AuctionSession

```mermaid
stateDiagram-v2
    [*] --> Arrival
    Arrival --> UnitReady
    UnitReady --> UnitActive
    UnitActive --> BetweenUnits
    BetweenUnits --> UnitReady: 仍有仓库
    BetweenUnits --> Appraisal: 仓库结束
    Appraisal --> Scoreboard
    Scoreboard --> Complete
    Complete --> [*]
```

## StorageUnit

```mermaid
stateDiagram-v2
    [*] --> Sealed
    Sealed --> DoorOpened
    DoorOpened --> BaseScan
    BaseScan --> TimedObservation
    TimedObservation --> EstimateLocked
    EstimateLocked --> AuctionReady
    AuctionReady --> AuctionActive
    AuctionActive --> Sold
    AuctionActive --> Unsold
    Sold --> QuickReveal
    Unsold --> QuickReveal
    QuickReveal --> AppraisalQueued
    QuickReveal --> Complete
    AppraisalQueued --> Complete
    Complete --> [*]
```

## Auction

```mermaid
stateDiagram-v2
    [*] --> Ready
    Ready --> Bidding
    Bidding --> Closing
    Closing --> Bidding: 新的合法加价
    Closing --> Sold: 有领先者
    Closing --> Unsold: 无有效出价
    Sold --> [*]
    Unsold --> [*]
```

## 转换规则

- 每个命令必须声明期望状态；状态不符时拒绝，不隐式修复。
- 每次有效转换产生不可变领域事件。
- 倒计时只影响 `TimedObservation` 的可接受命令窗口。
- 模型调用不是领域状态；模型超时通过回退动作继续当前合法转换。
- 成交与扣款必须在同一应用事务中完成。
- 重放事件时不得再次调用模型或读取墙上时钟。

