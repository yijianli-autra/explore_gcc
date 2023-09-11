load("@bazel_tools//tools/build_defs/cc:action_names.bzl", "ACTION_NAMES")
load(
    "@bazel_tools//tools/cpp:cc_toolchain_config_lib.bzl",
    "feature",
    "flag_group",
    "flag_set",
    "tool_path",
)

all_link_actions = [
    ACTION_NAMES.cpp_link_executable,
    ACTION_NAMES.cpp_link_dynamic_library,
    ACTION_NAMES.cpp_link_nodeps_dynamic_library,
]

TRICORE_TOOLCHAIN_DIR = '/home/xiaojianli/tricore_940_linux/bin/'

def _impl(ctx):
    tool_paths = [
        tool_path(
            name = "gcc",
            path = '/home/xiaojianli/explore_gcc_bazel(1)/explore_gcc_bazel/toolchain/wrapper_compiler/mock_cc.sh'
        ),
        # tool_path(
        #     name = "g++",
        #     path = TRICORE_TOOLCHAIN_DIR + 'tricore-elf-g++'
        # ),
        tool_path(
            name = "ld",
            path = TRICORE_TOOLCHAIN_DIR + 'tricore-elf-ld'
        ),
        tool_path(
            name = "ar",
            path = TRICORE_TOOLCHAIN_DIR + 'tricore-elf-ar'
        ),
        tool_path(
            name = "cpp",
            path = TRICORE_TOOLCHAIN_DIR + 'tricore-elf-cpp'
        ),
        tool_path(
            name = "gcov",
            path = TRICORE_TOOLCHAIN_DIR + 'tricore-elf-gcov'
        ),
        tool_path(
            name = "nm",
            path = TRICORE_TOOLCHAIN_DIR + 'tricore-elf-nm'
        ),
        tool_path(
            name = "objdump",
            path = TRICORE_TOOLCHAIN_DIR + 'tricore-elf-objdump'
        ),
        tool_path(
            name = "strip",
            path = TRICORE_TOOLCHAIN_DIR + 'tricore-elf-strip'
        ),
    ]

    features = [ # NEW
        feature(
            name = "default_linker_flags",
            enabled = True,
            flag_sets = [
                flag_set(
                    actions = all_link_actions,
                    flag_groups = ([
                        flag_group(
                            flags = [
                                "-nocrt0",
                            ],
                        ),
                    ]),
                ),
            ],
        ),
    ]

    return cc_common.create_cc_toolchain_config_info(
        ctx = ctx,
        features = features, # NEW
        cxx_builtin_include_directories = [
        ],
        toolchain_identifier = "aurix_gcc_win-toolchain",
        host_system_name = "local",
        target_system_name = "local",
        target_cpu = "tasking_x64_windows",
        target_libc = "unknown",
        compiler = "tasking",
        abi_version = "unknown",
        abi_libc_version = "unknown",
        tool_paths = tool_paths,
    )

cc_toolchain_config = rule(
    implementation = _impl,
    attrs = {},
    provides = [CcToolchainConfigInfo],
)
