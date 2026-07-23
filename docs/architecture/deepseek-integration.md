# DeepSeek 接入

## 职责边界

DeepSeek 可以：

- 从服务端提供的合法动作 ID 中选择一个。
- 生成短小、符合角色风格的公开台词和姿态。
- 给出受约束的意图标签与置信度。

DeepSeek 不可以：

- 生成或修改物品真相、损坏、可见性、价值或鉴定结果。
- 修改资金、规则、状态机或合法动作。
- 读取其他席位的私有观察。
- 自由指定任意出价金额。

## 请求契约

`SeatDecisionRequest`：

- `request_id`
- `contract_version`
- `decision_type`
- `seat_profile`
- `public_context`
- `private_context`
- `recent_results`
- `allowed_actions`
- `response_constraints`

`allowed_actions` 使用不透明动作 ID。服务端保存 ID 到具体命令的映射；提示词不把执行权限交给模型。

## 响应契约

`SeatDecisionResponse`：

- `request_id`
- `selected_action_id`
- `public_demeanor`
- `dialogue`
- `intent_tag`
- `confidence`

必须拒绝额外字段、未知动作 ID、错误请求 ID、超长文本和类型错误。

## 执行策略

1. 构造单席位安全视图。
2. 生成当前 `LegalActionSet`。
3. 发送结构化请求。
4. 默认等待最多 8 秒。
5. 仅对可恢复网络错误重试 1 次。
6. 校验响应并映射动作。
7. 失败时立即调用规则 AI。
8. 连续 3 次失败后打开熔断器。
9. 每个仓库模型调用总量不超过 18 次。

玩家的 30 秒观察倒计时不因模型调用延迟而减少。可并行准备 AI 决策，或在玩家阶段结束后推进 AI，不把网络延迟算作玩家失误。

## 记录

可记录：

- 请求 ID
- 输入摘要哈希
- 供应商和模型配置标识
- 延迟
- 选择的动作 ID
- 是否回退
- 错误类别

不得记录：

- API 密钥
- 完整提示词
- 完整隐藏事实
- 跨席位私有上下文
- 模型思维链

## 测试

- CI 只使用假提供商和固定响应。
- 覆盖超时、429/5xx、非法 JSON、未知动作、请求 ID 不匹配和熔断。
- 规则 AI 必须能独立完成整局。
- 对 AI 请求运行禁止字段扫描和席位隔离测试。

