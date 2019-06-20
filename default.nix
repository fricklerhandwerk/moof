with import <nixpkgs> {};
with python35Packages;
buildPythonPackage rec {
  name = "move";
  src = ".";

  buildInputs = [ pbr ];
}
