# move

Example `Python` application to practice `nix` packaging.

The program lets you move the terminal cursor with arrow keys. `Enter` toggles "drawing" mode, which highlights any cell the cursor passes. Any other keyboard press writes the respective character to the cell under the cursor.

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

  
