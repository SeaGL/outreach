{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
	nativeBuildInputs = with pkgs; [
		python312
		python312Packages.segno
		python312Packages.pillow
#		python312Packages.pillowfight
                python312Packages.pip
#                python311Packages.svgelements
#                python311Packages.pysvg-py3
#                python311Packages.svg-path
#                python311Packages.svgutils
#                python311Packages.svg-py
                python312Packages.cairosvg
	];

	shellHook = ''
		python -m venv .venv
		source .venv/bin/activate
		pip install qrcode-artistic
	'';
}
