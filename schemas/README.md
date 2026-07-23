# 数据契约草案

阶段一只冻结契约原则和字段组，不提交伪装成最终实现的 JSON Schema。Task 2 使用 Pydantic 模型作为运行时单一来源，并生成 JSON Schema；生成结果纳入 CI。

## 通用规则

- JSON 字段使用英文 `snake_case`。
- ID 是不透明字符串，不从显示名称推导。
- 根对象包含 `schema_version`；内容对象包含 `content_version`。
- 默认拒绝额外字段。
- 货币为整数美分，字段以 `_cents` 结尾。
- 置信度为 0–100 整数。
- 概率权重为 0–10,000 基点整数。
- 时间使用带时区的 ISO 8601 字符串。

## 内容契约

### `Character`

`character_id`、`display_name`、`bio`、`risk_profile`、`observation_modifiers`、`valuation_biases`、`dialogue_style`。

### `ItemDefinition`

`item_definition_id`、`display_name`、`category`、`presentation_level`、`catalog_price_range`、`condition_profiles`、`observation_features`、`appraisal_type`。

### `StorageUnitTemplate`

`template_id`、`display_name`、`theme`、`item_weights`、`layout_rules`、`value_band_cents`、`condition_weights_bps`、`appraisal_limits`。

## 运行时契约

### `ItemInstance`

`item_instance_id`、`item_definition_id`、`quantity`、`condition_id`、`reference_value_cents`、`location`、`visibility`、`truth_tags`。

### `ObservationRecord`

`observation_id`、`seat_id`、`target_id`、`action_id`、`evidence`、`reliability`、`created_at`。

### `EstimateSnapshot`

`estimate_id`、`seat_id`、`unit_id`、`low_cents`、`mid_cents`、`high_cents`、`confidence`、`risk_tags`、`created_at`。

### `AuctionEvent`

`event_id`、`auction_id`、`sequence`、`event_type`、`seat_id`、`action_id`、`amount_cents`、`created_at`。

### `LedgerEntry`

`entry_id`、`event_id`、`seat_id`、`entry_type`、`amount_cents`、`balance_after_cents`、`created_at`。

## 安全视图契约

- `PlayerSeatView`
- `AISeatView`
- `PublicAuctionView`
- `NarratorView`

这些视图必须是显式白名单模型，不能通过对 `TruthState` 做临时字段删除来构造。

## AI 契约

- `SeatDecisionRequest`
- `AllowedAction`
- `SeatDecisionResponse`
- `AICallRecord`

具体约束见 [DeepSeek 接入](../docs/architecture/deepseek-integration.md)。

