> Current local compatibility candidate for Steam build 25480438 / EXE 1.8.46015.0. Offline checks passed; live gameplay verification is pending.

# Galactic Menu Hotkey v1.2

Press **Tab** aboard the Super Destroyer to open the Galactic War Hologram menu. The addon calls the game's existing Hologram presenter directly. It does not enlarge the table interaction, show a distant interaction prompt, send Interact, or move the player toward the table.

Requires [Bingus Shared Loader v17 or newer / API 1](https://github.com/CowboyBingus/BingusSharedLoader/releases/latest). Install [Mod Bindings Menu](https://github.com/CowboyBingus/ModBindingsMenu/releases/latest) separately to change the keyboard shortcut under **Mouse & Keyboard > General > MODS**. Without it, the shortcut defaults to Tab. Controller button activation is not yet supported.

## Install

Import [Galactic-Menu-Hotkey-v1.2.zip](https://github.com/CowboyBingus/GalacticMenuHotkey/releases/latest) into Arsenal or HD2MM, enable this addon and Bingus Shared Loader, then deploy. Keep Bingus Shared Loader as the winning startup replacement. Restart Helldivers 2 after replacing version 0.8 so its enlarged interaction template is cleared.

## Compatibility and test status

This native call is guarded by the exact `game.dll` and `helldivers2.exe` SHA-256 values for Steam build **25480438** (EXE **1.8.46015.0**). It runs only when the ship's galaxy table is present and no menu presenter is active. A changed build, unavailable UI state, or another active menu leaves the shortcut inactive and writes the reason to `%LOCALAPPDATA%\CowboyBingus\Helldivers2\Logs\GalacticMenuHotkey.log`.

Offline tests confirm the function signature, the current build's presenter and screen enum mapping, and the mod's menu guards. A live test confirmed that Tab opens the map from a clear spot away from the table without moving the player. The first opening had a noticeable delay; later openings were smooth.

## Build and validate

Clone BingusSharedLoader beside this repository, then run `python -B scripts/build.py`. Run `luajit tests/test_hotkey.lua` on Windows to check native dispatch guards and binding integration. Optionally set `HD2_GAME_CAPTURE` to a local current-build game.dll memory capture to verify the native entry prefix; captures are not distributed.

Use either this standalone addon or its Vanilla Plus Megapack option. Mod Bindings Menu remains a separate install for either choice.

Current version: **v1.2**, for game build **25480438**. See [changes](CHANGELOG.md) and [validation coverage](docs/MIGRATION_VALIDATION.md).
