with import <nixpkgs> {};
with python35Packages;
buildPythonApplication rec {
  name = "move";
  src = ./.;

  PBR_VERSION = "0.0.0";
  buildInputs = [ pbr ];
  propagatedBuildInput = [ blessed ];
}
