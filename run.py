from subprocess import run
import shutil
import yaml

data = {}

width, height = shutil.get_terminal_size((80, 20))
length = width - 8
count = 25

print("\033[2J\033[1;1H", end="")
print("\033[1;33mRunning \033[1;3;4;35mAdvent Of Code\033[0;1;3;35m...\033[0m")

for i in range(1, count + 1):
    result = {}
    for m in "a", "b":
        file = __file__[:-6] + f"{i}/{i}{m}.py"
        try:
            res = run(["python3", file], capture_output=True).stdout.strip().decode("ascii")
            res = int(res)
        except ValueError:
            pass
        if res:
            result[m] = res
    if result != {}:
        data[i] = result

    c = i * length // count
    print(f"\033[1;32m[{'=' * c}>{' ' * (length - c)}] {('  ' + str(i * 100 // count))[-3:]}%", end="\r")
print()


def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, str_presenter)

with open(__file__[:-6] + "results.yaml", "w") as f:
    yaml.dump(dict(results=data), f, default_flow_style=False)
