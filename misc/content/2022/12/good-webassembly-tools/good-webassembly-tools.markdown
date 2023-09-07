Status: published
Date: 2022-12-04 10:15:25
Modified: 2023-09-07 15:03:07
Author: Benjamin Du
Slug: good-webassembly-tools
Title: Good Webassembly Tools
Category: Computer Science
Tags: Computer Science, programming, WASM, WebAssembly, Rust

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [wizer](https://github.com/bytecodealliance/wizer)
[wizer](https://github.com/bytecodealliance/wizer)
Don't wait for your Wasm module to initialize itself, pre-initialize it! Wizer instantiates your WebAssembly module, executes its initialization function, and then snapshots the initialized state out into a new WebAssembly module. Now you can use this new, pre-initialized WebAssembly module to hit the ground running, without making your users wait for that first-time set up code to complete.

## [extism](https://github.com/extism/extism)
[extism](https://github.com/extism/extism)
is a universal plug-in system 
which runs WebAssembly extensions inside your app.

## [modsurfer](https://github.com/dylibso/modsurfer)
[modsurfer](https://github.com/dylibso/modsurfer)
For developers, SRE, DevOps, and engineering leaders: understand what the WebAssembly in your system is all about. 
Modsurfer provides critical information about WebAssembly code through a handy GUI, or directly at your fingertips via our CLI.

## [observe-sdk](https://github.com/dylibso/observe-sdk)
[observe-sdk](https://github.com/dylibso/observe-sdk)
provides observability SDKs for WebAssembly, enabling continuous monitoring of WebAssembly code as it executes within a runtime.

## [chainsocket](https://github.com/dylibso/chainsocket)
[chainsocket](https://github.com/dylibso/chainsocket)
Proof of concept for a generative AI application framework powered by WebAssembly and Extism

