import os
import sys

import subprocess

def xj_print(*va_str):
    print('\033[2;31;43m ', *va_str, ' \033[0;0m')


def search_value(argv_list, argv_key):
    prev_value = ''
    for value in reversed(argv_list):
        if value == argv_key:
            return prev_value
        prev_value = value
    
    return ''

  # ['/home/xiaojianli/explore_gcc_bazel(1)/explore_gcc_bazel/toolchain/wrapper_compiler/mock_cc.py', '-MD', '-MF', 'bazel-out/k8-fastbuild/bin/_objs/CCU6_Isr_Timer/CCU6_Isr_Timer.d', '-frandom-seed=bazel-out/k8-fastbuild/bin/_objs/CCU6_Isr_Timer/CCU6_Isr_Timer.o', '-DBAZEL_CURRENT_REPOSITORY=""', '-iquote', '.', '-iquote', 'bazel-out/k8-fastbuild/bin', '--std=c++17', '-O3', '-w', '-fno-strict-aliasing', '-c', '-fmessage-length=0', '-fno-common', '-fdata-sections', '-ffunction-sections', '-mtc162', '-MMD', '-MP', '-ILibraries/iLLD/TC39B', '-ILibraries/iLLD/TC39B/Tricore', '-ILibraries/iLLD/TC39B/Tricore/_PinMap', '-ILibraries/iLLD/TC39B/Tricore/_Lib/InternalMux', '-ILibraries/iLLD/TC39B/Tricore/_Lib/DataHandling', '-ILibraries/iLLD/TC39B/Tricore/_Impl', '-ILibraries/iLLD/TC39B/Tricore/Stm/Timer', '-ILibraries/iLLD/TC39B/Tricore/Stm/Std', '-ILibraries/iLLD/TC39B/Tricore/Src/Std', '-ILibraries/iLLD/TC39B/Tricore/Spu/Std', '-ILibraries/iLLD/TC39B/Tricore/Smu/Std', '-ILibraries/iLLD/TC39B/Tricore/Smu/Smu', '-ILibraries/iLLD/TC39B/Tricore/Sent/Std', '-ILibraries/iLLD/TC39B/Tricore/Sent/Sent', '-ILibraries/iLLD/TC39B/Tricore/Sdmmc/Std', '-ILibraries/iLLD/TC39B/Tricore/Sdmmc/Sd', '-ILibraries/iLLD/TC39B/Tricore/Sdmmc/Emmc', '-ILibraries/iLLD/TC39B/Tricore/Scu/Std', '-ILibraries/iLLD/TC39B/Tricore/Rif/Std', '-ILibraries/iLLD/TC39B/Tricore/Rif/Rif', '-ILibraries/iLLD/TC39B/Tricore/Qspi/Std', '-ILibraries/iLLD/TC39B/Tricore/Qspi/SpiSlave', '-ILibraries/iLLD/TC39B/Tricore/Qspi/SpiMaster', '-ILibraries/iLLD/TC39B/Tricore/Psi5s/Std', '-ILibraries/iLLD/TC39B/Tricore/Psi5s/Psi5s', '-ILibraries/iLLD/TC39B/Tricore/Psi5/Std', '-ILibraries/iLLD/TC39B/Tricore/Psi5/Psi5', '-ILibraries/iLLD/TC39B/Tricore/Port/Std', '-ILibraries/iLLD/TC39B/Tricore/Port/Io', '-ILibraries/iLLD/TC39B/Tricore/Pms/Std', '-ILibraries/iLLD/TC39B/Tricore/Mtu/Std', '-ILibraries/iLLD/TC39B/Tricore/Msc/Std', '-ILibraries/iLLD/TC39B/Tricore/Msc/Msc', '-ILibraries/iLLD/TC39B/Tricore/Iom/Std', '-ILibraries/iLLD/TC39B/Tricore/Iom/Iom', '-ILibraries/iLLD/TC39B/Tricore/Iom/Driver', '-ILibraries/iLLD/TC39B/Tricore/I2c/Std', '-ILibraries/iLLD/TC39B/Tricore/I2c/I2c', '-ILibraries/iLLD/TC39B/Tricore/Hssl/Std', '-ILibraries/iLLD/TC39B/Tricore/Hssl/Hssl', '-ILibraries/iLLD/TC39B/Tricore/Hspdm/Std', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Trig', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Tom/Timer', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Tom/PwmHl', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Tom/Pwm', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Tom/Dtm_PwmHl', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Tim/Timer', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Tim/In', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Std', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Pwm', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Atom/Timer', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Atom/PwmHl', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Atom/Pwm', '-ILibraries/iLLD/TC39B/Tricore/Gtm/Atom/Dtm_PwmHl', '-ILibraries/iLLD/TC39B/Tricore/Gpt12/Std', '-ILibraries/iLLD/TC39B/Tricore/Gpt12/IncrEnc', '-ILibraries/iLLD/TC39B/Tricore/Geth/Std', '-ILibraries/iLLD/TC39B/Tricore/Geth/Eth', '-ILibraries/iLLD/TC39B/Tricore/Flash/Std', '-ILibraries/iLLD/TC39B/Tricore/Fce/Std', '-ILibraries/iLLD/TC39B/Tricore/Fce/Crc', '-ILibraries/iLLD/TC39B/Tricore/Evadc/Std', '-ILibraries/iLLD/TC39B/Tricore/Evadc/Adc', '-ILibraries/iLLD/TC39B/Tricore/Eray/Std', '-ILibraries/iLLD/TC39B/Tricore/Eray/Eray', '-ILibraries/iLLD/TC39B/Tricore/Emem/Std', '-ILibraries/iLLD/TC39B/Tricore/Edsadc/Std', '-ILibraries/iLLD/TC39B/Tricore/Edsadc/Edsadc', '-ILibraries/iLLD/TC39B/Tricore/Ebu/Std', '-ILibraries/iLLD/TC39B/Tricore/Ebu/Sram', '-ILibraries/iLLD/TC39B/Tricore/Ebu/Dram', '-ILibraries/iLLD/TC39B/Tricore/Ebu/BFlashSt', '-ILibraries/iLLD/TC39B/Tricore/Ebu/BFlashSpansion', '-ILibraries/iLLD/TC39B/Tricore/Dts/Std', '-ILibraries/iLLD/TC39B/Tricore/Dts/Dts', '-ILibraries/iLLD/TC39B/Tricore/Dma/Std', '-ILibraries/iLLD/TC39B/Tricore/Dma/Dma', '-ILibraries/iLLD/TC39B/Tricore/Cpu/Trap', '-ILibraries/iLLD/TC39B/Tricore/Cpu/Std', '-ILibraries/iLLD/TC39B/Tricore/Cpu/Irq', '-ILibraries/iLLD/TC39B/Tricore/Convctrl/Std', '-ILibraries/iLLD/TC39B/Tricore/Ccu6/TimerWithTrigger', '-ILibraries/iLLD/TC39B/Tricore/Ccu6/Timer', '-ILibraries/iLLD/TC39B/Tricore/Ccu6/TPwm', '-ILibraries/iLLD/TC39B/Tricore/Ccu6/Std', '-ILibraries/iLLD/TC39B/Tricore/Ccu6/PwmHl', '-ILibraries/iLLD/TC39B/Tricore/Ccu6/PwmBc', '-ILibraries/iLLD/TC39B/Tricore/Ccu6/Icu', '-ILibraries/iLLD/TC39B/Tricore/Can/Std', '-ILibraries/iLLD/TC39B/Tricore/Can/Can', '-ILibraries/iLLD/TC39B/Tricore/Asclin/Std', '-ILibraries/iLLD/TC39B/Tricore/Asclin/Spi', '-ILibraries/iLLD/TC39B/Tricore/Asclin/Lin', '-ILibraries/iLLD/TC39B/Tricore/Asclin/Asc', '-ILibraries/Service/CpuGeneric/SysSe/Time', '-ILibraries/Service/CpuGeneric/SysSe/Math', '-ILibraries/Service/CpuGeneric/SysSe/General', '-ILibraries/Service/CpuGeneric/SysSe/Comm', '-ILibraries/Service/CpuGeneric/SysSe/Bsp', '-ILibraries/Service/CpuGeneric/StdIf', '-ILibraries/Service/CpuGeneric/If', '-ILibraries/Service/CpuGeneric', '-ILibraries/Infra/Ssw/TC39B/Tricore', '-ILibraries/Infra/Platform/Tricore', '-ILibraries/Infra/Platform', '-ILibraries/Infra/Platform/Tricore/Compilers', '-ILibraries/Infra/Sfr/TC39B/_Reg', '-ILibraries/Infra/Ssw/TC39B/Tricore', '-IConfigurations', '-c', 'CCU6_Isr_Timer.c', '-o', 'bazel-out/k8-fastbuild/bin/_objs/CCU6_Isr_Timer/CCU6_Isr_Timer.o\r'

TRICORE_TOOLCHAIN_DIR = '/home/xiaojianli/tricore_940_linux/bin/tricore-elf-'
WORKSPACE = os.path.join(os.path.dirname(__file__), '..', '..')

def bash_file_call(argv):
    with open('tmp_run.sh', 'w') as tmp_batch_file:
        tmp_batch_file.write('\n'.join(argv))

    subprocess.run(['tmp_run.sh'], check=True)
    os.remove('tmp_run.sh')

def main():
    #backup_cwd = os.getcwd()
    #os.chdir(WORKSPACE)
    #xj_print('cd ', os.getcwd())

    source_file = search_value(sys.argv, '-c')
    assert source_file != ''
    extension = os.path.splitext(source_file)[-1]
    compiler_name = 'g++'
    if extension == '.c':
        compiler_name = 'gcc'
    run_argv = [TRICORE_TOOLCHAIN_DIR + compiler_name]
    run_argv.extend(sys.argv[1:])

    xj_print(' '.join(run_argv))
    bash_file_call(run_argv)

    #xj_print('cd ', backup_cwd)
    #os.chdir(backup_cwd)

if __name__ == '__main__':
    main()
