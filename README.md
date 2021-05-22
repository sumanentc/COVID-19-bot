# Covi-India-Bot

This is an open source bot useful for querying information related to **Novel Coronavirus (COVID-19)**.

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

This is an open source bot useful for querying information related to **Novel Coronavirus (COVID-19)**.
![RASA Shell](./images/rasa-cli.png)
![RASA-X ](./images/rasa-x.png)

The data mainly comes from [M-Media-Group/Covid-19-API](https://github.com/M-Media-Group/Covid-19-API) repository.

## Features

Currently, the Bot considers India and the states within.</br>
It has the below features.</br>

- It answers questions related COVID-19.
  - What is the total number of deaths in india?
  - How many recovered cases are there in india
  - How many confirmed cases are there in Ind
  - What is the total number of Active cases in Maharashtra
  - What is the total number of actve cases in Maharashtra and Goa
  - How many Confirmed cases are there in West Bengal
  - Which states are Most affected
  - Which states have maximum recovered states
  - Which states have most deaths
  - Which states are Least affected ?
  - What is the Recovery rate in Karnataka
  - What is the Recovery rate in Karnataka and Goa
  - What is the Mortality rate in Goa
- It can handle spelling mistakes.

- It can answers questions related to vaccination.

  - Number of people patially vaccinated in India
  - Number of people fully vaccinated

- It can answers questions related to vaccination slots availability.

  - Slots available in Pune
  - Slots available in Mumbai
  - Slots available in 400066

- It can handle out of context questions.

  - How are you?
  - How is the weather?

- It has RASA-X UI for Interactive training and usage

- It supports Facebok Messanger

### Built With

- [Rasa : 2.5.0 ](https://rasa.com/docs/rasa/)
- [Python : 3.8 ](https://www.python.org/)
- [Rasa-SDK Action Server : 2.5.0 ](https://rasa.com/docs/action-server)
- [RASA-X :0.38.1](https://rasa.com/docs/rasa-x/)

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python
- [Pipenv](https://pypi.org/project/pipenv/)
- [Docker](https://docs.docker.com/engine/install/)
- [Helm](https://helm.sh/docs/intro/install/)
- [Kubernetes](https://kubernetes.io/docs/setup/)

### Installation

- Clone the repository

  ```
  git clone https://github.com/sumanentc/COVID-19-bot.git
  ```

- Using RASA Shell and Stand alone Action Server

  1. Install dependencies

  ```
  pipenv shell

  pipenv install
  ```

  2. Train the model

  ```
  rasa train

  ```

  3. Start the Action Server

  ```
  rasa run actions -vv

  ```

  4. Start the RASA shell

  ```
  rasa shell -v
  ```

  5. Start asking questions on the RASA shell

- Using Docker Compose

1. Build Action Server Docker image

```
docker build actions/ -t sumand/rasa-action-server:2.5.0

docker push sumand/rasa-action-server:2.5.0

```

2. Build Rasa NLU Docker image

```
docker build . -t sumand/rasa-server:2.5.0

docker push sumand/rasa-server:2.5.0
```

3. Start the NLU Container

```
docker-compose up
```

4. Test the Bot

```
curl -XPOST localhost:5005/webhooks/rest/webhook -d '{"sender":"Me","message":"what is the total number of deaths in india"}'
```

- Using RASA-X

1.  Build Action Server Docker image

```
docker build actions/ -t sumand/rasa-action-server:2.5.0

docker push sumand/rasa-action-server:2.5.0

```

2. Build Rasa NLU Docker image

```
docker build . -t sumand/rasa-server:2.5.0

docker push sumand/rasa-server:2.5.0
```

3. Install RASA-X. I used [Helm-Chart](https://rasa.com/docs/rasa-x/installation-and-setup/install/helm-chart) for installation.

```
kubectl create namespace rasa

helm repo add rasa-x https://rasahq.github.io/rasa-x-helm

helm --namespace rasa install --values values.yml my-release rasa-x/rasa-x

helm --namespace rasa upgrade --values values.yml my-release rasa-x/rasa-x
```

4. Deploy [RASA-X](https://rasa.com/docs/rasa-x/installation-and-setup/deploy)

## Usage

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [M-Media-Group/Covid-19-API](https://github.com/M-Media-Group/Covid-19-API)
- [Install RASA-X using Helm Chart](https://rasa.com/docs/rasa-x/installation-and-setup/install/helm-chart/)
- [Co-WIN Public APIs](https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2)
