# Mirinae website search for GoldenDict

This is a small script for applying mirinae.io Korean grammar analysis designed to be used for GoldenDict popup functionality.
Support is given for Linux, tested on NixOS.

![](./img/plugin.gif)

### How it works

1. Selenium using Mozilla's `geckodriver` makes a request on mirinae.io
2. Screenshot is taken and saved in `/tmp`
3. Screenshot is converted to Base64 and embedded in website

### Dependencies

```nix
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
```

as in `shell.nix`:
- selenium (Python pip)
- pybase64 (Python pip)
- geckodriver (OS package manager)

### How to invoke script using GoldenDict

1. Add new dictionary under Programs in GoldenDict:
`python /absolute/path/to/mirinae-website-search.py --url %GDWORD%`

Due to me using NixOS, the script is invoked with a Nix shell as in `shellscript.sh`
My command looks like: `sh /absolute/path/to/shellscript.sh %GDWORD%`

### Caveats

- Each request takes some time to process
- There is also a mirinae.io extension for Chromium if this functionality is purely wanted for the browser
