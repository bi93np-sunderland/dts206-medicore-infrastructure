# ==========================================
# STAGE 1: The Builder Environment
# ==========================================
FROM python:3.10-slim AS builder

WORKDIR /build

# Copy only the requirements file first to cache the dependencies
COPY requirements.txt .

# Install dependencies into a local user directory to easily copy them later
RUN pip install --user --no-cache-dir -r requirements.txt

# ==========================================
# STAGE 2: The Production Environment
# ==========================================
FROM python:3.10-slim

WORKDIR /app

# Create a secure, non-root user with ID 1001
RUN useradd -m -u 1001 appuser

# Copy the installed python dependencies from the builder stage
COPY --from=builder /root/.local /home/appuser/.local

# Copy the actual application code
COPY . .

# Ensure the system knows where the Python packages are installed
ENV PATH=/home/appuser/.local/bin:$PATH

# Hand over ownership of the application folder to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER 1001

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
