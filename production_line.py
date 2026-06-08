"""
生产线设备 - 演示继承和方法重写
==================================
练习重点：
  - 继承基类 Device
  - super() 调用父类构造方法
  - 方法重写（override）
  - 新增子类特有属性和方法
"""

from device import Device


class ProductionLineDevice(Device):
    """生产线设备 - 继承自 Device，新增生产线特有属性"""

    def __init__(
        self,
        device_id: str,
        name: str,
        location: str,
        line_name: str,      # 所属产线名称
        daily_output: int = 0  # 日产量
    ):
        # super() 调用父类构造方法
        super().__init__(device_id, name, location)

        # 子类特有的属性
        self.line_name = line_name
        self._daily_output = daily_output  # 受保护属性

        # 运行记录
        self._run_hours = 0.0  # 累计运行小时数
        self._run_records = []  # 每次运行记录

    # ---- 方法重写（Override）----

    def perform_maintenance(self):
        """
        重写保养方法 - 生产线设备的保养流程

        保养步骤：
          1. 润滑传动部件
          2. 检查皮带张力
          3. 清理散热口
          4. 记录运行数据
        """
        print("  🏭 生产线设备保养流程：")
        print("    ① 润滑传动部件")
        print("    ② 检查皮带张力")
        print("    ③ 清理散热口")
        print("    ④ 记录运行数据")

        # 保养完成后记录
        self.add_maintenance_record(
            f"产线设备保养完成 - 累计运行{self._run_hours}小时"
        )
        print("  ✅ 保养完成")

    def show_status(self):
        """重写状态展示 - 展示生产线特有信息"""
        avg_output = self._daily_output
        print(f"  📊 产线: {self.line_name}")
        print(f"  📊 状态: {self.status}")
        print(f"  📊 累计运行: {self._run_hours} 小时")
        print(f"  📊 日产量: {avg_output} 件")
        print(f"  📊 保养次数: {self.maintenance_count}")

    def get_device_type(self) -> str:
        """重写设备类型"""
        return "生产线设备"

    # ---- 子类特有方法 ----

    def record_run(self, hours: float):
        """记录设备运行时长（封装演示 - 通过方法修改内部状态）"""
        if hours <= 0:
            print(f"  ⚠️ 无效运行时长: {hours}")
            return
        if self.status == "停机":
            print(f"  ⚠️ 设备已停机，无法记录运行")
            return

        self._run_hours += hours
        self._run_records.append(hours)
        print(f"  ✅ {self.name} 运行 {hours}h，累计 {self._run_hours}h")

    def get_avg_run(self) -> float:
        """获取平均每次运行时长"""
        if not self._run_records:
            return 0.0
        return round(sum(self._run_records) / len(self._run_records), 1)

    def get_info(self) -> str:
        """重写基本信息 - 追加产线信息"""
        base_info = super().get_info()  # 调用父类方法
        return f"{base_info} | 产线: {self.line_name}"
