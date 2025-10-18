{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: 
  let
    pkgs = nixpkgs.legacyPackages."x86_64-linux";
  in 
  {
    devShells."x86_64-linux".default = pkgs.mkShell {
      packages = with pkgs; [
        python312
        python312Packages.colorama
        python312Packages.aspell-python
        python312Packages.pyinstaller
        wineWowPackages.stable
        wget
        xorg.xvfb
        xorg.xrandr
        xvfb-run
      ];
      nativeBuildInputs = [ pkgs.pkg-config ];
      shellHook = ''
        export WINEPREFIX="$PWD/build/wine-prefix"
        export WINEARCH=win32
        echo -e "Welcome to the shell"
        '';
    };
  };
}
