import subprocess
import os

curr_dir = os.path.dirname(os.path.realpath(__file__))
base_cd_cmd = f"cd {curr_dir}"

subprocess.Popen(f"cd {curr_dir}", shell=True).wait()


def call_process(cmds: list):
    command = " && ".join([base_cd_cmd] + cmds)

    print(command)
    p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("stdout", p.stdout.decode("utf"))
    print("stderr", p.stderr.decode("utf"))


call_process(["cd i18n_zhcn_conversion", "python main.py"])
