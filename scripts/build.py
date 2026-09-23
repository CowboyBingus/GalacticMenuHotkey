"""Build the versioned standalone Galactic Menu Hotkey addon."""
from pathlib import Path
import json
import sys
import zipfile

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE.parent / "BingusSharedLoader" / "scripts"))
from build_addon import build_addon

VERSION = "1.1"


def build():
    output = HERE / "releases" / f"Galactic-Menu-Hotkey-v{VERSION}.zip"
    build_addon("mods/cowboybingus/galactic_menu_hotkey",
                (HERE / "src" / "galactic_menu_hotkey.lua").read_bytes(),
                "3d8fdb82-9df6-4dc9-a538-5f94fc60a2e7", output,
                display_name=f"Galactic Menu Hotkey v{VERSION}")
    with zipfile.ZipFile(output) as archive:
        files = {name: archive.read(name) for name in archive.namelist()}
    manifest = json.loads(files["manifest.json"])
    manifest["Description"] = ("Open the Galactic Map aboard your ship. Requires Bingus Shared Loader v16+. "
                               "Install Mod Bindings Menu separately to change the keyboard binding.")
    manifest["Options"][0]["Description"] = manifest["Description"]
    files["manifest.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    files["INSTALL.txt"] = (HERE / "INSTALL.txt").read_bytes()
    with zipfile.ZipFile(output, "w") as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return output


if __name__ == "__main__":
    print(build())
