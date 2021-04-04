FROM rasa/rasa-sdk:2.4.0

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
COPY requirements.txt ./

# Change back to root user to install dependencies
USER root

RUN apt-get update
RUN apt update

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip install -r requirements.txt

# Copy actions folder to working directory
COPY . /app/actions

# By best practices, don't run the code with root user
USER 1001

CMD ["start", "--actions", "actions"]
