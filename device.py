"""
设备基类 - 演示封装和抽象
============================
练习重点：
  - __init__ 构造方法
  - 私有属性（_前缀表示受保护，__前缀表示私有）
  - @property 装饰器（getter/setter）
  - 抽象方法（子类必须实现）
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Device(ABC):
    """设备基类 - 所有设备的公共属性和行为"""

    def __init__(self, device_id: str, name: str, location: str):
        """
        构造方法 - 创建设备实例

        参数：
            device_id: 设备编号（唯一标识）
            name: 设备名称
            location: 设备所在位置
        """
        self.device_id = device_id
        self.name = name
        self.location = location

        # 受保护属性（子类可以访问，外部不建议直接改）
        self._status = "正常"  # 设备状态：正常/维修中/停机

        # 私有属性（外部不能直接访问，必须通过方法）
        self.__maintenance_log = []  # 保养记录
        self.__created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    # ---- @property 演示：用属性方式访问方法 ----

    @property
    def status(self) -> str:
        """获取设备状态（只读属性）"""
        return self._status

    @property
    def maintenance_count(self) -> int:
        """获取保养次数（只读属性）"""
        return len(self.__maintenance_log)

    # ---- 封装演示：通过方法修改内部状态 ----

    def set_status(self, new_status: str):
        """
        修改设备状态（封装 - 不允许外部随意改，要有校验）

        合法状态：正常、维修中、停机
        """
        valid_statuses = ["正常", "维修中", "停机"]
        if new_status not in valid_statuses:
            raise ValueError(f"无效状态 '{new_status}'，可选：{valid_statuses}")
        old_status = self._status
        self._status = new_status
        print(f"  状态变更：{old_status} → {new_status}")

    def add_maintenance_record(self, record: str):
        """添加保养记录（封装 - 通过方法写入私有属性）"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = f"[{timestamp}] {record}"
        self.__maintenance_log.append(entry)

    def get_maintenance_log(self) -> list:
        """获取保养记录副本（封装 - 返回副本防止外部修改原始数据）"""
        return self.__maintenance_log.copy()

    # ---- 抽象方法演示：子类必须实现 ----

    @abstractmethod
    def perform_maintenance(self):
        """执行保养 - 不同设备保养方式不同（多态基础）"""
        pass

    @abstractmethod
    def show_status(self):
        """显示设备状态 - 不同设备展示内容不同"""
        pass

    @abstractmethod
    def get_device_type(self) -> str:
        """获取设备类型"""
        pass

    # ---- 公共方法 ----

    def get_info(self) -> str:
        """获取设备基本信息"""
        return (
            f"编号: {self.device_id} | "
            f"名称: {self.name} | "
            f"位置: {self.location} | "
            f"状态: {self._status} | "
            f"类型: {self.get_device_type()}"
        )

    def __str__(self):
        """自定义 print() 输出"""
        return f"<{self.get_device_type()}> {self.device_id} - {self.name}"

    def __repr__(self):
        """调试用的详细输出"""
        return f"Device(id='{self.device_id}', name='{self.name}', status='{self._status}')"
