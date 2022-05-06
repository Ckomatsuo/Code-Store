import os
import time
import shutil
from yamlUtils import YamlUtils
from ronghuaxueleng_pawdroid import get_content as pawdroid_content
from ronghuaxueleng_cfmem import get_content as cfmem_content

changfengoss = os.path.join("changfengoss")
dirname = time.strftime("%Y_%m_%d", time.localtime(time.time()))
yamlUtils = YamlUtils(changfengoss)
yamlUtils.clone_repo("https://github.com/changfengoss/pub.git")
yamlUtils.make_template_dict("yaml", dirname)
yamlUtils.save_file("sub/changfengoss.yaml")
shutil.rmtree(changfengoss)

# pawdroid_content()
# cfmem_content()

sub = os.path.join("sub")
yamlUtils = YamlUtils(sub)
#yamlUtils.make_template(["cfmem.yaml", "pawdroid.yaml"])
# yamlUtils.save_file("sub/combine.yaml")
