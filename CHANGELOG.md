# v1.2

- Update the shifted native map presenter address for Steam build 25480438.
- Keep saved keyboard bindings and Tab fallback.
- Offline builds and package checks pass; live gameplay validation remains pending.

# Changelog

## 1.1

- Integrate the saved keyboard shortcut from the separately installed Mod Bindings Menu.
- Retain Tab as the fallback when the binding addon is unavailable.
- Package as a standalone release for Bingus Shared Loader; also available as a Megapack option.

## 1.0

- Allow the native Hologram request only from the ship's observed idle menu state (presenter 0, stack depth 0). The 0.9 live log showed Tab was detected but blocked because its guard expected an already open Main menu.
- Live testing confirmed that Tab opens the Galactic Map from a clear spot away from the table, without moving the player or requiring the interaction prompt. The first opening had a noticeable delay; subsequent openings were smooth.

## 0.9

- Replace the enlarged table interaction and synthetic E input with the game's native Hologram presenter entry. The normal interaction prompt and player approach are no longer involved.
- Verify both current game modules by SHA-256 and the native presenter instruction prefix before binding the function.
- Attempt to open from Main presenter state aboard the Super Destroyer. The live game showed this guard did not match normal gameplay.
- Withdraw 0.8 after the live test showed that its larger radius still required targeting the table and moved the player.

## 0.8

- Continue probing the map template through the ship loading transition. Version 0.7 stopped after five searches before the game decrypted the template, leaving Tab inactive.
- Locate the current build's 46,616,576-byte decrypted entity region and validate the full map record before changing its four radii. This avoids repeatedly scanning its full contents during startup.

## 0.7

- Withdraw the 0.6 temporary-entity approach after a live Tab press crashed the game. The log stopped during that path, before it reported a successful spawn.
- Enlarge only the existing map interaction radius in the captured game template before the ship interaction is created. Keep view distances and priorities unchanged so normal nearby interactions retain their behavior.
- Send E only when the template was prepared before the current ship loaded. The map opening from a distance still needs an in-game check.

## 0.6 (withdrawn)

- Attempt to spawn `galactic_campaign_interact_point` at the local avatar's position on Tab, then remove it after the interaction window. A live Tab press crashed the game, so this version must not be used.
- Remove the static interaction-resource memory scan and patch. The previous version could send E at the table, but changing that template did not make the live interaction reachable from elsewhere on the ship.
- Log entity spawning, player-position lookup, input, and cleanup separately.

## 0.5

- Resolve `SendInput` from `user32.dll`, where Windows exports it. The live log showed that ship detection, interaction-record lookup, and Tab detection worked, but the previous `kernel32.dll` lookup left the synthetic interact key unavailable.
- Distinguish a missing `SendInput` export from a failed input call in the mod log.

## 0.4

- Detect the galaxy table unit placed in the ship hub.
- Remove the unrelated interaction-point resource check that never matched a placed unit.

## 0.3

- Pass the galaxy table's captured IdString64 to the engine's unit lookup.

## 0.2

- Check every active Stingray world for the ship's galaxy interaction point.
- Log callback, world detection, scan, and input stages for troubleshooting.

## 0.1

- Add a Tab shortcut for the Galactic War menu while aboard the Super Destroyer.
- Restore the galaxy table's captured interaction values after each shortcut.
- Restrict activation to the world containing the galaxy table.
- Package as a Bingus Shared Loader addon.

The 0.8 live test confirmed that the enlarged radius works but still requires
targeting the table and moves the player. The 0.9 live test confirmed that Tab
reached the addon, but its menu state guard blocked the native call.
