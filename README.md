# moof

Interactive terminal UI application written in `Python` to practice `nix` packaging.

## Controls

- arrow keys: move cursor
- `Enter` or `Space`: toggle "drawing" mode (highlight cells under cursor in chosen color)
- Numbers 1-9: select drawing color
- `Backspace`: clear screen
- `Escape`: quit program

All changes to the screen state are recorded to a file in the current directory. This way the produced images can in principle be recreated.

## Installation

Run `moof` without installing:

    cd moof
    nix-shell --run moof

To add `moof` to an environment, add the package in the appropriate place (`buildInputs`, `environment.systemPackages`, `home.packages`, etc.) by importing this repository's directory. Example:

    let
      moof = builtins.fetchGit {
        url = "https://github.com/fricklerhandwerk/moof";
        ref = "master";
      };
    in
    home.packages = [
      # ...
      (import moof)
    ];

  
