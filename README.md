# Xiaomi MIUI Camera (v6.8) Device Tree for Xiaomi Miatoll

Device configuration for Xiaomi MIUI Camera (MIUI Camera v6.8 - Build 68001770.0) port for **Xiaomi Miatoll** (`curtana`, `gram`, `joyeuse`, `excalibur`).

> [!IMPORTANT]
> **Compatibility:** Specifically designed and built for **Android 16 and Android 17 (A16 / A17) ONLY**.

## Build Information
- **Version:** MIUI Camera v6.8
- **Build Version:** 68001770.0
- **Target OS:** Android 16 & Android 17 (A16 / A17 Only)
- **Camera Port & Builds:** [ℌ𝔞𝔪𝔦𝔡𝔬](https://github.com/Hamido)
- **Maintainer:** [Abdo Ahmed Elbanaa](https://github.com/AbdoAhmedElbanaa)

## Features
- Full MIUI Camera v6.8 with refreshed UI and advanced processing
- Parallel Processing enabled on Android 16 / 17 AOSP custom ROMs
- Bundled native 64-bit architecture libraries
- SELinux enforcing rules with zero denials
- Automatic symlinks for JNI and camera proprietary libraries
- Android 16 (SDK 36) & Android 17 dedicated support

## How to Build

1. Clone this repository into your ROM source tree:
```bash
git clone https://github.com/AbdoAhmedElbanaa/android_device_xiaomi_miuicamera_v6.8_miatoll device/xiaomi/miuicamera_v6.8_miatoll
```

2. Clone the corresponding vendor repository into:
```bash
vendor/xiaomi/miuicamera_v6.8_miatoll
```

3. Inherit this package in your device tree `device.mk`:
```makefile
$(call inherit-product, device/xiaomi/miuicamera_v6.8_miatoll/device.mk)
```

4. Include BoardConfig in your device tree `BoardConfig.mk`:
```makefile
include device/xiaomi/miuicamera_v6.8_miatoll/BoardConfig.mk
```
