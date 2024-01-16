{
  sources ? import ./npins,
  system ? builtins.currentSystem,
}:
let
  pkgs = import sources.nixpkgs {
    inherit system;
    config = {};
    overlays = [];
  };
in
rec {
  moof = with pkgs.python3Packages; buildPythonApplication {
    name = "moof";
    src = ./.;
    buildInputs = [ ];
    propagatedBuildInputs = [ blessed ];
  };
  shell = pkgs.mkShell {
    packages = [
      moof
      pkgs.npins
    ];
  };
}
