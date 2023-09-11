load(":cc_toolchain_config.bzl", "cc_toolchain_config")

package(default_visibility = ["//visibility:public"])

filegroup(name = "empty")

cc_toolchain_config(name = "aurix_gcc_linux_toolchain_config") 

cc_toolchain(
    name = "aurix_gcc_win_toolchain",
    toolchain_identifier = "aurix_gcc_win-toolchain",
    toolchain_config = ":aurix_gcc_linux_toolchain_config",
    all_files = ":empty",
    compiler_files = ":empty",
    dwp_files = ":empty",
    linker_files = ":empty",
    objcopy_files = ":empty",
    strip_files = ":empty",
    supports_param_files = 0,
)

cc_toolchain_suite(
    name = "aurix_gcc_suite",
    toolchains = {
        "k8": ":aurix_gcc_win_toolchain",
    },
)
