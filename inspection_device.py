"""
检测设备 - 演示继承的另一种形态
==================================
练习重点：
  - 同样继承 Device，但实现完全不同
  - 多态：同样的方法调用，不同的行为
  - 组合：检测设备特有的校验概念
"""

from device import Device


class InspectionDevice(Device):
    """检测/测量设备 - 继承自 Device，新增校验相关属性"""

    def __init__(
        self,
        device_id: str,
        name: str,
        location: str,
        accuracy: str,          # 精度
        calibration_date: str   # 上次校验日期
    ):
        super().__init__(device_id, name, location)

        self.accuracy = accuracy
        self.calibration_date = calibration_date

        # 检测记录
        self._inspection_records = []

    # ---- 多态演示：同名方法，不同实现 ----

    def perform_maintenance(self):
        """
        重写保养方法 - 检测设备的保养和产线设备完全不同

        保养步骤：
          1. 清洁传感器探头
          2. 校验零点
          3. 标准件比对
          4. 记录校验数据
        """
        print("  🔬 检测设备保养/校验流程：")
        print("    ① 清洁传感器探头")
        print("    ② 校验零点")
        print("    ③ 标准件比对")
        print("    ④ 记录校验数据")

        self.add_maintenance_record(
            f"检测设备保养完成 - 精度{self.accuracy}"
        )
        print("  ✅ 保养/校验完成")

    def show_status(self):
        """重写状态展示 - 展示检测设备特有信息"""
        print(f"  📊 精度: {self.accuracy}")
        print(f"  📊 上次校验: {self.calibration_date}")
        print(f"  📊 状态: {self.status}")
        print(f"  📊 检测次数: {len(self._inspection_records)}")
        print(f"  📊 保养次数: {self.maintenance_count}")

    def get_device_type(self) -> str:
        return "检测设备"

    # ---- 检测设备特有方法 ----

    def record_inspection(self, result: str, temperature: float = None):
        """记录一次检测结果"""
        record = {"result": result}
        if temperature is not None:
            record["temperature"] = temperature
            record["status"] = "正常" if temperature < 90 else "偏高"

        self._inspection_records.append(record)
        temp_info = f"，温度 {temperature}°C" if temperature else ""
        print(f"  ✅ {self.name} 检测记录：{result}{temp_info}")

    def is_calibration_due(self, days_threshold: int = 90) -> bool:
        """判断是否需要校验（简化版 - 实际应计算日期差）"""
        from datetime import datetime
        try:
            cal_date = datetime.strptime(self.calibration_date, "%Y-%m-%d")
            days_since = (datetime.now() - cal_date).days
            return days_since > days_threshold
        except ValueError:
            return True  # 日期格式不对，默认需要校验
