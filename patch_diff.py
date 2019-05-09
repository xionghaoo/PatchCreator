import os
import diff_match_patch as dmp_module
import codecs


def create_pat_file(f1, f2):
    f1_text = read_file(f1)
    f2_text = read_file(f2)

    dmp = dmp_module.diff_match_patch()
    diff = dmp.diff_main(f1_text, f2_text)
    # Result: [(-1, "Hell"), (1, "G"), (0, "o"), (1, "odbye"), (0, " World.")]
    dmp.diff_cleanupSemantic(diff)
    # Result: [(-1, "Hello"), (1, "Goodbye"), (0, " World.")]
    patches = dmp.patch_toText(dmp.patch_make(diff))
    print(patches)
    f = open('patch.pat', 'w')
    f.write(patches)
    f.close()


def read_file(f):
    fin = codecs.open(f, 'r', encoding='utf-8')
    f_text = ''
    for line in fin:
        f_text += line
    return f_text


create_pat_file('f1', 'f2')
