<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Testing & Data Science</h3>
  <p align="center">
    Software Engineering Practices
    <br />
    <a><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://docs.pytest.org/en/6.2.x/">Pytest documentation</a>
    ·
    <a href="https://docs.python.org/3/library/unittest.html">Unittest documentation</a>
    ·
    <a href="https://robotframework.org/">Robot documentation</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#pytest">Pytest</a>
      <ul>
        <li><a href="#introduction">Introduction</a></li>
      </ul>
        <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- Pytest -->
## Pytest

### Introduction

Pytest is a testing framework based on python. It is mainly used to write API test cases. This tutorial helps you understand:
* Installation of `pytest`
* Various concepts and features of pytest
* Sample programs

By the end of this tutorial, you should be able to start writing test cases using pytest.

### Prerequisites

The prerequisites to begin with this tutorial are:
* Familiarity with any programming language.
* Knowledge of basic programming concepts.
* [Python](https://www.python.org/doc/m) installed.


<!-- GETTING STARTED -->
## Getting Started

Pytest is a python based testing framework, which is used to write and execute test codes. In the present days of REST services, pytest is mainly used for API testing even though we can use pytest to write simple to complex tests, i.e., we can write codes to test API, database, UI, etc.

### Advantages of Pytest

The advantages of Pytest are as follows:
* Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
* Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
* Pytest allows us to skip a subset of the tests during execution.
* Pytest allows us to run a subset of the entire test suite.
* Pytest is free and open source.
* Because of its simple syntax, pytest is very easy to start with.

In this tutorial, we will explain the pytest fundamentals with sample programs.


<!-- USAGE EXAMPLES -->
## Environment Setup

To install the latest version of pytest, execute the following command −

```
pip install pytest
```
Confirm the installation using the following command to display the help section of pytest.
```bash
pytest --help
```

<!-- ROADMAP -->
## Identifying Test files and Test Functions

Running pytest without mentioning a filename will run all files of format <b>test_*.py</b> or <b>\*_test.py</b> in the current directory and subdirectories. Pytest automatically identifies those files as test files. We <b>can</b> make pytest run other filenames by explicitly mentioning them.

Pytest requires the test function names to start with test. Function names which are not of format <b>test*</b> are not considered as test functions by pytest. We <b>cannot</b> explicitly make pytest consider any function not starting with test as a <b>test</b> function.

We will understand the execution of tests in our subsequent chapters.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## Starting with basic test

Now, we will start with our first pytest program. We will first create a directory and thereby, create our test files in the directory.

Let us follow the steps shown below:

* Create a new directory named <b>pytest</b> and navigate into the directory in your command line.

* Create a file named <b>test_square.py</b> and add the below code to that file.

```python
import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def tesequality():
   assert 10 == 11
```
<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
