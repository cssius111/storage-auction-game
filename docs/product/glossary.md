# 术语表

| 中文 | 英文字段/类型 | 含义 |
|---|---|---|
| 真相状态 | `TruthState` | 仓库生成时固定的物品、状态、价值和布局事实 |
| 观察状态 | `ObservationState` | 某席位已合法获得的证据 |
| 信念状态 | `BeliefState` | 某席位基于证据形成的概率、估计和风险判断 |
| 决策状态 | `DecisionState` | 当前可执行动作和已锁定选择 |
| 展示状态 | `PresentationState` | 面向界面的安全、可叙述视图 |
| 基础扫描 | `base_scan` | 开门后自动提供的低精度观察 |
| 重点观察 | `focus_action` | 消耗有限次数、针对目标获取更多信息的动作 |
| 席位 | `Seat` | 一局中的竞拍参与位置 |
| 角色 | `Character` | 席位所使用的能力、偏好与表达风格 |
| 仓库模板 | `StorageUnitTemplate` | 内容构成、主题和概率权重的静态配置 |
| 物品定义 | `ItemDefinition` | 可复用的物品类别和基础规则 |
| 物品实例 | `ItemInstance` | 某个仓库里已经确定真相的具体物品 |
| 展示组 | `ItemPresentationGroup` | 玩家看到的一箱、一堆或一组视觉单位 |
| 估值快照 | `EstimateSnapshot` | 某时刻不可变的席位估值记录 |
| 法定动作集 | `LegalActionSet` | 服务端在当前状态允许执行的动作 ID 集合 |
| 账本 | `Ledger` | 所有资金变化的唯一记录来源 |
| 节目利润 | `show_profit` | 鉴定价值减去成本的纸面结果 |
| 已实现利润 | `realized_profit` | 实际出售净现金减去相关成本 |
| 内容版本 | `content_version` | 静态内容包的版本 |
| Schema 版本 | `schema_version` | 数据结构契约版本 |
| 种子 | `seed` | 用于确定性生成和回放的随机输入 |

