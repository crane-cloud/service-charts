# Cranecloud JupyterLab with Production Kernel Culling
# Built on the official Jupyter base image
FROM jupyter/base-notebook:latest

# Switch to root for system-wide changes
USER root

# Create Jupyter configuration directory and add kernel culling settings (production)
RUN mkdir -p /etc/jupyter && \
    echo "c.MappingKernelManager.cull_idle_timeout = 1800" >> /etc/jupyter/jupyter_server_config.py && \
    echo "c.MappingKernelManager.cull_interval = 300" >> /etc/jupyter/jupyter_server_config.py && \
    echo "c.MappingKernelManager.cull_connected = False" >> /etc/jupyter/jupyter_server_config.py && \
    echo "c.MappingKernelManager.cull_busy = False" >> /etc/jupyter/jupyter_server_config.py && \
    echo "c.MappingKernelManager.cull_terminated = True" >> /etc/jupyter/jupyter_server_config.py && \
    echo "c.MappingKernelManager.max_kernels = 5" >> /etc/jupyter/jupyter_server_config.py && \
    echo "c.MappingKernelManager.log_kernel_culling = True" >> /etc/jupyter/jupyter_server_config.py && \
    echo "c.Application.log_level = 'INFO'" >> /etc/jupyter/jupyter_server_config.py

# Create a startup script with Cranecloud branding
RUN echo '#!/bin/bash' > /usr/local/bin/start-jupyter && \
    echo 'echo "==============================================="' >> /usr/local/bin/start-jupyter && \
    echo 'echo "🚀 Starting Cranecloud JupyterLab..."' >> /usr/local/bin/start-jupyter && \
    echo 'echo "   Powered by Cranecloud Infrastructure"' >> /usr/local/bin/start-jupyter && \
    echo 'echo "   Production-ready with kernel culling"' >> /usr/local/bin/start-jupyter && \
    echo 'echo "==============================================="' >> /usr/local/bin/start-jupyter && \
    echo 'echo "⚙️  Kernel Culling Settings:"' >> /usr/local/bin/start-jupyter && \
    echo 'echo "   • Idle timeout: 30 minutes"' >> /usr/local/bin/start-jupyter && \
    echo 'echo "   • Check interval: 5 minutes"' >> /usr/local/bin/start-jupyter && \
    echo 'echo "   • Max kernels: 5"' >> /usr/local/bin/start-jupyter && \
    echo 'echo "   • Connected culling: Disabled"' >> /usr/local/bin/start-jupyter && \
    echo 'echo "   • Logging: Enabled"' >> /usr/local/bin/start-jupyter && \
    echo 'echo "==============================================="' >> /usr/local/bin/start-jupyter && \
    echo 'jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --LabApp.token="" --LabApp.password=""' >> /usr/local/bin/start-jupyter && \
    chmod +x /usr/local/bin/start-jupyter

# Add Cranecloud metadata labels
LABEL org.cranecloud.name="cranecloud-jupyterlab" \
      org.cranecloud.description="Production JupyterLab with kernel culling" \
      org.cranecloud.maintainer="Cranecloud Team"

# Revert to standard user
USER ${NB_UID}

# Set the default command to start JupyterLab
CMD ["/usr/local/bin/start-jupyter"]