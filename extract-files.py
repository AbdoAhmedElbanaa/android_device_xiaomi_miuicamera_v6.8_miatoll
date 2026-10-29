#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024-2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/miuicamera_v6.8_miatoll',
    'vendor/xiaomi/miatoll',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    ('system/lib64/libcamera_algoup_jni.xiaomi.so', 'system/lib64/libcamera_mianode_jni.xiaomi.so'): blob_fixup()
        .add_needed('libgui_shim_miuicamera.so'),
    'system/lib64/libcamera_jpegutil_jni.xiaomi.so': blob_fixup()
        .remove_needed('libhidltransport.so'),
    'system/lib64/libcamera_960_mpbase.so': blob_fixup()
        .fix_soname(),
}  # fmt: skip

module = ExtractUtilsModule(
    'miuicamera_v6.8_miatoll',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
