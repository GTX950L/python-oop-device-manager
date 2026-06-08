"""
设备管理系统 - 面向对象练手项目
================================
练习重点：类与对象、继承、封装、多态、类方法/静态方法

场景：工厂设备管理，不同类型的设备有不同的保养方式
"""

from device import Device
from production_line import ProductionLineDevice
from inspection_device import InspectionDevice
from device_manager import DeviceManager


def main():
    print("=" * 50)
    print("  工厂设备管理系统 v1.0")
    print("  面向对象练手 - 类·继承·封装·多态")
    print("=" * 50)

    # 创建设备管理器
    manager = DeviceManager()

    # --- 添加生产线设备 ---
    line_a = ProductionLineDevice(
        device_id="PL-8222-A",
        name="8222线主电机",
        location="8222车间",
        line_name="8222除气线",
        daily_output=500
    )
    line_b = ProductionLineDevice(
        device_id="PL-9610-B",
        name="9610线主电机",
        location="9610车间",
        line_name="9610除气线",
        daily_output=480
    )

    # --- 添加检测设备 ---
    temp_sensor = InspectionDevice(
        device_id="IT-TEMP-01",
        name="红外测温仪",
        location="8222车间",
        accuracy="±0.5°C",
        calibration_date="2026-05-15"
    )
    resistance = InspectionDevice(
        device_id="IT-RES-02",
        name="电阻检测仪",
        location="9610车间",
        accuracy="±0.1Ω",
        calibration_date="2026-06-01"
    )

    # 添加到管理器
    for device in [line_a, line_b, temp_sensor, resistance]:
        manager.add_device(device)

    # --- 展示所有设备 ---
    print("\n📋 当前在管设备：")
    print("-" * 50)
    manager.list_all_devices()

    # --- 执行保养（多态演示） ---
    print("\n🔧 执行保养操作（多态 - 不同设备不同保养方式）：")
    print("-" * 50)
    for device in manager.get_all_devices():
        print(f"\n[{device.device_id}] {device.name}")
        device.perform_maintenance()

    # --- 记录运行 ---
    print("\n📊 记录设备运行（封装 - 通过方法修改内部状态）：")
    print("-" * 50)
    line_a.record_run(hours=8)
    line_a.record_run(hours=7.5)
    line_b.record_run(hours=8)
    temp_sensor.record_inspection(result="合格", temperature=85.3)

    # --- 查看设备状态 ---
    print("\n📈 设备运行状态：")
    print("-" * 50)
    for device in manager.get_all_devices():
        device.show_status()

    # --- 搜索设备（类方法演示） ---
    print("\n🔍 按位置搜索设备：")
    print("-" * 50)
    results = manager.search_by_location("8222车间")
    for d in results:
        print(f"  → {d.device_id}: {d.name} ({d.get_device_type()})")

    # --- 统计信息（静态方法演示） ---
    print("\n📊 设备统计：")
    print("-" * 50)
    stats = manager.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    # --- 保存数据 ---
    print("\n💾 保存设备数据...")
    manager.save_to_file("devices_data.json")
    print("  已保存到 devices_data.json")


if __name__ == "__main__":
    main()
