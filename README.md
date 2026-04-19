# Maskpy²

Maskpy² is a python obfuscator combining source-level transformations, encrypted bytecode, and nested virtual machines with a custom ISA.

## Features

**Nested polymorphic virtual machines:**
Functions can be lifted to a custom ISA executed by a generated interpreter. A configurable number of VMs (3–5 by default, tunable via `-v`) are stacked per function, and the IR is split across them so no single interpreter sees the whole function. Each VM is independently randomized:

- Architecture: pure stack, register-based (8 regs), or hybrid.
- Shuffled opcode table (opcode bytes differ per VM).
- Per-VM compound/fused opcodes (e.g. `LOAD_ADD`, `PUSH_STORE`, `LOAD2`).
- Random `NOP` padding in the bytecode stream.

**Withheld opcodes & self-modifying dispatch:**
Some opcode handlers are left out of the static interpreter and patched into the dispatch table at runtime. The VM can't run the program until it has finished patching itself, which breaks naive static lifting and makes the dispatch table hard to fingerprint.

**Cross-VM data flow:**
Nested VMs talk to each other through shared stacks, global registers, and explicit `VM_YIELD` instructions. Control and data flow only make sense if you reason about all the VMs at once.

**Layered VM crypto:**
xoshiro256** drives the keystream, XTEA encrypts bytecode segments, and SipHash handles key derivation and integrity tags. Each VM has its own derived key.

**Polymorphic bytecode encryption (JIT-decrypted):**
Functions that aren't lifted to the VM are compiled to CPython bytecode, stripped of metadata (`co_filename`, `co_name`, `co_qualname`), and padded with dead instructions (`NOP`, `LOAD_CONST`/`POP_TOP` pairs). The result is then encrypted using one of three randomly chosen compositions of a PCG64 XOR stream and a PCG-driven byte permutation. The cleartext code object only exists briefly at call time, rebuilt by a trampoline.

**Mixed boolean-arithmetic (MBA) & opaque predicates:**
Arithmetic and boolean expressions are rewritten into equivalent but messier MBA forms over several passes. Dead branches guarded by opaque predicates (number-theoretic identities, bit-level invariants) are inserted to confuse control-flow analysis.

**Constant unfolding:**
Numeric and boolean constants are expanded into expression trees that evaluate to the original value, so the constant isn't visible anymore.

**String & bytes encryption:**
String and bytes literals are XOR-encrypted at compile time with a per-literal random key and decrypted on demand by a small runtime helper (`_sd`). f-strings are left alone to avoid breaking formatted expressions.

**Anti-debug guards:**
Each obfuscated function starts with `sys.gettrace()` / `sys.getprofile()` checks. If a tracer or profiler is attached, the function silently returns `None`.

**Comment, docstring & identifier stripping:**
Comments and docstrings are dropped, and every global and local identifier is renamed to an opaque token (`X1`, `X2`, …) scoped per function.

## Installation & Usage

```sh
git clone git@github.com:NeKroFR/Maskpy2.git
cd Maskpy2/
python Maskpy2.py <input.py> [-o output.py] [-f func1 func2 ...] [-v N]
```

- `-o, --output`: output file (default: `<input>_obfuscated.py`)
- `-f, --functions`: functions to obfuscate (default: all top-level functions)
- `-v, --vm-count`: VMs per function (default: random 3–5)

You can find some samples under `tests/` and `ctf/` (flag format: `flag{...}`).
