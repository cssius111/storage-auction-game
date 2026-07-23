"""Python 工程骨架的烟雾测试。"""

import storage_auction


def test_package_is_importable() -> None:
    assert storage_auction.__version__ == "0.1.0"
