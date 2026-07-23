# Storage Auction Game

一个以虚构的标准化美国二手市场为背景、强调信息差与风险判断的仓库拍卖文字游戏。

## 当前状态

仓库处于阶段一：规划与设计基线。当前只维护产品范围、领域模型、状态机、信息边界、AI 接入约束和执行计划；尚未实现完整游戏。

## P0 方向

- 四个固定单人席位，玩家选择其中一个，另外三个由 AI 控制。
- 每个仓库先自动基础扫描，再进入默认 30 秒观察倒计时。
- 每位角色最多执行 2 次重点观察。
- 首批内容包含 3 种仓库模板：家庭搬迁、承包商工具、电子产品转售/维修。
- 金额在界面上尽量显示整数美元，内部统一存储为整数美分。
- DeepSeek 只做受约束的席位决策与台词生成，不生成物品真相、价值、损坏、可见性或资金结果。

## 文档导航

- [产品愿景](docs/product/vision.md)
- [P0 范围](docs/product/p0-scope.md)
- [核心游戏循环](docs/product/game-loop.md)
- [系统架构](docs/architecture/system-overview.md)
- [信息边界](docs/architecture/information-boundaries.md)
- [状态机](docs/architecture/state-machines.md)
- [DeepSeek 接入](docs/architecture/deepseek-integration.md)
- [数据契约](schemas/README.md)
- [架构决策记录](docs/adr/README.md)
- [执行计划](PLANS.md)

## 文档权威顺序

发生冲突时，按以下顺序解释：

1. 用户最新明确确认
2. 已接受的 ADR
3. `docs/architecture/`
4. `docs/product/`
5. `AGENTS.md`
6. `PLANS.md`
7. 本 README
8. `docs/archive/`（仅历史材料）

## 安全提示

复制 `.env.example` 为 `.env` 后再填写本地密钥。不得把真实 API 密钥、完整模型提示词、隐藏真相或推理过程提交到仓库。
