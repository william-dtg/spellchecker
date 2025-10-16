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
      ];
      nativeBuildInputs = [ pkgs.pkg-config ];
      shellHook = "
        echo -e \"\\e[1;32mWelcome to the shell\\e[0m\"
        ";
    };
  };
}
