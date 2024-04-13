## Introduction
This README file provides information on how to use Pillow to manipulate pixel values in images and create effects like dissolve mode. Additionally, it includes a sample matrix to demonstrate the process.

## Installation
Before proceeding, make sure you have Pillow installed. You can install it using pip:

```bash
pip install Pillow
```
## Process
I changed the pixel values as per my preference. The output appeared as a dissolve effect.


![Dissolve Mode Image](src/dissolveMode(like).png)

-firstly I took mean values for r, g, b values of the pixels.
-then changed the values using this equation (r_exact + r_mean _randomVal)/3, here random value in ramnge of 0 to 255.
- for example, if r_exact = 10, r_mean = 100, randomVal = 50, then new value = (10 + 100 + 50)/3 = 53.33
- And used math.ceil() to get the upper nearest integer value.
