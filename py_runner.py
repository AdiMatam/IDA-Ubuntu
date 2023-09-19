import subprocess as sub
import sys

class Spec:
    def __init__(self, compiledirs, linkdirs, links, raws=[]):
        self.compiledirs = compiledirs
        self.linkdirs = linkdirs
        self.links = links
        self.raws = raws

    def generate(self):
        self.compile_str = " ".join([f"-I{arg}" for arg in self.compiledirs])
        self.linkdir_str = " ".join([f"-L{arg}" for arg in self.linkdirs])
        self.link_str = " ".join([f"-l{arg}" for arg in self.links])
        self.raw_str = " ".join(self.raws)

        return (self.compile_str, self.linkdir_str + " " + self.link_str + " " + self.raw_str)

    def __add__(self, other):
        return Spec(
            compiledirs = self.compiledirs + other.compiledirs,
            linkdirs = self.linkdirs + other.linkdirs,
            links = self.links + other.links,
            raws = self.raws + other.raws
        );


linkmap = {
    "standard": Spec(
        compiledirs = ["sundials/include"],
        linkdirs = ["sundials/lib"],
        links = ["sundials_ida", "sundials_nvecserial", "sundials_nvecmanyvector", "m"],
    ),
}

linkmap.update({
    "superlu": linkmap["standard"] +
        Spec(
            compiledirs = ["superlu/SRC"],
            linkdirs = ["superlu/lib"],
            links = ["sundials_sunlinsolsuperlumt", "superlu_mt_PTHREAD"],
            raws = ["/usr/lib/x86_64-linux-gnu/libblas.so"]
    ),
    
    "klu": linkmap["standard"] + 
        Spec(
            compiledirs = ["suitesparse/include"],
            linkdirs = ["suitesparse/lib2"],
            links = ["sundials_sunlinsolklu", "klu", "amd", "colamd", "btf", "suitesparseconfig"],
    )
    
})

def main():
    if len(sys.argv) < 3:
        print("USAGE: python3 py_runner.py <program w/o extension> <type: klu, superlu, standard>")
        return

    # python3 sunrun.py sundials/examples/ida/serial/idaHeat2D_sps superlu
    sample = sys.argv[1]
    ptype = sys.argv[2]

    # simulate
    source = f"{sample}.c"
    obj = f"{sample}.o"
    exe = f"{sample}"

    spec = linkmap[ptype]
    comp, link = spec.generate()

    compile_call = f"gcc -c {source} -o {obj} {comp}"
    link_call = f"gcc {obj} -o {exe} {link}"

    print(compile_call)
    print()
    print(link_call)
    print()

    sub.call(compile_call, shell=True)
    sub.call(link_call, shell=True)

    if len(sys.argv) > 3:
        if sys.argv[3] == "run":
            sub.call(f"./{exe} {''.join(sys.argv[4:])}", shell=True)

main()

"""
"""
