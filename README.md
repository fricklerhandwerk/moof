# move

Interactive terminal UI application written in `Python` to practice `nix` packaging.

## Controls

- arrow keys: move cursor
- `Enter`: toggle "drawing" mode (highlight cells under cursor in green)
- Numbers 1-9: select drawing color
- `Backspace`: clear screen
- `Escape`: quit program

All other keys will print the respective character at the cursor position without changing it.

Run `move` without installing:

    cd move
    nix-shell --run move

To add `move` to an environment, add the package in the appropriate place (`buildInputs`, `environment.systemPackages`, `home.packages`, etc.) by importing this repository's directory. Example:

    let
      move = builtins.fetchGit {
        url = "https://github.com/fricklerhandwerk/move";
        ref = "master";
      };
    in
    home.packages = [
      # ...
      (import move)
    ];

  
