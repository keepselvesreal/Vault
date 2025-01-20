# Use ubuntu as the base image
FROM ubuntu:latest

# Update Package lists and install necessary packages
RUN apt-get update && \
    apt-get install -y g++ python3 python3-pip python3-venv git htop redis-server

# Create a non-root user
RUN useradd -ms /bin/bash llamauser

# Set the working directory
WORKDIR /home/llamademo

# Create and activate virtual environment
RUN python3 -m venv /home/llamademo/venv
ENV PATH="/home/llamademo/venv/bin:$PATH"

# Expose ports for Streamlit and Flask
EXPOSE 8501
EXPOSE 5000

# Define environment variables with default values
ENV HF_REPO=TheBloke/Llama-2-7B-chat-GGML
ENV HF_MODEL_FILE=llama-2-7b-chat.ggmlv3.q2_K.bin
ENV DOWNLOAD_LATER=false

# Install required Python packages in virtual environment
COPY requirements.txt .
RUN /home/llamademo/venv/bin/pip install -r requirements.txt

# Copy necessary files into container
COPY chatbot chatbot
COPY ingestion ingestion

# Set necessary permissions and user
RUN chmod -R 777 /home
USER llamauser

# Add Hugging Face token as build argument
ARG HUGGINGFACEHUB_API_TOKEN
ENV HUGGINGFACEHUB_API_TOKEN=${HUGGINGFACEHUB_API_TOKEN}

# Run entrypoint.sh
CMD ["./chatbot/entrypoint.sh"]