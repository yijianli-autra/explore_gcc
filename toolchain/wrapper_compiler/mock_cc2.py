import os
import sys

import subprocess

TASKING_DIR = 'C:/Infineon/AURIX-Studio-1.9.8/tools/Compilers/Tasking_1.1r8/ctc/bin/'
TASKING_CC = TASKING_DIR + 'cctc'
TASKING_AS = TASKING_DIR + 'astc'
WORKSPACE = os.path.join(os.path.dirname(__file__), '..', '..')

HACK_ENV = {
    'COPYRIGHT':'COPYRIGHT',
    'TASKING_RUN_STAMP':'c79d0ef5',
}

MISC_ARGV = '-cs --misrac-version=2004 --iso=99 --c++14 --language=+volatile --exceptions --anachronisms --fp-model=3 -O3 --tradeoff=4 --compact-max-size=200 -g -Wc-w544 -Wc-w557 -Ctc39xb -Y0 -N0 -Z0'.split(' ')

TO_OBJECT_ARGV = '-Og -Os --no-warnings= --error-limit=42'.split(' ')

def xj_print(*va_str):
    print('\033[2;31;43m ', *va_str, ' \033[0;0m')

def replace_extension(path, new_extension):
    value = list(os.path.splitext(path))
    if len(value) > 1:
        value[-1] = new_extension
    return ''.join(value)

def search_value(argv_list, argv_key):
    return_next = False
    for value in argv_list:
        if return_next:
            return value
        if value == argv_key:
            return_next = True
    
    return ''

class TaskingSourcesCompileInfo:

    def __init__(self):
        self.dep_file = ''
        self.output_file = ''
        self.sources_file = ''
        self.src_tmp_file = ''
        self.std = 'c++14'
        self.copts = []

    def to_exec_argv(self):
        return [self.to_src_file_argv(), self.to_object_argv()]

    def to_src_file_argv(self):
# Output format:cctc -cs --dep-file="Libraries/iLLD/TC39B/Tricore/_PinMap/IfxDmu_PinMap.d" --misrac-version=2004 -D__CPU__=tc39xb "-fC:/Users/autratech/AURIX-v1.9.8-workspace/MTU_MBIST_1_KIT_TC397_TFT/Release/TASKING_C_C___Compiler-Include_paths.opt" --iso=99 --c++14 --language=+volatile --exceptions --anachronisms --fp-model=3 -O0 --tradeoff=4 --compact-max-size=200 -g -Wc-w544 -Wc-w557 -Ctc39xb -Y0 -N0 -Z0 -o "Libraries/iLLD/TC39B/Tricore/_PinMap/IfxDmu_PinMap.src" "../Libraries/iLLD/TC39B/Tricore/_PinMap/IfxDmu_PinMap.c"
        result_argv = [TASKING_CC]
        result_argv.extend(MISC_ARGV)
        result_argv.append('--dep-file={}'.format(self.dep_file))
        result_argv.append('-o {}'.format(self.src_tmp_file))
        result_argv.append(self.sources_file)
        return result_argv

    def to_object_argv(self):
# astc -Og -Os --no-warnings= --error-limit=42 -o  "Libraries/iLLD/TC39B/Tricore/_PinMap/IfxDmu_PinMap.o" "Libraries/iLLD/TC39B/Tricore/_PinMap/IfxDmu_PinMap.src"
        result_argv = [TASKING_AS]
        result_argv.extend(TO_OBJECT_ARGV)
        result_argv.append('-o {}'.format(self.output_file))
        result_argv.append(self.src_tmp_file)
        return result_argv

def make_tasking_sources_compile_info(gcc_pattern_argv):
#Input is: -MD -MF bazel-out/x64_windows-fastbuild/bin/_objs/test/test.d -iquote . -iquote bazel-out/x64_windows-fastbuild/bin -cs -c test.c -o bazel-out/x64_windows-fastbuild/bin/_objs/test/test.o  
    info = TaskingSourcesCompileInfo()
    info.sources_file = search_value(gcc_pattern_argv, '-c')
    info.dep_file = search_value(gcc_pattern_argv, '-MF')
    info.output_file = search_value(gcc_pattern_argv, '-o')
    info.src_tmp_file = replace_extension(info.dep_file, '.src')

    info.sources_file = info.sources_file.replace('/', '\\')
    info.dep_file = info.dep_file.replace('/', '\\')
    info.output_file = info.output_file.replace('/', '\\')
    info.src_tmp_file = info.src_tmp_file.replace('/', '\\')
    return info

def main():
    backup_cwd = os.getcwd()
    xj_print('cd ', WORKSPACE)
    os.chdir(WORKSPACE)
    compile_info = make_tasking_sources_compile_info(sys.argv[1:])
    batch_cmd = []
    for argv in compile_info.to_exec_argv():
        xj_print('xj@debug forward args:', ' '.join(argv))    
        #subprocess.run(argv, env=HACK_ENV, check=True, shell=True)
        batch_cmd.append(' '.join(argv))
    
    with open('tmp_run.bat', 'w') as tmp_batch_file:
        tmp_batch_file.write('\n'.join(batch_cmd))

    subprocess.run(['tmp_run.bat'], env=HACK_ENV, check=True)
    xj_print('cd ', backup_cwd)
    os.chdir(backup_cwd)
    
if __name__ == '__main__':
    main()
