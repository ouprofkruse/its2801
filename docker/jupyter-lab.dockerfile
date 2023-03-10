FROM jupyter/minimal-notebook

ARG DOTNET_VERSION=6.0
ENV DOTNET_ROOT=${HOME}/.dotnet
ENV PATH=${PATH}:${DOTNET_ROOT}:${DOTNET_ROOT}/tools

USER root

RUN apt-get update \
    && apt-get install -y libc6 libgcc-12-dev libgssapi-krb5-2 libicu-dev libssl3 libstdc++6 zlib1g

USER ${NB_USER}

RUN wget https://dot.net/v1/dotnet-install.sh \
    && bash ./dotnet-install.sh --channel ${DOTNET_VERSION} \
    && dotnet tool install -g Microsoft.dotnet-interactive \
    && dotnet interactive jupyter install


RUN pip install --quiet --no-cache-dir nbgitpuller \
    jupyterlab-git \
    jupyterlab_github \
    jupyter-archive \
    jupyterlab-lsp \
    jupyterlab_play_cell_button \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"