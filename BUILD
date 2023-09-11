load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library")

DEFAULT_COPTS = [
        "-ILibraries/iLLD/TC39B",
        "-ILibraries/iLLD/TC39B/Tricore",
        "-ILibraries/iLLD/TC39B/Tricore/_PinMap",
        "-ILibraries/iLLD/TC39B/Tricore/_Lib/InternalMux",
        "-ILibraries/iLLD/TC39B/Tricore/_Lib/DataHandling",
        "-ILibraries/iLLD/TC39B/Tricore/_Impl",
        "-ILibraries/iLLD/TC39B/Tricore/Stm/Timer",
        "-ILibraries/iLLD/TC39B/Tricore/Stm/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Src/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Spu/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Smu/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Smu/Smu",
        "-ILibraries/iLLD/TC39B/Tricore/Sent/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Sent/Sent",
        "-ILibraries/iLLD/TC39B/Tricore/Sdmmc/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Sdmmc/Sd",
        "-ILibraries/iLLD/TC39B/Tricore/Sdmmc/Emmc",
        "-ILibraries/iLLD/TC39B/Tricore/Scu/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Rif/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Rif/Rif",
        "-ILibraries/iLLD/TC39B/Tricore/Qspi/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Qspi/SpiSlave",
        "-ILibraries/iLLD/TC39B/Tricore/Qspi/SpiMaster",
        "-ILibraries/iLLD/TC39B/Tricore/Psi5s/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Psi5s/Psi5s",
        "-ILibraries/iLLD/TC39B/Tricore/Psi5/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Psi5/Psi5",
        "-ILibraries/iLLD/TC39B/Tricore/Port/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Port/Io",
        "-ILibraries/iLLD/TC39B/Tricore/Pms/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Mtu/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Msc/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Msc/Msc",
        "-ILibraries/iLLD/TC39B/Tricore/Iom/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Iom/Iom",
        "-ILibraries/iLLD/TC39B/Tricore/Iom/Driver",
        "-ILibraries/iLLD/TC39B/Tricore/I2c/Std",
        "-ILibraries/iLLD/TC39B/Tricore/I2c/I2c",
        "-ILibraries/iLLD/TC39B/Tricore/Hssl/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Hssl/Hssl",
        "-ILibraries/iLLD/TC39B/Tricore/Hspdm/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Trig",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Tom/Timer",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Tom/PwmHl",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Tom/Pwm",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Tom/Dtm_PwmHl",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Tim/Timer",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Tim/In",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Pwm",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Atom/Timer",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Atom/PwmHl",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Atom/Pwm",
        "-ILibraries/iLLD/TC39B/Tricore/Gtm/Atom/Dtm_PwmHl",
        "-ILibraries/iLLD/TC39B/Tricore/Gpt12/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Gpt12/IncrEnc",
        "-ILibraries/iLLD/TC39B/Tricore/Geth/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Geth/Eth",
        "-ILibraries/iLLD/TC39B/Tricore/Flash/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Fce/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Fce/Crc",
        "-ILibraries/iLLD/TC39B/Tricore/Evadc/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Evadc/Adc",
        "-ILibraries/iLLD/TC39B/Tricore/Eray/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Eray/Eray",
        "-ILibraries/iLLD/TC39B/Tricore/Emem/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Edsadc/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Edsadc/Edsadc",
        "-ILibraries/iLLD/TC39B/Tricore/Ebu/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Ebu/Sram",
        "-ILibraries/iLLD/TC39B/Tricore/Ebu/Dram",
        "-ILibraries/iLLD/TC39B/Tricore/Ebu/BFlashSt",
        "-ILibraries/iLLD/TC39B/Tricore/Ebu/BFlashSpansion",
        "-ILibraries/iLLD/TC39B/Tricore/Dts/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Dts/Dts",
        "-ILibraries/iLLD/TC39B/Tricore/Dma/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Dma/Dma",
        "-ILibraries/iLLD/TC39B/Tricore/Cpu/Trap",
        "-ILibraries/iLLD/TC39B/Tricore/Cpu/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Cpu/Irq",
        "-ILibraries/iLLD/TC39B/Tricore/Convctrl/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Ccu6/TimerWithTrigger",
        "-ILibraries/iLLD/TC39B/Tricore/Ccu6/Timer",
        "-ILibraries/iLLD/TC39B/Tricore/Ccu6/TPwm",
        "-ILibraries/iLLD/TC39B/Tricore/Ccu6/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Ccu6/PwmHl",
        "-ILibraries/iLLD/TC39B/Tricore/Ccu6/PwmBc",
        "-ILibraries/iLLD/TC39B/Tricore/Ccu6/Icu",
        "-ILibraries/iLLD/TC39B/Tricore/Can/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Can/Can",
        "-ILibraries/iLLD/TC39B/Tricore/Asclin/Std",
        "-ILibraries/iLLD/TC39B/Tricore/Asclin/Spi",
        "-ILibraries/iLLD/TC39B/Tricore/Asclin/Lin",
        "-ILibraries/iLLD/TC39B/Tricore/Asclin/Asc",
        "-ILibraries/Service/CpuGeneric/SysSe/Time",
        "-ILibraries/Service/CpuGeneric/SysSe/Math",
        "-ILibraries/Service/CpuGeneric/SysSe/General",
        "-ILibraries/Service/CpuGeneric/SysSe/Comm",
        "-ILibraries/Service/CpuGeneric/SysSe/Bsp",
        "-ILibraries/Service/CpuGeneric/StdIf",
        "-ILibraries/Service/CpuGeneric/If",
        "-ILibraries/Service/CpuGeneric",
        "-ILibraries/Infra/Ssw/TC39B/Tricore",
        "-ILibraries/Infra/Platform/Tricore",
        "-ILibraries/Infra/Platform",
        "-ILibraries/Infra/Platform/Tricore/Compilers",
        "-ILibraries/Infra/Sfr/TC39B/_Reg",
        "-ILibraries/Infra/Ssw/TC39B/Tricore",
        "-IConfigurations",
    ]


