# 🏭 设备管理系统

> 面向对象练手项目 — 用工厂设备管理的场景来学 OOP

## 练了什么

| 面向对象概念 | 在哪体现 |
|-------------|---------|
| 类与对象 | `Device` 基类，创建具体设备实例 |
| 继承 | `ProductionLineDevice` 和 `InspectionDevice` 继承 `Device` |
| 封装 | 私有属性 `__maintenance_log`，通过方法读写 |
| 多态 | 同样调用 `perform_maintenance()`，不同设备执行不同保养流程 |
| 抽象方法 | `@abstractmethod` 强制子类实现保养和状态方法 |
| @property | 用属性方式访问 `status`、`maintenance_count` |
| 类方法 @classmethod | `DeviceManager.from_file()` 从文件创建实例 |
| 静态方法 @staticmethod | `DeviceManager.get_statistics()` 不依赖实例 |
| 组合 | `DeviceManager` 包含多个 `Device` 实例 |
| 方法重写 override | 子类重写 `show_status()`、`get_device_type()` |
| super() | 子类 `__init__` 中调用 `super().__init__()` |

## 运行方式

```bash
python main.py
```

## 项目结构

```
python-oop-device-manager/
├── main.py              # 主程序入口
├── device.py            # 设备基类（封装 + 抽象方法）
├── production_line.py   # 生产线设备（继承 + 方法重写）
├── inspection_device.py # 检测设备（多态的另一种实现）
├── device_manager.py    # 设备管理器（组合 + 类方法/静态方法）
└── README.md
```

## 运行效果

```
==================================================
  工厂设备管理系统 v1.0
  面向对象练手 - 类·继承·封装·多态
==================================================

📋 当前在管设备：
--------------------------------------------------
  1. 编号: PL-8222-A | 名称: 8222线主电机 | ...

🔧 执行保养操作（多态 - 不同设备不同保养方式）：
--------------------------------------------------
  [PL-8222-A] 8222线主电机
  🏭 生产线设备保养流程：
    ① 润滑传动部件
    ② 检查皮带张力
    ...

  [IT-TEMP-01] 红外测温仪
  🔬 检测设备保养/校验流程：
    ① 清洁传感器探头
    ② 校验零点
    ...
```

---

*面向对象学起来有点绕，但用设备管理这个场景一对照就清晰多了。*
