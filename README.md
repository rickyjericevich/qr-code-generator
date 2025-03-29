<!-- This readme is inspired from https://github.com/othneildrew/Best-README-Template -->

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicensed][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--   <a href="https://github.com/rickyjericevich/qr-code-generator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">QR Code Generator</h3>

  <p align="center">
    A simple QR code generator
    <br />
    <br />
<!--     <a href="https://github.com/rickyjericevich/qr-code-generator">View Demo</a> -->
<!--     &middot; -->
    <a href="https://github.com/rickyjericevich/qr-code-generator/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/rickyjericevich/qr-code-generator/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
        <!-- <li><a href="#configure-environment-variables">Configure environment variables</a></li>
        <li><a href="#build-the-docker-image">Build the Docker image</a></li>
        <li><a href="#run-the-container">Run the container</a></li> -->
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#url">URL</a></li>
        <li><a href="#payload">Payload</a></li>
        <li><a href="#response">Response</a></li>
        <li>
          <a href="#examples">Examples</a>
          <ul>
            <li><a href="#python">Python</a></li>
            <li><a href="#javascript">JavaScript</a></li>
          </ul>
        </li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li>
      <a href="#contributing">Contributing</a>
      <ul>
        <li><a href="#top-contributors">Top contributors</a></li>
      </ul>
    </li>
<!--     <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This project is a WIP solution to the Stellenbosch University's [Computer Science 113/114 Semester Project: A custom QR code generator](https://cs.sun.ac.za/courses/cs114/) for 2025.

<p align="right"><a href="#readme-top">Back to top</a></p>


### Built With

Vanilla Python for now 

<!-- [![Pydantic][Pydantic.dev]][Pydantic-url] -->


<p align="right"><a href="#readme-top">Back to top</a></p>



<!-- GETTING STARTED -->
## Getting Started

<!-- The instructions below are to run the app as a Docker container. If you want to run it locally, see the [Dockerfile](Dockerfile) for the setup steps. -->
TBD

<!-- ### Configure environment variables

Populate a .env file with the required variables. You can use [.env.example](.env.example) as a template.

`LOG_LEVEL`: One of the [logging module's log levels](https://docs.python.org/3/library/logging.html#logging-levels) (default=INFO).

`BASE_URL`: The domain or base url that the api is hosten on (default=localhost). See [Usage](#usage) for more detail.

### Build the Docker image
```
docker build -t qr_code_generator_img .
```

### Run the container
```
docker run --name qr_code_generator --env-file .env qr_code_generator_img
```


<p align="right"><a href="#readme-top">Back to top</a></p> -->



<!-- USAGE EXAMPLES -->
## Usage

<!-- At startup, this application listens on port ? for POST requests. When a client posts a request to the url, this app receives the message and attempt to process it.

For this application to correctly process messages, requests should be structured as follows:

### URL

The URL string must be of the form:

1. `BASE_URL/?`
2. ``



### Payload

The payload must be a stringified [JSON object literal](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON#json_structure).

The JSON object's key-value pairs must be ?. For example: ?

### Response



### Examples

Below are some code snippets that briefly demonstrates how clients would make requests and receive responses. Full examples can be found in the [examples folder](examples)

#### Python
Add a callback to receive response
```python
def on_message(client, userdata, msg):
    response = json_util.loads(msg.payload.decode())

...

client.on_message = on_message
```

Then post a message to the API URL to receive the QR code image
```python
def on_subscribe(client, userdata, mid, reason_code_list, properties):
    client.post(urk=, payload=, properties=)
```

#### JavaScript
```javascript

``` -->
TBD

<p align="right"><a href="#readme-top">Back to top</a></p>

<!-- ROADMAP -->

## Roadmap

<!-- - [ ] ? -->
TBD

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right"><a href="#readme-top">Back to top</a></p>

### Top contributors

<a href="https://github.com/rickyjericevich/qr-code-generator/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=rickyjericevich/qr-code-generator" alt="contrib.rocks image" />
</a>



<p align="right"><a href="#readme-top">Back to top</a></p>



<!-- CONTACT -->
## Contact

Ricky Jericevich - [linkedin.com/in/rickyjericevich](http://www.linkedin.com/in/rickyjericevich) - rickyjericevich@gmail.com

Project Link: [qr-code-generator](https://github.com/rickyjericevich/qr-code-generator)

<p align="right"><a href="#readme-top">Back to top</a></p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/rickyjericevich/qr-code-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/rickyjericevich/qr-code-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rickyjericevich/qr-code-generator.svg?style=for-the-badge
[forks-url]: https://github.com/rickyjericevich/qr-code-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/rickyjericevich/qr-code-generator.svg?style=for-the-badge
[stars-url]: https://github.com/rickyjericevich/qr-code-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/rickyjericevich/qr-code-generator.svg?style=for-the-badge
[issues-url]: https://github.com/rickyjericevich/qr-code-generator/issues
[license-shield]: https://img.shields.io/github/license/rickyjericevich/qr-code-generator.svg?style=for-the-badge
[license-url]: https://github.com/rickyjericevich/qr-code-generator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rickyjericevich
[product-screenshot]: images/screenshot.png
[python.org]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/
[Pydantic.dev]: https://img.shields.io/badge/Pydantic-000000?style=for-the-badge&logo=pydantic
[Pydantic-url]: https://pydantic.dev/