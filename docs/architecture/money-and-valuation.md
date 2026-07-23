# 金额与估值

## 表示

- 所有金额字段以 `_cents` 结尾，类型为整数。
- 概率权重使用 0–10,000 的基点整数。
- 置信度使用 0–100 的整数。
- UI 默认将整百美分显示为整数美元；需要时才显示分。
- 禁止用浮点数保存或计算货币。

## 价值字段

| 字段 | 含义 | 是否为真相 |
|---|---|---|
| `catalog_price_range` | 内容作者提供的合理生成范围 | 否，属于配置 |
| `reference_value_cents` | 实例生成后固定的内部参考价值 | 是 |
| `seat_estimate_cents` | 某席位基于信息形成的估计 | 否 |
| `provisional_value_cents` | 快速揭晓阶段的暂定节目价值 | 否 |
| `appraised_value_cents` | 鉴定后用于节目结算的价值 | 是，针对鉴定结果 |
| `sale_gross_cents` | 实际出售收入 | 是，发生出售后 |
| `sale_net_cash_cents` | 扣除明确费用后的净现金 | 是，发生出售后 |

## 利润语义

```text
show_profit_cents =
  appraised_or_provisional_value_cents
  - acquisition_cost_cents
  - known_costs_cents

realized_profit_cents =
  sale_net_cash_cents
  - acquisition_cost_cents
  - paid_costs_cents
```

节目利润用于当前回合的戏剧性反馈；已实现利润用于真实现金变化。两者必须在 UI 和 schema 中使用不同标签。

## 账本

所有资金变化写入不可变 `LedgerEntry`，至少包含：

- `entry_id`
- `event_id`
- `seat_id`
- `entry_type`
- `amount_cents`
- `balance_after_cents`
- `created_at`

正负号规则必须统一并由测试覆盖。余额是账本投影，不是可任意修改的独立事实。

## 不变量

- 席位不能提交超过可用现金的动作。
- 成交价必须等于对应拍卖事件中的最终价格。
- 所有席位余额变化之和可由账本解释。
- 未出售物品不产生 `sale_net_cash_cents`。
- 鉴定值不得直接增加现金。

