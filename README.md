# COVID-19 Bot

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
  - Which states are Least affected ?
  - What is the Recovery rate in Karnataka
  - What is the Recovery rate in Karnataka and Goa
  - What is the Mortality rate in Goa
- It can handle spelling mistakes.

- It can answers questions related to vaccination.

  - Number of people patially vaccinated in India
  - Number of people fully vaccinated

- It can handle out of context questions.

  - How are you?
  - How is the weather?

- It has RASA-X UI for Interactive training and usage

### Built With

- [Rasa : 2.0.2 ](https://rasa.com/docs/rasa/)
- [Python : 3.8 ](https://www.python.org/)
- [Rasa-SDK Action Server : 2.4.0 ](https://rasa.com/docs/action-server)

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python
- [Pipenv](https://pypi.org/project/pipenv/)
- [Docker](https://docs.docker.com/engine/install/)
- [Helm](https://helm.sh/docs/intro/install/)
- [Kubernetes](https://kubernetes.io/docs/setup/)

### Installation

## Usage

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [M-Media-Group/Covid-19-API](https://github.com/M-Media-Group/Covid-19-API)
- [Install RASA-X using Helm Chart](https://rasa.com/docs/rasa-x/installation-and-setup/install/helm-chart/)
