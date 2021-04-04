# COVID-19 Bot

This is an open source bot for querying information about **Novel Coronavirus (COVID-19)**.

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This is an open source bot for querying information about **Novel Coronavirus (COVID-19)**.

The data mainly comes from [M-Media-Group/Covid-19-API](https://github.com/M-Media-Group/Covid-19-API) repository.

## Features

Currently, the Bot considers India and the states within. Bot is able to answers questions related COVID-19. It uses custom spell checker and handle out of scope also. Some of the sample questions it supports are as follows</br>

- What is the total number of deaths in india
- Recovered cases in india
- Confirmed cases in india
- Active cases in Maharashtra
- Active cases in Maharashtra and Goa
- Confirmed cases in West Bengal
- Most affected states
- Most recovered states
- Least affected states
- Recovery rate in Karnataka
- Recovery rate in Karnataka and Goa
- Mortality rate in Goa
- fully vaccinated people in India
- patial vaccinated people in India
- people fully vaccinated in India

### Built With

- [Rasa : 2.0.2 ](https://rasa.com/docs/rasa/)
- [Python : 3.8 ](https://www.python.org/)
- [Rasa-SDK Action Server : 2.4.0 ](https://rasa.com/docs/action-server)

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python
- Pipenv

### Installation

1. Clone the repo
   ```
   git clone https://github.com/sumanentc/COVID-19-bot.git
   ```
2. Install dependencies

   ```
   pipenv shell

   pipenv install
   ```

3. Train the model

   ```
   rasa train

   ```

4. Start the Action Server

   ```
   rasa run actions

   ```

<!-- USAGE EXAMPLES -->

## Usage

1. Start the Action Server locally

   ```
   rasa run actions

   ```

2. To build the Action Server image using the Dockerfile

```
docker build actions/ -t sumand/rasa-action-server:2.4.0

```

3. To Run the Action Server using the Docker Image

```
docker run -p 5055:5055 --name my-action-server sumand/rasa-action-server:2.4.0

```

4. To train RASA models

```
rasa train

```

5. To start RASA shell

```
rasa shell

```

6. To install RASA-X using Helm Chart

```
kubectl create namespace rasa

helm repo add rasa-x https://rasahq.github.io/rasa-x-helm

helm --namespace rasa install --values values.yml my-release rasa-x/rasa-x

helm --namespace rasa upgrade --values values.yml my-release rasa-x/rasa-x

```

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [M-Media-Group/Covid-19-API](https://github.com/M-Media-Group/Covid-19-API)
- [Install RASA-X using Helm Chart](https://rasa.com/docs/rasa-x/installation-and-setup/install/helm-chart/)
