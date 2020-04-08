with import <nixpkgs> {};
with python37Packages;
buildPythonApplication rec {
  name = "move";
  src = ./.;

  PBR_VERSION = "0.1.0";
  buildInputs = [ pbr ];
  propagatedBuildInput = [ blessed ];
}
