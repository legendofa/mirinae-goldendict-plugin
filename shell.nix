with (import <nixpkgs> {});
let
  my-python-packages = python-packages: with python-packages; [
    selenium
    pybase64
  ];
  python-with-my-packages = python3.withPackages my-python-packages;
in
mkShell {
  buildInputs = [
  	geckodriver
    python-with-my-packages
  ];
}
