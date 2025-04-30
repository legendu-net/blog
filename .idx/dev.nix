# To learn more about how to use Nix to configure your environment
# see: https://firebase.google.com/docs/studio/customize-workspace
{ pkgs, ... }: {
  channel = "stable-24.11";
  
  
  # Use https://search.nixos.org/packages to find packages
  packages = with pkgs; [
    bash-completion
    neovim
    gitui
    ripgrep
    rm-improved
    bat
    poetry
  ];

  # Sets environment variables in the workspace
  env = {
    PATH = [
      "$HOME/.local/bin"
    ];
  };
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      "asvetliakov.vscode-neovim"
      "ms-python.python"
      "ms-python.debugpy"
      "ms-toolsai.jupyter"
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
      };
      # Runs when the workspace is (re)started
      onStart = {
        poetry-project = ''
        poetry config --local virtualenvs.in-project true
        poetry install
        '';
        icon = ''
        curl -sSL https://raw.githubusercontent.com/legendu-net/icon/main/install_icon.sh | bash -s -- \
            -d ~/.local/bin
        '';
      };
    };
  };
}
