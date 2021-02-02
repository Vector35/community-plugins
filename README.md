# Binary Ninja Plugins

| PluginName | Author | Last Updated | License | Type | Description |
|------------|--------|--------------|---------|----------|-------------|
|[Improved Gameboy Architecture](https://github.com/ZetaTwo/binja-gameboy)|[Carl Svensson (@zetatwo)](https://github.com/ZetaTwo)|2021-01-23|MIT|architecture, binaryview|A loader and diassembler for Game Boy ROMs.|
|[Rust Demangle](https://github.com/inspier/BinjaRustDemangler)|[inspier](https://github.com/inspier)|2021-01-06|MIT|helper|Demangles Rust symbols.|
|[BD Viewer](https://github.com/PistonMiner/binaryninja-bindiff-viewer)|[Linus S. (aka PistonMiner)](https://github.com/PistonMiner)|2020-12-16|MIT|helper, ui|View BinDiff results and port symbols|
|[DeGObfuscate](https://github.com/kryptoslogic/binja_degobfuscate)|[Jamie Hankins](https://github.com/kryptoslogic)|2020-12-02|MIT|helper|De-obfuscates strings inside of obfuscated Go binaries|
|[Symgrate2 Plugin](https://github.com/travisgoodspeed/symgrate2-binja-plugin)|[Travis Goodspeed](https://github.com/travisgoodspeed)|2020-11-25|MIT|helper|This is a client plugin for recovering symbols using the Symgrate2 server.|
|[VulnFanatic](https://github.com/Martyx00/VulnFanatic)|[Martin Petran](https://github.com/Martyx00)|2021-01-07|Apache-2.0|helper|Assistant plugin for vulnerability research.|
|[Ghinja](https://github.com/Martyx00/ghinja)|[Martin Petran](https://github.com/Martyx00)|2020-12-17|Apache-2.0|ui|Plugin to embed Ghidra Decompiler into Binary Ninja|
|[SEPROM Loader](https://github.com/matteyeux/seprom-loader)|[matteyeux](https://github.com/matteyeux)|2021-01-05|MIT|binaryview|Binary View for loading 32 bits and 64 bits Apple SEPROM|
|[devi](https://github.com/murx-/devi_binja)|[@_murks](https://github.com/murx-)|2020-11-04|MIT|helper, ui|devi - DEvirtualize VIrtual calls in C++ binaries|
|[Golang Symbol Restore](https://github.com/d-we/binja-golang-symbol-restore)|[Daniel Weber](https://github.com/d-we)|2020-10-19|MIT|helper|Binary Ninja plugin for restoring function names from stripped Golang binaries|
|[GO Loader Assist](https://github.com/f0rki/bn-goloader)|[Michael Rodler](https://github.com/f0rki)|2021-02-02|MIT|ui|Short script that parses go symbol table and renames/creates functions.|
|[BNHook](https://github.com/jeffli678/bnhook)|[Grant Orndorff](https://github.com/jeffli678)|2020-06-07|MIT|core, ui|Insert custom hooks|
|[Nampa](https://github.com/thebabush/nampa)|[Paolo Montesel (https://github.com/thebabush)](https://github.com/thebabush)|2020-05-27|LGPL v3|binaryview, core|FLIRT for (binary) ninjas|
|[YARA Scan](https://github.com/trib0r3/binja-yara)|[trib0r3](https://github.com/trib0r3)|2020-05-26|MIT|binaryview, core|YARA signatures|
|[Dependency analyzer](https://github.com/Shizmob/binja-depanalyzer)|[Shiz](https://github.com/Shizmob)|2020-05-24|MIT|helper|Analyze dependencies and resolve obfuscated imports|
|[HLIL Dump](https://github.com/atxsinn3r/BinjaHLILDump)|[atxsinn3r](https://github.com/atxsinn3r)|2020-06-07|BSD-3-Clause|helper|Dumps HLIL code to a directory|
|[GEF-Binja](https://github.com/hugsy/gef-binja)|[hugsy](https://github.com/hugsy)|2020-05-18|MIT|helper, ui|Interface Binary Ninja with GDB-GEF easily.|
|[msp430 Architecture](https://github.com/joshwatson/binaryninja-msp430)|[Josh Watson](https://github.com/joshwatson)|2019-09-06|MIT|architecture|MSP430 Architecture Plugin for Binary Ninja|
|[binja_sigmaker](https://github.com/apekros/binja_sigmaker)|[apekros and Alex3434](https://github.com/apekros)|2020-08-19|MIT|architecture, binaryview, core, ui|Generate and find signatures.|
|[Jump table branch editor](https://github.com/Vasco-jofra/jump-table-branch-editor)|[jofra](https://github.com/Vasco-jofra)|2019-07-06|MIT|core, ui|A plugin that eases fixing jump table branches|
|[bnida](https://github.com/zznop/bnida)|[zznop](https://github.com/zznop)|2020-07-22|MIT|helper|Transfer analysis data between Binary Ninja and IDA|
|[genesis](https://github.com/zznop/bn-genesis)|[zznop](https://github.com/zznop)|2019-07-23|MIT|patch|SEGA Megadrive/Genesis ROM Hacking Toolkit|
|[kallsyms](https://github.com/zznop/bn-kallsyms)|[zznop](https://github.com/zznop)|2020-07-22|MIT|helper|Parses output from /proc/kallsyms and applies symbols to the corresponding kernel BN database|
|[recursion](https://github.com/zznop/bn-recursion)|[zznop](https://github.com/zznop)|2020-07-22|MIT|helper|Locate and annotate direct and indirect recursion|
|[Annotate Functions](https://github.com/bkerler/annotate)|[B.Kerler with code from John Levy and @carstein](https://github.com/bkerler)|2019-07-09|MIT|binaryview|A plugin that annotates function arguments.|
|[VMNDH-2k12 Architecture Plugin](https://github.com/verylazyguy/binaryninja-vmndh)|[verylazyguy](https://github.com/verylazyguy)|2019-07-10|MIT|architecture|A disassembler and lifter for the VMNDH-2k12 architecture.|
|[MSVC](https://github.com/0x1F9F1/binja-msvc)|[Brick](https://github.com/0x1F9F1)|2019-07-12|MIT|helper|Parses MSVC structures to improve analysis|
|[AVR Architecture Plugin](https://github.com/fluxchief/binaryninja_avr)|[Kevin Hamacher](https://github.com/fluxchief)|2019-07-12|MIT|architecture, binaryview|AVR architecture plugin + lifter.|
|[BNIL Instruction Graph](https://github.com/withzombies/bnil-graph)|[Ryan Stortz (@withzombies)](https://github.com/withzombies)|2020-07-16|Apache-2.0|ui|A plugin to graph BNIL instruction trees|
|[Sourcery Pane](https://github.com/mechanicalnull/sourcery_pane)|[mechanicalnull](https://github.com/mechanicalnull)|2019-07-14|MIT|helper, ui|Synchronized source code pane for debug binaries|
|[Frida](https://github.com/chame1eon/binaryninja-frida)|[Chame1eon](https://github.com/chame1eon)|2020-06-01|MIT|helper|A plugin to integrate the Frida dynamic instrumentation toolkit into Binary Ninja.|
|[Format String Finder](https://github.com/Vasco-jofra/format-string-finder-binja)|[jofra](https://github.com/Vasco-jofra)|2019-07-15|MIT|helper|Finds format string vulnerabilities|
|[Windows Driver Analyzer](https://github.com/shareef12/driveranalyzer)|[shareef12](https://github.com/shareef12)|2019-08-07|MIT|helper|Find IRP dispatch routines and valid IOCTLs in a Windows kernel driver|
|[Syscaller](https://github.com/carstein/Syscaller)|[Michal Melewski](https://github.com/carstein)|2019-07-15|MIT|helper|Decorate encountered syscalls with details like name and arguments|
|[peutils](https://github.com/404d/peutils)|[404'd](https://github.com/404d)|2020-12-12|MIT|helper|Binary Ninja plugin providing various niche utilities for working with PE binaries|
|[Auto Utils](https://github.com/404d/autoutils)|[404'd](https://github.com/404d)|2020-12-12|MIT|helper|Various auto analysis utilities|
|[bncov](https://github.com/ForAllSecure/bncov)|[Mark Griffin](https://github.com/ForAllSecure)|2020-12-18|MIT|helper|Code coverage analysis and visualization plugin|
|[SVD Memory Map Parser](https://github.com/ehntoo/binaryninja-svd)|[Mitchell Johnson (@ehntoo)](https://github.com/ehntoo)|2020-10-13|MIT or Apache 2.0|helper|A parser for the CMSIS System View Description format|
|[Function ABI](https://github.com/whitequark/binja_function_abi)|[whitequark](https://github.com/whitequark)|2019-09-04|BSD-0-clause|ui|A plugin that adds a GUI for changing function ABI.|
|[Itanium C++ ABI](https://github.com/whitequark/binja_itanium_cxx_abi)|[whitequark](https://github.com/whitequark)|2020-05-17|BSD-0-clause|analysis|A plugin providing an analysis for Itanium C++ ABI.|
|[Intel 8086 Architecture](https://github.com/whitequark/binja-i8086)|[whitequark](https://github.com/whitequark)|2019-09-04|BSD-0-clause|arch|A plugin providing the 16-bit Intel architecture.|
|[Renesas M16C Architecture](https://github.com/whitequark/binja-m16c)|[whitequark](https://github.com/whitequark)|2020-01-19|BSD-0-clause|architecture|A plugin providing the Renesas M16C architecture.|
|[Instruction Slicer](https://github.com/c3r34lk1ll3r/Instruction_Slicer)|[Andrea Ferraris](https://github.com/c3r34lk1ll3r)|2020-11-25|MIT|helper|Forward and backward instruction slicer|
|[BinRida](https://github.com/c3r34lk1ll3r/BinRida)|[Andrea Ferraris](https://github.com/c3r34lk1ll3r)|2019-09-26|MIT|helper|This plugin allows to stalk, dump and instrument a process using Frida functionalities.|
|[Game Boy Loader and Architecture Plugin](https://github.com/icecr4ck/bnGB)|[Hugo Porcher (@icecr4ck)](https://github.com/icecr4ck)|2020-11-17|MIT|architecture, binaryview|A loader and diassembler for Game Boy ROMs.|
|[Motorola 68k Architecture Plugin](https://github.com/wrigjl/binaryninja-m68k)|[Alex Forencich](https://github.com/wrigjl)|2020-12-30|MIT|architecture|A disassembler and lifter for the Motorola 68k architecture.|
|[Clean Tricks](https://github.com/janbbeck/CleanTricks)|[Jan Beck](https://github.com/janbbeck)|2020-06-08|MIT|architecture, binaryview, core, helper, ui|This plugin removes some simple known obfuscation techniques to cut down on the tedium.|
|[bn-riscv](https://github.com/uni-due-syssec/bn-riscv)|[Katharina Utz](https://github.com/uni-due-syssec)|2021-01-18|Apache-2.0|architecture|RISC-V architecture plugin.|
|[Division and Modulo Deoptimizer](https://github.com/jmprdi/binja-division-deoptimization)|[Nathan Peercy](https://github.com/jmprdi)|2020-05-11|MIT|binaryview, helper, ui|Deoptimize Divisions and Modulos in Binary Ninja.|
|[IDC Importer](https://github.com/Cryptogenic/idc_importer)|[SpecterDev](https://github.com/Cryptogenic)|2020-03-26|MIT|helper|Allows users to import idc database dumps from IDA into Binary Ninja.|
|[revsync](https://github.com/lunixbochs/revsync)|[lunixbochs](https://github.com/lunixbochs)|2020-05-13|MIT|ui|Realtime IDA Pro and Binary Ninja sync plugin|
|[DUMB](https://github.com/toolCHAINZ/DUMB)|[toolCHAINZ](https://github.com/toolCHAINZ)|2020-03-01|MIT|architecture, binaryview|DUMB: An Example Architecture for Binary Ninja|
|[hexfiles](https://github.com/toolCHAINZ/hexfiles)|[toolCHAINZ](https://github.com/toolCHAINZ)|2020-10-03|MIT|binaryview|A simple loader for Motorola SREC, Intel HEX, and TI-TXT files.|
|[WASM Plugin](https://github.com/CarveSystems/binjawa)|[Meador Inge](https://github.com/CarveSystems)|2020-06-30|MIT|architecture, binaryview|This is a plugin for disassembling and lifting WASM images..|
|[VTIL Plugin](https://github.com/vtil-project/VTIL-BinaryNinja)|[Layle](https://github.com/vtil-project)|2020-07-04|BSD-3-Clause|architecture, binaryview|Integrates the VTIL (Virtual-machine Translation Intermediate Language) Project with Binary Ninja|
|[Switch Loader](https://github.com/EliseZeroTwo/Switch-Binja-Loader)|[EliseZeroTwo](https://github.com/EliseZeroTwo)|2020-07-22|ISC|binaryview, helper|Loader for common Nintendo Switch binaries|
|[SENinja](https://github.com/borzacchiello/seninja)|[Luca Borzacchiello](https://github.com/borzacchiello)|2020-10-27|2-Clause BSD|helper|Symbolic execution plugin for BinaryNinja|
|[Discord Rich Presence Integration](https://github.com/x1tan/binaryninja-discord-integration)|[xitan](https://github.com/x1tan)|2020-07-17|MIT|helper|Enables Discord Rich Presence Integration for Binary Ninja|
|[cryptoscan](https://github.com/Rami114/cryptoscan)|[Ben Pottier](https://github.com/Rami114)|2020-08-02|MIT|binaryview, ui|A plugin to detect several common crypto constructs and magic vars.|
|[CHIP-8 ROM Loader](https://github.com/uafio/BinaryNinja-CHIP8-Arch)|[uafio](https://github.com/uafio)|2020-08-15|MIT|architecture, binaryview, core, helper, ui|Load and disassemble CHIP-8 ROM.|
|[Emotet API+string deobfuscator](https://github.com/mauronz/binja-emotet)|[Francesco Muroni](https://github.com/mauronz)|2020-09-21|MIT|helper|Deobufscate API calls and strings in unpacked Emotet samples.|
|[iBoot64 Loader](https://github.com/BlackwingHQ/iBoot64Binja)|[Blackwing Intelligence](https://github.com/BlackwingHQ)|2020-10-01|MIT|binaryview|Binary View for loading iBoot, SecureROM, etc. firmware|
|[logrn](https://github.com/sum-catnip/logrn)|[catnip](https://github.com/sum-catnip)|2020-10-02|MIT|helper|binary ninja plugin for abusing logging functions|
|[Delphi VMT Analyzer](https://github.com/ImNotAVirus/delphi_ninja)|[ImNotAVirus](https://github.com/ImNotAVirus)|2020-10-02|MIT|helper|Find Delphi VMTs and generate their structures|
# Binary Ninja Community Plugins

Plugins in this repository are provided by the community. Vector 35, Inc. makes no guarantees to the quality, safety or efficacy of the plugins herein.

## Official Plugins

This repository tracks third-party plugins, but many official plugins are provided by Vector 35 that offer additional functionality:

 - [Example Plugins](https://github.com/Vector35/binaryninja-api/tree/dev/python/examples) are included with all installs of Binary Ninja and can [be installed](https://github.com/Vector35/binaryninja-api/tree/dev/python/examples#loading-plugins) from there
 - [Official Samples](https://github.com/Vector35/official-plugins) a fully formed repository of official plugins
 - [Sample Plugin](https://github.com/Vector35/sample_plugin) if you're looking for a template to build a new plugin from

## Installing Plugins

To install plugins, you can either use the Plugin Manager in the UI or clone the repositories linked here in into your [plugin folder](https://github.com/Vector35/binaryninja-api/tree/dev/python/examples#loading-plugins).

## Contributing Plugins

 1. Create a new repository (Optionally, just copy it from the [sample plugin](https://github.com/Vector35/sample_plugin))
 1. Fill out a [`plugin.json`](https://github.com/Vector35/sample_plugin/blob/master/plugin.json). Optionally you can use the `generate_plugininfo.py -i` to interactively walk you through setting the required fields. The `plugin.json` must pass all the checks when run through `generate_plugininfo.py -v plugin.json`. `generate_plugininfo.py` can also generate your `README.md` and your `LICENSE` file with the `-r`, `-l`, or `-a` (all) options. Below is a list of the required and recommended fields.
 1. Create and push a git tag with the version of your plugin (e.g. `v1.1`). Create a release, optionally attaching build artifacts as required.
 1. File an [issue](https://github.com/Vector35/community-plugins/issues) with a link to your repo and the tag name of the release.
 1. To update your plugin repeat the two previous steps.

### Required Fields

To be displayed in the plugin loader, your `plugin.json` MUST have the following fields:

 - `pluginmetadataversion` - The current version is the integer `2`
 - `name` - Good names do not use "Binary Ninja" or "Binja" neither do they use the words "plugin" or "extension". So instead of "Binja 6502 Architecture Plugin" simply use "6502 Architecture"
 - `author` - Your name, handle, or company name.
 - `api` - A list of supported architectures. Though we support `python2` and `python3` we highly recommend plugin authors support `python3` as `python2` support will be dropped as some time in the near future.
 - `license` - A json object with `name` and `text` keys.
 - `description` - This is a short (<50 character) description of the plugin.
 - `longdescription` - A longer Markdown formatted description of the plugin including hyperlinks and images as needed.
 - `version` - Version string
 - `minimumBinaryNinjaVersion` - An integer _build number_ so instead of `1.1.555` use `555`.
 - `platforms` - A list of strings one for each supported platform. Valid platforms are `Darwin`, `Linux`, and `Windows`

### Recommended Fields

 - `type` - A list of strings of the following types: `core`, `ui`, `architecture`, `binaryview`, and `helper`.
   - `helper` - Plugin that adds some base functionality to Binary Ninja. Most plugins will be of this type.
   - `ui` - The plugin extends the UI is some way.
   - `architecture` - The plugin adds an architecture (e.g. `x86`, `ARM`, `MIPS`).
   - `binaryview` - The plugin adds a new BinaryView (e.g. `PE`, `MachO`, `ELF`).
   - `core` - Plugin that extends the core's analysis. Your plugin probably isn't one of these.
 - `installinstructions` - A json object with keys for each supported platform listed in `platforms` and text Markdown formatted.

## License

Note that content contained in the root of this repository itself is Copyright 2016, Vector 35, Inc. and [available](LICENSE) under an MIT license, but each individual plugin may be released under a different license.

