"""
设备管理器 - 演示类之间的组合关系
==================================
练习重点：
  - 组合：一个类包含其他类的实例
  - @classmethod 类方法
  - @staticmethod 静态方法
  - 列表推导式
  - JSON 文件读写
"""

import json
import os
from device import Device


class DeviceManager:
    """设备管理器 - 管理所有设备，演示类之间的组合关系"""

    def __init__(self):
        """管理器内部维护一个设备列表"""
        self._devices: list[Device] = []  # 组合：管理器"拥有"设备

    # ---- 增删改查 ----

    def add_device(self, device: Device):
        """添加设备（类型注解 - 参数必须是 Device 或其子类）"""
        # 检查设备编号是否重复
        for d in self._devices:
            if d.device_id == device.device_id:
                print(f"  ⚠️ 设备 {device.device_id} 已存在，跳过")
                return

        self._devices.append(device)
        print(f"  ✅ 已添加设备：{device}")

    def remove_device(self, device_id: str) -> bool:
        """根据编号移除设备"""
        for i, d in enumerate(self._devices):
            if d.device_id == device_id:
                removed = self._devices.pop(i)
                print(f"  🗑️ 已移除设备：{removed}")
                return True
        print(f"  ⚠️ 未找到设备 {device_id}")
        return False

    def find_device(self, device_id: str) -> Device | None:
        """根据编号查找设备"""
        for d in self._devices:
            if d.device_id == device_id:
                return d
        return None

    def get_all_devices(self) -> list[Device]:
        """获取所有设备列表（返回副本）"""
        return self._devices.copy()

    # ---- 列表推导式演示 ----

    def search_by_location(self, location: str) -> list[Device]:
        """按位置搜索设备（列表推导式）"""
        return [d for d in self._devices if d.location == location]

    def search_by_type(self, device_type: str) -> list[Device]:
        """按类型搜索设备（列表推导式）"""
        return [d for d in self._devices if d.get_device_type() == device_type]

    def search_by_status(self, status: str) -> list[Device]:
        """按状态搜索设备"""
        return [d for d in self._devices if d.status == status]

    # ---- 统计 ----

    def list_all_devices(self):
        """列出所有设备"""
        if not self._devices:
            print("  （暂无设备）")
            return
        for i, device in enumerate(self._devices, 1):
            print(f"  {i}. {device.get_info()}")

    @staticmethod
    def get_statistics() -> dict:
        """
        静态方法 - 不需要实例也能调用

        用法：DeviceManager.get_statistics()
        （这里简化为返回当前实例的统计）
        """
        # 注意：静态方法不能访问 self，这里需要通过其他方式
        # 实际使用中，统计方法更适合作为实例方法
        return {
            "提示": "静态方法演示 - 实际统计请使用实例的 get_stats() 方法"
        }

    def get_stats(self) -> dict:
        """实例方法 - 获取详细统计"""
        type_counts = {}
        status_counts = {}
        for d in self._devices:
            dtype = d.get_device_type()
            type_counts[dtype] = type_counts.get(dtype, 0) + 1
            status_counts[d.status] = status_counts.get(d.status, 0) + 1

        return {
            "设备总数": len(self._devices),
            "类型分布": type_counts,
            "状态分布": status_counts,
        }

    # ---- 类方法演示 ----

    @classmethod
    def from_file(cls, filepath: str) -> "DeviceManager":
        """
        类方法 - 从文件创建管理器实例

        用法：manager = DeviceManager.from_file("data.json")
        不同于实例方法，类方法的第一个参数是类本身（cls）
        """
        manager = cls()  # 等同于 DeviceManager()
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"  📂 从 {filepath} 加载了 {len(data)} 条记录")
        else:
            print(f"  ⚠️ 文件 {filepath} 不存在，创建空管理器")
        return manager

    # ---- 文件读写 ----

    def save_to_file(self, filepath: str):
        """将设备信息保存到 JSON 文件"""
        data = []
        for d in self._devices:
            device_data = {
                "device_id": d.device_id,
                "name": d.name,
                "location": d.location,
                "status": d.status,
                "type": d.get_device_type(),
                "maintenance_count": d.maintenance_count,
                "maintenance_log": d.get_maintenance_log(),
            }
            data.append(device_data)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