cc_library(
    name = "CCU6_Isr_Timer",
    srcs = ["CCU6_Isr_Timer.c"],
    hdrs = ["CCU6_Isr_Timer.h"],
    copts = DEFAULT_COPTS,
    deps = [
        ":all_libs",
    ],
    alwayslink = True,
)

cc_library(
    name = "CCU6_Interrupt_CC",
    srcs = ["CCU6_Interrupt_CC.cc"],
    hdrs = ["CCU6_Interrupt_CC.h"],
    copts = DEFAULT_COPTS,
    deps = [
        ":CCU6_Isr_Timer",
    ],
    alwayslink = True,
)

cc_library(
    name = "CCU6_Interrupt",
    srcs = ["CCU6_Interrupt.c"],
    hdrs = ["CCU6_Interrupt.h"],
    copts = DEFAULT_COPTS,
    deps = [
        ":all_libs",
    ],
    alwayslink = True,
)


cc_library(
    name = "Cpu0_Main",
    srcs = ["Cpu0_Main.c"],
    deps = [
        ":CCU6_Interrupt_CC",
    ],
    copts = DEFAULT_COPTS,
    alwayslink = True,
)

cc_library(
    name = "Cpu1_Main",
    srcs = ["Cpu1_Main.c"],
    deps = [
        ":CCU6_Interrupt_CC",
    ],
    copts = DEFAULT_COPTS,
    alwayslink = True,
)

cc_library(
    name = "Cpu2_Main",
    srcs = ["Cpu2_Main.c"],
    deps = [
        ":CCU6_Interrupt_CC",
    ],
    copts = DEFAULT_COPTS,
    alwayslink = True,
)

cc_library(
    name = "Cpu3_Main",
    srcs = ["Cpu3_Main.c"],
    deps = [
        ":CCU6_Interrupt_CC",
    ],
    copts = DEFAULT_COPTS,
    alwayslink = True,
)

cc_library(
    name = "Cpu4_Main",
    srcs = ["Cpu4_Main.c"],
    deps = [
        ":CCU6_Interrupt_CC",
    ],
    copts = DEFAULT_COPTS,
    alwayslink = True,
)

cc_library(
    name = "Cpu5_Main",
    srcs = ["Cpu5_Main.c"],
    deps = [
        ":CCU6_Interrupt_CC",
    ],
    copts = DEFAULT_COPTS,
    alwayslink = True,
)

cc_binary(
    name = "cpp_hello",
    deps = [
        ":Cpu0_Main",
        ":Cpu1_Main",
        ":Cpu2_Main",
        ":Cpu3_Main",
        ":Cpu4_Main",
        ":Cpu5_Main",
    ],
    data = [
        "Lcf_Gnuc_Tricore_Tc.lsl",
    ],
    linkopts = [
        "--std=c++17",
        "-nocrt0",
        "-mtc162",
        "-T\"//home/xiaojianli/explore_gcc_bazel(1)/explore_gcc_bazel/Lcf_Gnuc_Tricore_Tc.lsl\"",
        # "-Wl,--gc-sections",
    ]
)

cc_library(
    name = "all_libs",
    srcs = [
        "//Configurations:config_srcs",
        "//Libraries:lib_srcs",
    ],
    hdrs = [
        "//Configurations:config_headers",
        "//Libraries:lib_headers",
    ],
    copts = DEFAULT_COPTS,
    alwayslink = True,
)
