# Binary Ninja Plugins

| PluginName | Author | License | Type | Description |
|------------|--------|---------|----------|-------------|
|[Syscaller](https://github.com/carstein/Syscaller)|[Michal Melewski <michal.melewski@gmail.com>](https://github.com/carstein)|[MIT](Syscaller/LICENSE)|binaryview|A plugins that print out details about encountered syscalls.|
|[Bookmarks](https://github.com/joshwatson/binaryninja-bookmarks)|[Josh Watson](https://github.com/joshwatson)|[MIT](binaryninja-bookmarks/LICENSE)|core, ui|A plugin that adds bookmarking functionality.|
|[Microcorruption BinaryView Plugin](https://github.com/joshwatson/binaryninja-microcorruption)|[Josh Watson](https://github.com/joshwatson)|[MIT](binaryninja-microcorruption/LICENSE)|binaryview, core, ui|A `BinaryView` for Microcorruption CTF memory dumps|
|[RetDec Offline Decompiler](https://github.com/ThisIsSecurity/retdec_offline)|[Stormshield](https://github.com/ThisIsSecurity)|[MIT](retdec_offline/LICENSE)|architecture, binaryview, core, ui|The plugin recovers C code from machine code.|
|[LLVM Deobfuscator](https://github.com/RPISEC/llvm-deobfuscator)|[Toshi Piazza & Kareem El-Faramawi](https://github.com/RPISEC)|[MIT](llvm-deobfuscator/LICENSE)|core, ui|Deobfuscator for LLVM-Obfuscator|
|[Xref Call Finder](https://github.com/rick2600/xref_call_finder)|[rick2600](https://github.com/rick2600)|[MIT](xref_call_finder/LICENSE)|architecture, binaryview, core, ui|Print call chains to a target function|
|[Djumpo Unchained](https://github.com/ThisIsSecurity/djumpo_unchained)|[Stormshield](https://github.com/ThisIsSecurity)|[MIT](djumpo_unchained/LICENSE)|architecture, binaryview, core, ui|The plugin de-obfuscates chained jumps.|
|[function_abi](https://github.com/whitequark/binja_function_abi)|[whitequark](https://github.com/whitequark)|[BSD-0-clause](binja_function_abi/LICENSE)|ui|A plugin that adds a GUI for changing function ABI.|
|[CLIPPER Architecture Plugin](https://github.com/pmackinlay/binaryninja-clipper)|[Patrick Mackinlay](https://github.com/pmackinlay)|[MIT](binaryninja-clipper/LICENSE)|architecture|A disassembler and lifter for the CLIPPER architecture.|
|[bnpy](https://github.com/extremecoders-re/bnpy)|[extremecoders](https://github.com/extremecoders-re)|[MIT](bnpy/LICENSE)|architecture|Python 2.7 architecture plugin.|
|[AVR Architecture Plugin](https://github.com/fluxchief/binaryninja_avr)|[Kevin Hamacher](https://github.com/fluxchief)|[MIT](binaryninja_avr/LICENSE)|architecture, binaryview|AVR architecture plugin + lifter.|
|[ripr](https://github.com/pbiernat/ripr)|[Patrick Biernat](https://github.com/pbiernat)|[MIT](ripr/LICENSE)|none|Package binary code as a Python class backed by Unicorn-Engine|
|[Mach-O Symbols Generator](https://github.com/bambu/binaryninja-machosymbols)|[Bambu](https://github.com/bambu)|[MIT](binaryninja-machosymbols/LICENSE)|ui|Creates symbols and renames functions in mach-o binaries|
|[x64dbgbinja](https://github.com/x64dbg/x64dbgbinja)|[x64dbg](https://github.com/x64dbg)|[MIT](x64dbgbinja/LICENSE)|binaryview|Official x64dbg plugin for Binary Ninja.|
|[WinAPI-Annotator](https://github.com/levyjm/WinAPI-Annotator)|[John Levy with help from @carstein](https://github.com/levyjm)|[MIT](WinAPI-Annotator/LICENSE)|binaryview|A plugins that annotates Windows API function arguments.|
|[Nampa](https://github.com/kenoph/nampa)|[Paolo Montesel (github.com/kenoph)](https://github.com/kenoph)|[LGPL v3](nampa/LICENSE)|binaryview, core|FLIRT for (binary) ninjas|
|[VMNDH-2k12 Architecture Plugin](https://github.com/verylazyguy/binaryninja-vmndh)|[verylazyguy](https://github.com/verylazyguy)|[MIT](binaryninja-vmndh/LICENSE)|architecture|A disassembler and lifter for the VMNDH-2k12 architecture.|
|[Annotator](https://github.com/carstein/Annotator)|[Michal Melewski <michal.melewski@gmail.com>](https://github.com/carstein)|[MIT](Annotator/LICENSE)|binaryview|A plugins that annotates libc function arguments.|
|[Pasticciotto Architecture Plugin](https://github.com/peperunas/binaryninja-pasticciotto)|[Giulio De Pasquale](https://github.com/peperunas)|[MIT](binaryninja-pasticciotto/LICENSE)|architecture|A disassembler for the Pasticciotto architecture.|
|[easypatch](https://github.com/walterschell/easypatch)|[Walter Schell](https://github.com/walterschell)|[MIT](easypatch/LICENSE)|ui|Right click to patch contents of memory operands|
|[MSP430 Architecture Plugin](https://github.com/joshwatson/binaryninja-msp430)|[Josh Watson](https://github.com/joshwatson)|[MIT](binaryninja-msp430/LICENSE)|architecture|A disassembler and lifter for the MSP430 architecture.|
|[Binjatron](https://github.com/snare/binjatron)|[snare](https://github.com/snare)|[MIT](binjatron/LICENSE)|ui|Synchronise the Binary Ninja binary view with a debugger via Voltron.|
|[BNHook](https://github.com/orndorffgrant/bnhook)|[Grant Orndorff](https://github.com/orndorffgrant)|[MIT](bnhook/LICENSE)|core, ui|Insert custom hooks|
|[Explain Instruction](https://github.com/ehennenfent/binja_explain_instruction)|[Eric Hennenfent](https://github.com/ehennenfent)|[Apache 2](binja_explain_instruction/LICENSE)|education, ui|Displays a window that explains in simple English what an assembly instruction does|
|[Keyhole](https://github.com/carstein/Keyhole)|[Michal Melewski <michal.melewski@gmail.com>](https://github.com/carstein)|[MIT](Keyhole/LICENSE)|ui|Report about functions in given binary.|
|[Radare2 Linear Sweep Plugin](https://github.com/Manouchehri/binaryninja-radare2)|[David Manouchehri](https://github.com/Manouchehri)|[BSD4](binaryninja-radare2/LICENSE)|binaryview, core, ui|Uses radare to identify extra symbols|
|[Simple Linear Sweep](https://github.com/lstotch/linsweep)|[butters](https://github.com/lstotch)|[MIT](linsweep/LICENSE)|architecture, binaryview, core, ui|Uses simplistic techniques to identify additional functions for x86 and x86_64 binaries.|
|[Search Immediate](https://github.com/6e726d/binaryninja-search)|[6e726d](https://github.com/6e726d)|[MIT](binaryninja-search/LICENSE)|ui|Search for the specific value in the instruction operands.|
|[Trickle-down Variables](https://github.com/toolCHAINZ/trickledown_vars)|[toolCHAINZ](https://github.com/toolCHAINZ)|[MIT](trickledown_vars/LICENSE)|ui|(ALPHA) Autorename variables that are copies of other variables.|
|[binjago](https://github.com/zznop/binjago)|[zznop](https://github.com/zznop)|[MIT](binjago/LICENSE)|binaryview|Binjago static analysis plugin suite.|
|[bnil-graph](https://github.com/withzombies/bnil-graph)|[Ryan Stortz (@withzombies)](https://github.com/withzombies)|[Apache 2.0](bnil-graph/LICENSE)|ui|A BinaryNinja plugin to graph a BNIL instruction tree|
|[Itanium C++ ABI](https://github.com/whitequark/binja_itanium_cxx_abi)|[whitequark](https://github.com/whitequark)|[BSD-0-clause](binja_itanium_cxx_abi/LICENSE)|analysis|A plugin providing an analysis for Itanium C++ ABI.|
|[BINoculars](https://github.com/rick2600/binoculars)|[rick2600](https://github.com/rick2600)|[MIT](binoculars/LICENSE)|ui|Plugin for Binary Ninja to centralize features useful in static analysis.|
|[msdn](https://github.com/schmotzle/binja-msdn)|[Benedikt Schmotzle](https://github.com/schmotzle)|[MIT](binja-msdn/LICENSE)|ui|Search MSDN api reference|
|[Binja Architecture Reference](https://github.com/ehennenfent/binja_arch_ref)|[Eric Hennenfent](https://github.com/ehennenfent)|[MIT](binja_arch_ref/LICENSE)|ui|Binary Ninja plugin to display a cheat sheet with information about the current architecture|
|[LC-3 Architecture Plugin](https://github.com/kapaw/binaryninja-lc3)|[Paw Petersen](https://github.com/kapaw)|[MIT](binaryninja-lc3/LICENSE)|architecture|Disassembler for the LC-3 architecture.|
|[Binary Ninja Dynamic Analysis Tools](https://github.com/ehennenfent/binja_dynamics)|[Eric Hennenfent](https://github.com/ehennenfent)|[Apache 2](binja_dynamics/LICENSE)|dynamic, education, ui|Adds a series of dynamic analysis tools aimed at beginners to Binary Ninja.|
|[Intel 8051 Family Architecture Plugin](https://github.com/amtal/i8051)|[amtal](https://github.com/amtal)|[AGPLv3](i8051/LICENSE)|architecture|Disassembler for the 8051 architecture family.|
|[Binja Sibyl](https://github.com/kenoph/binja_sibyl)|[Paolo Montesel (github.com/kenoph)](https://github.com/kenoph)|[BSD 2-Clause License](binja_sibyl/LICENSE)|binaryview, ui|Sibyl plugin for Binja|
|[SPU Cell Architecture Plugin](https://github.com/bambu/binaryninja-spu)|[Bambu](https://github.com/bambu)|[MIT](binaryninja-spu/LICENSE)|architecture, core, ui|A disassembler for the SPU Cell architecture.|
|[SyscallIdentify](https://github.com/HascoetKevin/SyscallsIdentifier_BinaryNinja)|[Kevin Hascoët <neolex@email.com>](https://github.com/HascoetKevin)|[MIT](SyscallsIdentifier_BinaryNinja/LICENSE)|binaryview|A plugin that identify the syscalls.|
|[AVR Architecture Plugin](https://github.com/cah011/binja-avr)|[Carl Hurd](https://github.com/cah011)|[MIT](binja-avr/LICENSE)|architecture, core, ui|A disassembler for the AVR architecture.|
|[Sensei](https://github.com/ehennenfent/binja_sensei)|[Eric Hennenfent](https://github.com/ehennenfent)|[MIT](binja_sensei/LICENSE)|ui|A wrapper around several plugins that may be of use to beginners|
|[Frida Plugin](https://github.com/chame1eon/binaryninja-frida)|[Chame1eon](https://github.com/chame1eon)|[MIT](binaryninja-frida/LICENSE)|binaryview, core, ui|A plugin to integrate the Frida dynamic instrumentation toolkit into Binary Ninja.|
|[LLIL](https://github.com/ColdHeat/liil)|[Kevin Chung](https://github.com/ColdHeat)|[MIT](liil/LICENSE)|ui|Linear IL view for Binary Ninja|


