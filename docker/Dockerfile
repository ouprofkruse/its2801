FROM jupyter/minimal-notebook

ARG DOTNET_VERSION=7.0
ENV DOTNET_ROOT=/opt/dotnet
ENV PATH=${PATH}:${DOTNET_ROOT}:${DOTNET_ROOT}/tools

USER root

RUN apt-get update \
    && apt-get install -y libc6 libgcc-12-dev libgssapi-krb5-2 libicu-dev libssl3 libstdc++6 zlib1g

RUN wget https://dot.net/v1/dotnet-install.sh \
    && bash ./dotnet-install.sh --channel ${DOTNET_VERSION} --install-dir ${DOTNET_ROOT} \
    && dotnet tool install Microsoft.dotnet-interactive --tool-path /opt/dotnet/tools \
    && dotnet interactive jupyter install \
    && fix-permissions "/home/${NB_USER}"

USER ${NB_USER}

RUN pip install --quiet --no-cache-dir nbgitpuller \
    jupyterlab-git \
    jupyterlab_github \
    jupyter-archive \
    jupyterlab-lsp \
    jupyterlab_play_cell_button \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

# HK additions for python (based on CS1400 -- Shawn Ostermann)
RUN pip install numpy \
    pillow \
    Matplotlib \
    plotly \
    calysto \
    cairosvg \
    cairocffi \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"


