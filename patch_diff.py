import os
import diff_match_patch as dmp_module
import codecs

# 原版本文件
OLD_FILE = 'index.android.bundle'

# 新版本文件
NEW_FILE = 'index.android.bundle_2'

# 补丁文件
PATCH_FILE = '_patch'


def create_pat_file(f1, f2):
    print('--------patch start--------')
    f1_text = read_file(f1)
    f2_text = read_file(f2)

    dmp = dmp_module.diff_match_patch()
    diff = dmp.diff_main(f1_text, f2_text)
    patches = dmp.patch_toText(dmp.patch_make(diff))
    write_file(PATCH_FILE, patches)
    print(PATCH_FILE + ' file created')
    print('--------patch end--------')


def read_file(f):
    fin = codecs.open(f, 'r', encoding='utf-8')
    f_text = ''
    for line in fin:
        f_text += line
    return f_text


def write_file(f_name, content):
    f = open(f_name, 'w')
    f.write(content)
    f.close()


def verify_patch(f_patch, f1):
    print('--------verify start--------')
    patches_text = read_file(f_patch)
    f1_text = read_file(f1)
    dmp = dmp_module.diff_match_patch()
    patches = dmp.patch_fromText(patches_text)
    result = dmp.patch_apply(patches, f1_text)
    if result[1][0]:
        write_file('patched_' + f1, result[0])
        print('patch verify success')
    else:
        print('patch verify failure')
    print('--------verify end--------')


create_pat_file(OLD_FILE, NEW_FILE)

verify_patch(PATCH_FILE, OLD_FILE)


